import requests
import tqdm
from config import LOAD_HEADERS


def __download_files(url: str, filename: str):
    with open(f".\\{filename}", 'wb') as f:
        with requests.get(url, stream=True, headers=LOAD_HEADERS) as r:
            
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
                for chunk in r.iter_content(chunk_size=1024):
                    pb.update(len(chunk))
                    f.write(chunk)


def load(url:str, filename:str):
    __download_files(url, filename)

