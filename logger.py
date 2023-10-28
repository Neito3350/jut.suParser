from time import gmtime, strftime

class Logger():

    def __init__(self, no_log_file:bool=True) -> None:
        self.__no_log_file = no_log_file
        self._LOG_INFO = "[INFO]"
        self._LOG_ERROR = "[ERROR]"

    def __log(self, log_type, message):
        timeNow = strftime("%H:%M:%S", gmtime())
        print(f"[{timeNow}]{log_type}: {message};")

        if not self.__no_log_file:
            with open("log.txt", "a+", encoding="utf-8") as logfile:
                logfile.write(f"[{timeNow}]{log_type}: {message};\n")
            
    def log_info(self, message):
        self.__log(self._LOG_INFO, message)

    def log_error(self, message):
        self.__log(self._LOG_ERROR, message)