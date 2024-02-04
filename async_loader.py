import asyncio
import httpx
import tqdm
from config import HEADERS

class AsyncLoader():

    def __init__(self):
        self.urls:list
        self.extention:str = 'bytestream'

    def set_urls(self, urls):
        self.urls = urls

    def set_ext(self, extention: str):
        self.extention = extention

    async def __download_files(self, url: str, filename: str):
        with open(filename.strip() + f'.{self.extention}', 'wb') as f:
            async with httpx.AsyncClient() as client:
                async with client.stream('GET', url, headers=HEADERS) as r:
                    
                    r.raise_for_status()
                    total = int(r.headers.get('content-length', 0))

                    tqdm_params = {
                        'desc': filename,
                        'total': total,
                        'miniters': 1,
                        'unit': 'it',
                        'unit_scale': True,
                        'unit_divisor': 1024,
                    }

                    with tqdm.tqdm(**tqdm_params) as pb:
                        async for chunk in r.aiter_bytes():
                            pb.update(len(chunk))
                            f.write(chunk)


    async def __make_tasks(self):

        loop = asyncio.get_running_loop()

        tasks = [loop.create_task(self.__download_files(url, filename)) for url, filename in self.urls]

        await asyncio.gather(*tasks, return_exceptions=True)

    def go(self):
        asyncio.run(self.__make_tasks())