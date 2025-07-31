
#!/usr/bin/env python3

import os
from crewai import Agent, Task, Crew, Process
from crewai.llm import LLM

def create_llm():
    """Create LLM instance based on available API keys"""
    
    # Check for OpenRouter API key
    if os.getenv("OPENROUTER_API_KEY"):
        print("استخدام OpenRouter API")
        return LLM(
            model="openai/gpt-4o-mini",  # or any OpenRouter model
            api_key=os.getenv("OPENROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1"
        )
    
    # Check for Hugging Face API key
    elif os.getenv("HUGGINGFACE_API_KEY"):
        print("استخدام Hugging Face API")
        return LLM(
            model="huggingface/microsoft/DialoGPT-medium",
            api_key=os.getenv("HUGGINGFACE_API_KEY"),
            base_url="https://api-inference.huggingface.co/v1"
        )
    
    # Check for OpenAI API key
    elif os.getenv("OPENAI_API_KEY"):
        print("استخدام OpenAI API")
        return LLM(model="gpt-3.5-turbo")
    
    else:
        print("تحذير: لم يتم العثور على أي مفتاح API.")
        print("يرجى إضافة أحد المفاتيح التالية في أداة Secrets:")
        print("- OPENROUTER_API_KEY لاستخدام OpenRouter")
        print("- HUGGINGFACE_API_KEY لاستخدام Hugging Face")
        print("- OPENAI_API_KEY لاستخدام OpenAI")
        return None

# Set up a simple example
def main():
    # Create LLM instance
    llm = create_llm()
    if not llm:
        return
    
    # Create a simple agent
    researcher = Agent(
        role='Researcher',
        goal='Conduct thorough research on given topics',
        backstory='You are an experienced researcher with a passion for uncovering insights.',
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
    
    # Create a task
    research_task = Task(
        description='Research the latest trends in AI and write a brief summary',
        agent=researcher,
        expected_output='A brief summary of AI trends'
    )
    
    # Create crew
    crew = Crew(
        agents=[researcher],
        tasks=[research_task],
        verbose=2,
        process=Process.sequential
    )
    
    # Execute the crew
    result = crew.kickoff()
    print("Crew execution completed!")
    print(result)

if __name__ == "__main__":
    main()
