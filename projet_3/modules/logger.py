from loguru import logger

logger.add(
    "projet_3.log",
    rotation="1 week",
    level="INFO"
)