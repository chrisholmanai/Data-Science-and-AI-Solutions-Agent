from fastapi import APIRouter
from agent_core.agent_runner import run_agent

router = APIRouter()

@router.get("/agent")
def agent_response(q: str):
    return {"response": run_agent(q)}