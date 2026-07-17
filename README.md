# My Coding Agent
- Hi. I made this coding agent with tutorials to understand how agents made.
- Currently agent can use 4 functions with tool calls which are get_director_files, get_file_content, write_file, run_python_file.
- Also agent can answer your questions with/without tool calls. 
- There is a loop and agent decides what to do.  
- I used openai library with openrouter/free api endpoint which has 50 request per day for free and it automatically selects the free model so agent's performance can vary in each chat.
- set up project by cloning and creating a dotenv and your api key inside.
- There is a calculator app to try and test my agent on mini project.
- agent lives inside calculator directory and cant see outside of it. You can set it however you want in main.py but be careful as it may change anything in your computer.
---
- example usage is:
```uv run main.py "fix my calculator app"```
