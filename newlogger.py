from time import gmtime, strftime


class Logger():

    def __init__(self, write_to_logfile:bool=False) -> None:
        self.write_to_logfile = write_to_logfile

    def __log(self, message):
        logstring = f"[{strftime("%H:%M:%S", gmtime())}]: {message}"
        print(logstring)

        if self.write_to_logfile:
            with open("log.log", "a+", encoding="utf-8") as logfile:
                logfile.write(logstring+"\n")

    def setlog(self, message):
        self.__log(message)