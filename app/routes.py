from fastapi import APIRouter, FastAPI, status
from fastapi.responses import JSONResponse

import asyncio
from .models import WebhookPayload
from .session_handler import handle_session_data
from .logger import logger


router = APIRouter()


@router.post("/webhook/")
async def webhook_endpoint(payload: WebhookPayload):
    task = asyncio.create_task(
        handle_session_data(payload.id), name=payload.id)
    logger.info(f"Task for session_id: {task.get_name()} created")

    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Received"})


def setup_routes(app: FastAPI) -> None:
    """:param app: FastAPI instance"""
    app.include_router(router)
