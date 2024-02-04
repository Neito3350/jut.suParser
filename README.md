# jutsu Parser

## Пример:
```python
from Anime import Anime
from Episode import Episode
from async_loader import AsyncLoader

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
episode.get_titles() # [название аниме + сезон + серия, название эпизода]
episode.get_next_episode() # следующий эпизод (если есть)
episode.get_early_episode() # предыдущий эпизод
episode.get_direct_link() # прямая ссылка на серию
# episode.get_stream("разрешение: 360, 480, 720, 1080") # список [stream, contentLength]

# использование асинхронного загрузчика
filename = episode.get_titles()[0]
direct_link = episode.get_direct_link('1080')

asl = AsyncLoader()
asl.set_ext('mp4')
asl.set_urls([(direct_link, filename)]) # тут можно указать несколько кортежей с ссылками и названиями, они будут загружаться параллельно
asl.go()
```
