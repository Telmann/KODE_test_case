import httpx


async def text_check(text: str):
    url = "https://speller.yandex.net/services/spellservice.json/checkText"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params={"text": text})
        response.raise_for_status()
        return response.json()