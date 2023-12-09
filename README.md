# jutsu Parser

## Пример:
```python
from Anime import Anime
from Episode import Episode
from loader import Loader

# методы класса Anime
anime = Anime("URL TO ANIME")
anime.get_title() # -> str: название аниме
anime.get_description() # -> str: описание
anime.get_arches() # -> list: список арок
anime.get_films() # -> list: список фильмов
anime.get_episodes() # -> list: список всех серий
anime.get_first_episode() # -> str: первый эпизод
anime.get_last_episode() # -> str: последний эпизод
anime.get_episodes_by_arches() # -> dict: арка + принадлежащие ей эпизоды
anime.get_slogan() # -> str: слоган
anime.get_specs() # -> list: жанр, год выпуска, темы, возрастной рейтинг, оригинальное название

# методы класса Episode
episode = Episode("URL TO EPISODE")
episode.get_titles() # -> list: название аниме + сезон + серия; название эпизода
episode.get_next_episode() # -> str: следующий эпизод (если есть)
episode.get_early_episode() # -> str: предыдущий эпизод
episode.get_direct_link() # -> str: прямая ссылка на серию
episode.get_stream("разрешение: 360, 480, 720, 1080") # -> list: список [stream, contentLength]

# использование загрузчика
filename = episode.get_titles()[0]
stream, contentLength = episode.get_stream("480") -> list
loader = Loader(stream = stream, contentLength = contentLength, filename = filename)
loader.download()
```
