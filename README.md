# jutsu Parser
## Буду по возможности дорабатывать и исправлять ошибки.
```python
from jutsuParser import Anime, Episode
from downloader import Downloader

anime = Anime("URL TO ANIME")

title = anime.get_title() # название аниме
anime.get_description() # описание
anime.get_arches() # список арок
anime.get_films() # вернет список фильмов
anime.get_episodes() # вернет список всех серий
anime.get_first_episode() # вернёт первый эпизод
anime.get_last_episode() # вернет последний эпизод
anime.get_episodes_by_arches() # вернет словарь: арка + принадлежащие ей эпизоды

episode = Episode("URL TO EPISODE")

episode.get_title_plus_serial_number() # вернет название аниме + сезон + серия "Ванпанчмен 1 сезон 1 серия"
episode.get_full_title() # вернет реальное название серии "Ванпанчмен 1 серия: сильнейший человек"
episode.get_next_episode() # вернет следующий эпизод (если есть)
episode.get_early_episode() # вернет предыдущий эпизод
episode.get_direct_link() # вернет прямую ссылку на серию
stream, contentLength = episode.get_stream("разрешение: 360, 480, 720, 1080") # вернет список [stream, contentLength]

Downloader(stream=stream, streamLength=contentLength, out_dir=".\\", title=title).download() # скачает серию
```
