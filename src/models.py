from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date

class ActionItem(BaseModel):
    task: str = Field(..., description="The specific action to be taken")
    assignee: Optional[str] = Field(None, description="The person responsible for the task")
    due_date: Optional[date] = Field(None, description="The deadline for the task if mentioned")

class MeetingSummary(BaseModel):
    summary: str
    action_items: List[ActionItem]

class TranscriptInput(BaseModel):
    transcript: str

class ExportRequest(BaseModel):
    target_system: str
    items: List[ActionItem]