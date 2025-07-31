
# دليل إعداد نماذج اللغة (LLMs)

## المفاتيح المطلوبة

### 1. OpenRouter
- اذهب إلى [OpenRouter](https://openrouter.ai)
- أنشئ حساب واحصل على API key
- أضف `OPENROUTER_API_KEY` في أداة Secrets في Replit

### 2. Hugging Face
- اذهب إلى [Hugging Face](https://huggingface.co)
- أنشئ حساب واذهب إلى Settings > Access Tokens
- أنشئ token جديد واحصل على API key
- أضف `HUGGINGFACE_API_KEY` في أداة Secrets في Replit

### 3. OpenAI (اختياري)
- اذهب إلى [OpenAI](https://platform.openai.com)
- احصل على API key
- أضف `OPENAI_API_KEY` في أداة Secrets في Replit

## النماذج المدعومة

### OpenRouter
- `openai/gpt-4o` - أحدث نموذج من OpenAI
- `openai/gpt-4o-mini` - نسخة مصغرة وأرخص
- `anthropic/claude-3.5-sonnet` - نموذج Claude من Anthropic
- `meta-llama/llama-3.1-70b-instruct` - نموذج Llama من Meta
- `google/gemini-pro` - نموذج Gemini من Google

### Hugging Face
- `mistralai/Mistral-7B-Instruct-v0.1` - نموذج Mistral
- `meta-llama/Llama-2-7b-chat-hf` - نموذج Llama 2
- `codellama/CodeLlama-7b-Instruct-hf` - نموذج للبرمجة

## كيفية الاستخدام

```python
from crewai.llm import LLM

# استخدام OpenRouter
llm = LLM(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# استخدام Hugging Face  
llm = LLM(
    model="mistralai/Mistral-7B-Instruct-v0.1",
    api_key=os.getenv("HUGGINGFACE_API_KEY"),
    base_url="https://api-inference.huggingface.co/v1"
)
```

## تشغيل الأمثلة

```bash
# تشغيل المثال الأساسي
uv run python example_crew.py

# تشغيل أمثلة LLM مختلفة
uv run python llm_examples.py
```
