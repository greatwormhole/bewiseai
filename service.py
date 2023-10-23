import aiohttp

from conf import URL_PATH

async def get_random_posts(amount: int):
    
    relative_path = '/api/random'
    kwargs = f'?count={amount}'
    URI = URL_PATH + relative_path + kwargs # temp
    
    async with aiohttp.ClientSession() as session:
        async with session.get(URI) as resp:
            return await resp.text()