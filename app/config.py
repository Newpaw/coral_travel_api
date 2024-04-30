import os
from dotenv import load_dotenv
import asyncio

load_dotenv()


class Settings:
    def __init__(self):
        self.API_USERNAME = os.getenv("API_USERNAME")
        self.API_PASSWORD = os.getenv("API_PASSWORD")
        self.AUTH_URL = os.getenv("AUTH_URL")
        self.SESSIONS_URL = os.getenv("SESSIONS_URL")
        self.DESTINATION_URL = os.getenv("DESTINATION_URL")
        self.ACCESS_TOKEN_EXPIRY = int(os.getenv("ACCESS_TOKEN_EXPIRY", 3600))
        self.token = None
        self.token_timestamp = None
        self.LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    def is_token_expired(self):
        if not self.token or (asyncio.get_event_loop().time() - self.token_timestamp) > self.ACCESS_TOKEN_EXPIRY:
            return True
        return False

    def update_token(self, token, timestamp):
        self.token = token
        self.token_timestamp = timestamp


settings = Settings()
