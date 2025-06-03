from fastapi import FastAPI
from routes.agent import router as agent_router

app = FastAPI()
app.include_router(agent_router)