import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse
from prompts import system_prompt
from call_function import avaiable_functions, call_function
import json


def main():
    print("Hello from my-coding-agent!")

    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")

    if api_key is None:
        raise RuntimeError("api key is not found")

    client = OpenAI(
        base_url = "https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [
        { "role": "system", "content": system_prompt },
        { "role": "user", "content": args.user_prompt }
    ]

    is_finished = False
    for _ in range(20):
        response = client.chat.completions.create(
            model = "openrouter/free",
            messages = messages,
            tools=avaiable_functions,
            temperature=0 # if more deterministic results needed
        )

        if response.usage is None:
            raise RuntimeError("Failed API request")

        message = response.choices[0].message

        if message.tool_calls:
            for tool_call in message.tool_calls:
                result_message = call_function(tool_call, verbose=True)

                if not result_message["content"]:
                    raise Exception("Error getting result content of the function run")
            
                temp_str = result_message["content"]
                result_message["content"] = f"Here's the result of {tool_call.function.name}: {temp_str}"
                messages.append(result_message)

            if args.verbose:
                print(f"-> {result_message['content']}")
        else:
            if args.verbose:
                print(f"User prompt: {args.user_prompt}")
                print(f"Prompt tokens: {response.usage.prompt_tokens}")
                print(f"Response tokens: {response.usage.completion_tokens}")

            is_finished = True
            messages.append(message)
            break
        

    if is_finished:
        print(f"Final response: {messages[-1].content}")
    else:
        print("Has reached to the limit. It is interrupted and not finished")



if __name__ == "__main__":
    main()
