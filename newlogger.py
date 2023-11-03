from time import gmtime, strftime


class Logger():

    def __init__(self, write_to_logfile:bool=False) -> None:
        self.write_to_logfile = write_to_logfile
        self.logtype_info = "[INFO]"
        self.logtype_error = "[ERROR]"
        # self.logtype_warning = "[WARNING]"

    def __log(self, logtype, message):
        logstring = f"[{strftime("%H:%M:%S", gmtime())}]{logtype}: {message}"
        print(logstring)

        if self.write_to_logfile:
            with open("log.log", "a+", encoding="utf-8") as logfile:
                logfile.write(logstring+"\n")

    def info(self, message):
        self.__log(self.logtype_info, message)

    def error(self, message):
        self.__log(self.logtype_error, message)