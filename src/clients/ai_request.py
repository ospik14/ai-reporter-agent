import json
import os
from dotenv import load_dotenv
from google import generativeai as genai
from config.promts import CONTENT_SELECTION_PROMT
from schemas.article import ArticleBase

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3-flash-preview')

async def content_selection(content: list):
    news = "\n\n".join(
        f'id: {article.id} \ntitle: {article.title} \ndescription: {article.description}'
        for article in content
    )
    promt = CONTENT_SELECTION_PROMT + news

    response = await model.generate_content_async(
        promt,
        generation_config=genai.GenerationConfig(
            response_mime_type="application/json"
        )
    )
    
    data = json.loads(response.text)
    
    return data