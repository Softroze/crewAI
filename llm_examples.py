
#!/usr/bin/env python3

import os
from crewai.llm import LLM

def create_openrouter_llm():
    """Create OpenRouter LLM instances with different models"""
    
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("OPENROUTER_API_KEY غير موجود")
        return None
    
    # Examples of popular OpenRouter models
    models = {
        "gpt-4o": "openai/gpt-4o",
        "gpt-4o-mini": "openai/gpt-4o-mini", 
        "claude-3.5-sonnet": "anthropic/claude-3.5-sonnet",
        "llama-3.1-70b": "meta-llama/llama-3.1-70b-instruct",
        "gemini-pro": "google/gemini-pro"
    }
    
    # Create LLM instance
    llm = LLM(
        model=models["gpt-4o-mini"],  # Change to desired model
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
        temperature=0.7
    )
    
    return llm

def create_huggingface_llm():
    """Create Hugging Face LLM instance"""
    
    api_key = os.getenv("HUGGINGFACE_API_KEY") 
    if not api_key:
        print("HUGGINGFACE_API_KEY غير موجود")
        return None
    
    # Popular Hugging Face models
    models = {
        "mistral-7b": "mistralai/Mistral-7B-Instruct-v0.1",
        "llama-2-7b": "meta-llama/Llama-2-7b-chat-hf",
        "codellama": "codellama/CodeLlama-7b-Instruct-hf"
    }
    
    llm = LLM(
        model=models["mistral-7b"],  # Change to desired model
        api_key=api_key,
        base_url="https://api-inference.huggingface.co/v1",
        temperature=0.7
    )
    
    return llm

def create_local_ollama_llm():
    """Create local Ollama LLM instance"""
    
    llm = LLM(
        model="ollama/llama3.2",  # or any locally installed model
        base_url="http://localhost:11434",
        temperature=0.7
    )
    
    return llm

if __name__ == "__main__":
    print("أمثلة على LLM providers مختلفة:")
    
    # OpenRouter example
    openrouter_llm = create_openrouter_llm()
    if openrouter_llm:
        print("✅ OpenRouter LLM تم إنشاؤه بنجاح")
    
    # Hugging Face example  
    hf_llm = create_huggingface_llm()
    if hf_llm:
        print("✅ Hugging Face LLM تم إنشاؤه بنجاح")
    
    # Local Ollama example
    try:
        ollama_llm = create_local_ollama_llm()
        print("✅ Ollama LLM تم إنشاؤه بنجاح")
    except Exception as e:
        print(f"❌ Ollama غير متوفر: {e}")
