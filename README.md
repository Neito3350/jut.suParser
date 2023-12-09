# jutsu Parser

## Последние изменения:
**[09.12.23]:
    1. Удален класс "Jutsu"
    1. Исправлен импорт "logger" в "loader.py"
    1. Методы "get_number" и "get_title" в классе "Episode" собраны в один: 1. 1. 1. "get_titles" - возвращает список: [название аниме + сезон + серия, название эпизода]
    1. Метод "get_direct_link" был скрыт ("__get_direct_link")
    1. Классы "Anime" и "Episode" разделены по файлам**

## Пример:
```python
from Anime import Anime
from Episode import Episode
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
episode.get_titles() # [название аниме + сезон + серия, название эпизода]
episode.get_next_episode() # следующий эпизод (если есть)
episode.get_early_episode() # предыдущий эпизод
episode.get_direct_link() # прямая ссылка на серию
episode.get_stream("разрешение: 360, 480, 720, 1080") # список [stream, contentLength]

# использование загрузчика
filename = episode.get_titles()[0]
stream, contentLength = episode.get_stream("480")
loader = Loader(stream = stream, contentLength = contentLength, filename = filename)
loader.download()
```
