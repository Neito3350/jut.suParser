from time import gmtime, strftime


class Logger():

    def __init__(self, write_to_logfile:bool=False, no_print:bool=False) -> None:
        self.write_to_logfile = write_to_logfile
        self.no_print = no_print

    def __log(self, message):
        logstring = f"[{strftime("%H:%M:%S", gmtime())}]: {message}"
        
        if not self.no_print:
            print(logstring)

        if self.write_to_logfile:
            with open("log.log", "a+", encoding="utf-8") as logfile:
                logfile.write(logstring+"\n")

    def setlog(self, message):
        self.__log(message)