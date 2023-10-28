from time import gmtime, strftime

class Logger():

    def __init__(self) -> None:
        self._log_list = []
        self._LOG_INFO = "[INFO]"
        self._LOG_ERROR = "[ERROR]"

    def _log(self, log_type, message):
        timeNow = strftime("%H:%M:%S", gmtime())
        self._log_list.append(f"[{timeNow}]{log_type}: {message};")

        with open("log.txt", "a+", encoding="utf-8") as logfile:
            logfile.write(f"[{timeNow}]{log_type}: {message};\n")
            
        print(f"[{timeNow}]{log_type}: {message};")

    def log_info(self, message):
        self._log(self._LOG_INFO, message)

    def log_error(self, message):
        self._log(self._LOG_ERROR, message)