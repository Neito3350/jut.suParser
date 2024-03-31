# jutsu Parser

Асинхронный загрузчик создан на основе этого: https://github.com/pythontoday/download_files_with_progress_bar

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

"ASYNC_LOADER ОТПРАВЛЕН НА ДОРАБОТКУ!"

# # использование асинхронного загрузчика
# filename = episode.get_titles()[0] # получаем название серии
# direct_link = episode.get_direct_link('1080') # получаем прямую ссылку на эпизод

# aloader = AsyncLoader() # создаем объект класса AsyncLoader

# # настраиваем
# aloader.configure(
#     urls = [(direct_link, filename)], # передаем данные в таком формате [(ссылка, название файла)]
#     extention = ".mp4", # указываем расширение
#     numbers_of_downloads = 2 # указываем количество одновременно загружаемых файлов (желательно не более 3-х)
# )

aloader.go() # запускаем загрузчик и ждем...
```
