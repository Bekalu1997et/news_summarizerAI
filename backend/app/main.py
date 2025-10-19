from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .scraper import scrape_article
from .summarizer import generate_summary

app = FastAPI(title="News Summarizer API")

class SummarizeRequest(BaseModel):
    url: str

@app.post("/summarize")
async def summarize(request: SummarizeRequest):
    try:
        article = scrape_article(request.url)
        summaries = {
            "short": generate_summary(article,"short"),
            "medium": generate_summary(article,"medium"),
            "long": generate_summary(article, "long")
        }
        return {"url": request.url, "summaries": summaries}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))