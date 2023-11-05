# jutsu Parser
## Использование:
```python
from jutsuParser import Anime, Episode
from downloader import Downloader

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
```
