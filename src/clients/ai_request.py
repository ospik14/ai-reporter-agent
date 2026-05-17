import os
from dotenv import load_dotenv
from google import generativeai
from config.promts import CONTENT_SELECTION_PROMT

load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

model = generativeai.GenerativeModel('gemini-3-flash-preview')

async def content_selection(content: list):
    news = "\n\n".join(
        f'id: {article.id} \ntitle: {article.title} \ndescription: {news.description}'
        for article in content
    )

    promt = CONTENT_SELECTION_PROMT + news