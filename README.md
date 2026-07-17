- There is a calculator app to try and test my agent on mini project.
- Currently agent can use 4 functions with tool calls which are get_director_files, get_file_content, write_file, run_python_file.
- Also agent can speak directly. 
- There is a loop and agent decides what to do. 
- I used openai library with openrouter/free api endpoint which has 50 request per day for free and it automatically selects the free model so agent's performance can vary in each chat.
- set up project by cloning and creating a dotenv and your api key inside.  

- example usage is:
```uv run main.py "fix my calculator app"```
