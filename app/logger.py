import logging
from .config import settings

log_level = settings.LOG_LEVEL
numeric_level = getattr(logging, log_level, None)
if not isinstance(numeric_level, int):
    raise ValueError(f"Invalid log level: {log_level}")
logging.basicConfig(
    level=numeric_level,
    format="%(asctime)s - %(name)s - %(filename)s - %(levelname)s - %(message)s"
)

# Create a logger object
logger = logging.getLogger("uvicorn")

logger.info(f"Log level set to {log_level}")
