import os
from time import sleep
import win32print
import win32api

class PyPrinter:
    def __init__(self, num):
        self.num = num
        
        printers = win32print.EnumPrinters(2)
        self.printer_name = printers[self.num][2]
    
    def new_print(self, path, arqs):
        win32print.SetDefaultPrinter(self.printer_name)

        for arq in arqs:
            win32api.ShellExecute(0, "print", arq, None, path, 0)


class PathLookOut:
    def __init__(self, live_path):
        self.live_path = live_path

        self.folder_before = os.listdir(self.live_path)
        self.folder_after = self.folder_before[:]
    
    def look(self, time_delay=1):
        self.folder_after = os.listdir(self.live_path)

        len_fb = len(self.folder_before)
        len_fa = len(self.folder_after)

        if len_fb > len_fa:
            self.folder_before = self.folder_after
            print('Arq removed')
        elif len_fb < len_fa:
            news_arqs = []
            for i in self.folder_after:
                if not i in self.folder_before: news_arqs.append(i)
            self.folder_before = self.folder_after

            print('New arq')
            
            return news_arqs
    
        sleep(time_delay)
            

def main():
    #------------------------------------------------
    spy_folder = r'/home/alex0001/Downloads/pasta01'
    printer_num = 0
    #------------------------------------------------

    path_lookout = PathLookOut(spy_folder)
    printer = PyPrinter(printer_num)

    while True:
        resp = path_lookout.look()

        if resp:
            printer.new_print(path_lookout, resp)

if __name__ == '__main__':
    main()
