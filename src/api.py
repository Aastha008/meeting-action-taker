from fastapi import FastAPI, HTTPException
from src.models import TranscriptInput, MeetingSummary, ExportRequest
from src.core import ActionExtractor

app = FastAPI(title="Meeting Action Taker")
extractor = ActionExtractor()

@app.post("/process", response_model=MeetingSummary)
async def process_transcript(data: TranscriptInput):
    try:
        return await extractor.process_transcript(data.transcript)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/export")
async def export_items(request: ExportRequest):
    # Logic to push to external systems would go here
    return {"status": "success", "pushed_items": len(request.items), "system": request.target_system}