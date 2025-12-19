from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict, Optional

app = FastAPI()

class AssessmentRequest(BaseModel):
    participants: Dict[str, str]
    config: Optional[Dict[str, Any]] = None

@app.get("/.well-known/agent-card.json")
def agent_card():
    return {
        "name": "GreenDummyAgent",
        "description": "Minimal green agent for AgentBeats registration",
    }

@app.post("/assessment_request")
def assessment_request(req: AssessmentRequest):
    return {
        "status": "ok",
        "artifact": {
            "summary": "GreenDummyAgent ran successfully.",
            "participants": req.participants,
            "config": req.config or {},
        }
    }