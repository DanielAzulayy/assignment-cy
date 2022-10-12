from fastapi import APIRouter
from loguru import logger
from starlette.responses import Response

from app.models.words import Words
from app.services.words import WordsService
from app.utils.words import parse_words

router = APIRouter()
words_service = WordsService()


@router.get("/api/v1/words")
async def get_words():
    try:
        return words_service.words_counter
    except Exception as exception:
        logger.error(f"Failed get_words. {exception=}")
        return Response("Internal server error", status_code=500)


@router.post("/api/v1/words")
async def add_words(words: Words):
    try:
        if words.value is None:
            return Response("Words should be given.", status_code=500)
        if parsed_words := parse_words(words.value):
            words_service.count_words(parsed_words)
        return Response("Words added. 'ACK'", status_code=200)
    except Exception as exception:
        logger.error(f"Failed to add_words. {exception=}")
        return Response("Internal server error", status_code=500)


@router.get("/api/v1/words/frequency_distribution_rank")
async def frequency_distribution_rank():
    try:
        return words_service.frequency_rank()
    except Exception as exception:
        logger.error(f"Failed to count frequency distribution rank. {exception=}")
        return Response("Internal server error", status_code=500)
