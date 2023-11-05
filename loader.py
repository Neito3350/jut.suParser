from newlogger import Logger
from tqdm import tqdm
import os

log = Logger(write_to_logfile = True)

class Loader():

    def __init__(self, stream, contentLength:int, filename:str = "exampleFile", out_dir:str = ".\\"):
        self._stream = stream
        self._contentLength = contentLength
        self._filename = filename
        self._out_dir = out_dir
        self._bar_format = "{desc}: {percentage:3.0f}%[{n_fmt}/{total_fmt}][{remaining}][{rate_fmt}{postfix}]" 

    def set_bar_format(self, bar_format_string:str):
        # устанавливает формат вывода прогреса загрузки
        self._bar_format = bar_format_string

    def __progress(self):
        # вернет объект класса tqdm
        return tqdm(
            desc = self._filename,
            total = self._contentLength,
            unit = "B",
            unit_scale = True,
            unit_divisor = 1024,
            dynamic_ncols = True,
            bar_format = self._bar_format
        )
    
    def __dir_exists_check(self):
        # проверит существует ли директория, если нет то создаст
        if not os.path.isdir(self._out_dir):
            os.makedirs(self._out_dir)
        else:
            log.setlog("директория существует")

    def __file_exists_check(self):
        # проверит существует ли файл
        if not os.path.isfile("{}/{}.mp4".format(self._out_dir, self._filename)):
            return False
        else:
            return True

    def download(self):
        # загружает файл
        self.__dir_exists_check()

        if not self.__file_exists_check():
            with open(file = f"{self._out_dir}\\{self._filename}.mp4", mode = "wb") as file:
                bar = self.__progress()

                for content in self._stream.iter_content(chunk_size = 1024):
                    bar.update(file.write(content))
                    if file.closed:
                        log.setlog("загрузка завершена")
        else:
            log.setlog("файл существует")