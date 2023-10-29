from tqdm import tqdm
from logger import Logger
# from threading import Thread
import os

logger = Logger(no_log_file=True)

class Downloader():
    def __init__(self,  stream, streamLength:int, out_dir:str, title:str="file"):
        self.title = title
        self.stream = stream
        self.streamLength = streamLength
        self.out_dir = out_dir
        self.__bar_format = "{desc}: {percentage:3.0f}%[{n_fmt}/{total_fmt}][{remaining}][{rate_fmt}{postfix}]"

    def __progress(self):
        return tqdm(
            desc=self.title,
            total=self.streamLength,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
            dynamic_ncols=True,
            bar_format=self.__bar_format)

    def __check_dir_and_file_exists(self):
        if not os.path.isdir(self.out_dir):
            os.makedirs(self.out_dir)
        else:
            logger.log_error("the dir exists")

        if not os.path.isfile("{}/{}.mp4".format(self.out_dir, self.title)):
            logger.log_info("make out file")
        else:
            logger.log_error("the file exists")

    def download(self):
        self.__check_dir_and_file_exists()

        with open(file="{}/{}.mp4".format(self.out_dir, self.title), mode='wb') as file:
            bar = self.__progress()
            for content in self.stream.iter_content(chunk_size=1024):
                size = file.write(content)
                bar.update(size)
                if file.closed:
                    logger.log_info("load complete")
        