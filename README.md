# jut.su Parser

> [!NOTE]
> Парсер в разработке, будут ошибки.
> Приложение с графическим интерфейсом под управлением "DearPyGUI" в разработке...

> [!WARNING]
> Некоторые эпизоды недоступны в определенных странах.

### Возможности
- **CLASS "ANIME":**

    - **НАЗВАНИЕ**
        ```python
        from jutsuParser import Anime

        anime = Anime("https://jut.su/onepunchman")
        anime.get_title() # возвращает строку с названием аниме
        ```
    - **ОПИСАНИЕ**
        ```python
        from jutsuParser import Anime

        anime = Anime("https://jut.su/onepunchman")
        anime.get_deskription() # возвращает строку с описанием аниме
        ```
    - **ФИЛЬМЫ**
        ```python
        from jutsuParser import Anime

        anime = Anime("https://jut.su/onepunchman")
        anime.get_films() # возвращает список ссылок на фильмы
        ```
    - **СПИСОК АРОК**
        ```python
        from jutsuParser import Anime

        anime = Anime("https://jut.su/onepunchman")
        anime.get_arches() # возвращает список арок (если они есть)
        ```
    - **ВСЕ ЭПИЗОДЫ**
        ```python
        from jutsuParser import Anime

        anime = Anime("https://jut.su/onepunchman")
        anime.get_episodes() # возвращает список ссылок на эпизоды
        ```
    - **ПЕРВЫЙ ЭПИЗОД**
        ```python
        from jutsuParser import Anime

        anime = Anime("https://jut.su/onepunchman")
        anime.get_first_episode() # возвращает первый эпизод
        ```
    - **ПОСЛЕДНИЙ ЭПИЗОД**
        ```python
        from jutsuParser import Anime

        anime = Anime("https://jut.su/onepunchman")
        anime.get_last_episode() # возвращает последний эпизод
        ```
    - **АРКА + ПРИНАДЛЕЖАЩИЕ ЕЙ ЭПИЗОДЫ**
        ```python
        from jutsuParser import Anime

        anime = Anime("https://jut.su/onepunchman")
        anime.get_episodes_by_arches() # возвращает словарь: арка + эпизоды этой арки
        """
        episodesByArches = {
            "Первая арка":["1 серия", "2 серия", "3 серия", ...],
            "Вторая арка":["7 серия", "8 серия", "9 серия", ...]
            и т.д
        }
        """
        ```

- **CLASS "EPISODE":**

    - **НАЗВАНИЕ АНИМЕ + СЕЗОН + СЕРИЯ**
        ```python
        from jutsuParser import Episode

        episode = Episode("https://jut.su/onepunchman/episode-1.html")
        episode.get_title_plus_serial_number() # вернет: Ванпанчмен 1 сезон 1 серия
        ```
    - **НАЗВАНИЕ СЕРИИ**
        ```python
        from jutsuParser import Episode

        episode = Episode("https://jut.su/onepunchman/episode-1.html")
        episode.get_full_title() # вернет: Сильнейший человек
        ```
    - **СЛЕДУЮЩИЙ ЭПИЗОД**
        ```python
        from jutsuParser import Episode

        episode = Episode("https://jut.su/onepunchman/episode-1.html")
        episode.get_next_episode() # вернет следующий эпизод
        ```
    - **ПРЕДЫДУЩИЙ ЭПИЗОД**
        ```python
        from jutsuParser import Episode

        episode = Episode("https://jut.su/onepunchman/episode-1.html")
        episode.get_early_episode() # вернет предыдущий эпизод
        ```
    - **ПРЯМАЯ ССЫЛКА НА ЭПИЗОД**
        ```python
        from jutsuParser import Episode

        episode = Episode("https://jut.su/onepunchman/episode-1.html")
        episode.get_direct_link() # вернет прямую ссылку на эпизод
        ```
    - **СТРИМ (GET_STREAM)**
        ```python
        from jutsuParser import Episode

        episode = Episode("https://jut.su/onepunchman/episode-1.html")
        stream, contentLength = episode.get_stream("1080") # принимает аргумент resolution (360, 480, 720, 1080); вернет список [stream, streamLength]
        ```

- **CLASS "DOWNLOADER":**
    - **ЗАГРУЗКА ВИДЕО**
        ```python
        from jutsuParser import Episode
        from downloader import Downloader

        episode = Episode("https://jut.su/onepunchman/episode-1.html")
        title = episode.get_title_plus_series_number()
        stream, contentLength = episode.get_stream("480")
        Downloader(stream=stream, streamLength=contentLength, out_dir=".\\", title=title).download()
        ```