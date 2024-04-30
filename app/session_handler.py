import httpx
import asyncio
from .config import settings
from .logger import logger


async def authenticate():
    data = {
        "response_type": "token",
        "grant_type": "client_credentials",
        "client_id": settings.API_USERNAME,
        "client_secret": settings.API_PASSWORD
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(settings.AUTH_URL, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
        logger.info(f"Authentication response: {response.status_code}")
        response_data = response.json()
        settings.update_token(
            response_data['access_token'], asyncio.get_event_loop().time())


async def fetch_session_data(session_id: int):
    if settings.is_token_expired():
        logger.info("Token is expired, authenticating...")
        await authenticate()
    headers = {"Authorization": f"Bearer {settings.token}",
               "Accept": "application/json"}
    async with httpx.AsyncClient() as client:
        response = await client.get(settings.SESSIONS_URL.format(id=session_id), headers=headers)
        logger.info(f"Data fetched from {settings.SESSIONS_URL.format(id=session_id)} with response: {response.status_code}")
        return response.json()


async def handle_session_data(session_id: int):
    session_data = await fetch_session_data(session_id)
    await send_data_to_destination(session_data)
    return session_data


async def send_data_to_destination(data):
    async with httpx.AsyncClient() as client:
        response = await client.post(settings.DESTINATION_URL, json=data)
        logger.info(
            f"Data sent to {settings.DESTINATION_URL} with response: {response.status_code}")
