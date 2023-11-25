# jutsu Parser
## Использование:
```python
from jutsuParser import Anime, Episode, Jutsu
from loader import Loader

# методы класса Anime
anime = Anime("URL TO ANIME")
anime.get_title() # название аниме
anime.get_description() # описание
anime.get_arches() # список арок
anime.get_films() # список фильмов
anime.get_episodes() # список всех серий
anime.get_first_episode() # первый эпизод
anime.get_last_episode() # последний эпизод
anime.get_episodes_by_arches() # арка + принадлежащие ей эпизоды
anime.get_slogan() # слоган
anime.get_specs() # жанр, год выпуска, темы, возрастной рейтинг, оригинальное название

# методы класса Episode
episode = Episode("URL TO EPISODE")
episode.get_number() # название аниме + сезон + серия "Ванпанчмен 1 сезон 1 серия"
episode.get_title() # реальное название серии "сильнейший человек"
episode.get_next_episode() # следующий эпизод (если есть)
episode.get_early_episode() # предыдущий эпизод
episode.get_direct_link() # прямая ссылка на серию
episode.get_stream("разрешение: 360, 480, 720, 1080") # список [stream, contentLength]

# методы класса Jutsu
jutsu = Jutsu()
jutsu.get_anime_blocks(url="URL TO ANIME LIST", pages_number=1) # словарь {"название":{"link":"ссылка", "info":[сезоны, серии, фильмы]}}
jutsu.get_all_anime(pages=5, write_to_json=True) # вернет словарь {"название":{"link":"ссылка", "info":[сезоны, серии, фильмы]}} с указанного количества страниц (при необходимости запишет в json файл)

# использование загрузчика
filename = episode.get_number()
stream, contentLength = episode.get_stream("480")
loader = Loader(stream = stream, contentLength = contentLength, filename = filename)
loader.download()
```
