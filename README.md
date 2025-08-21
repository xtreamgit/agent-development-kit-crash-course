# Agent Development Kit (ADK) Crash Course

This repository contains examples for learning Google's Agent Development Kit (ADK), a powerful framework for building LLM-powered agents.

## This repository was provided by bhancockio.
https://github.com/bhancockio/agent-development-kit-crash-course.git

Out of the 12 examples, I'm focusing at the last 8 examples (5-12) and I'm skipping the first 4 examples because in course number 5 Brandon explains how to use the ADK and agent values (sessions, id, state, etc.) to create a web application.

## Getting Started

### Setup Environment

You only need to create one virtual environment for all examples in this course. Follow these steps to set it up:

```bash
# Create virtual environment in the root directory
python -m venv .venv

# Activate (each new terminal)
# macOS/Linux:
source .venv/bin/activate
# Windows CMD:
.venv\Scripts\activate.bat
# Windows PowerShell:
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

Once set up, this single environment will work for all examples in the repository.

### Setting Up API Keys

1. Create an account in Google Cloud https://cloud.google.com/?hl=en
2. Create a new project
3. Go to https://aistudio.google.com/apikey
4. Create an API key
5. Assign key to the project
6. Connect to a billing account

Each example folder contains a `.env.example` file. For each project you want to run:

1. Open the `.env.example` file
2. Rename `.env.example` to `.env` 
3. Open the `.env` file and replace the placeholder with your API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
Remember to put the .env file in the root directory of the project which is the folder with the number in front.

You'll need to repeat this for each example project you want to run.

## Examples Overview

Here's what you can learn from each example folder:

### 1. Basic Agent
Introduction to the simplest form of ADK agents. Learn how to create a basic agent that can respond to user queries.

### 2. Tool Agent
Learn how to enhance agents with tools that allow them to perform actions beyond just generating text.

### 3. LiteLLM Agent
Example of using LiteLLM to abstract away LLM provider details and easily switch between different models.

### 4. Structured Outputs
Learn how to use Pydantic models with `output_schema` to ensure consistent, structured responses from your agents.

### 5. Sessions and State
Understand how to maintain state and memory across multiple interactions using sessions.

### 6. Persistent Storage
Learn techniques for storing agent data persistently across sessions and application restarts.

### 7. Multi-Agent
See how to orchestrate multiple specialized agents working together to solve complex tasks.

### 8. Stateful Multi-Agent
Build agents that maintain and update state throughout complex multi-turn conversations.

### 9. Callbacks
Implement event callbacks to monitor and respond to agent behaviors in real-time.

### 10. Sequential Agent
Create pipeline workflows where agents operate in a defined sequence to process information.

### 11. Parallel Agent
Leverage concurrent operations with parallel agents for improved efficiency and performance.

### 12. Loop Agent
Build sophisticated agents that can iteratively refine their outputs through feedback loops.

## Official Documentation

For more detailed information, check out the official ADK documentation:
- https://google.github.io/adk-docs/get-started/quickstart

## Support

Need help or run into issues? Join our free AI Developer Accelerator community on Skool:
- [AI Developer Accelerator Community](https://www.skool.com/ai-developer-accelerator/about)

In the community you'll find:
- Weekly coaching and support calls
- Early access to code from YouTube projects
- A network of AI developers of all skill levels ready to help
- Behind-the-scenes looks at how these apps are built
