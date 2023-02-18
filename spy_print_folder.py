import os
from time import sleep
import win32print
import win32api

class PyPrinter:
    def __init__(self, num):
        self.num = num
        self.printer_name = win32print.EnumPrinters(2)[num][2]
        self.arq_suport = ['.pdf']
   
    def new_print(self, path, arqs):
        win32print.SetDefaultPrinter(self.printer_name)

        for arq in arqs:
            try:
                printed = False
                for i in self.arq_suport:
                    if i in arq:
                        win32api.ShellExecute(0, "print", arq, None, path, 0)
                        print(f'Arq printed: {path+arq} - {self.printer_name}\n')
                        printed = True

                if not printed:
                    print('Unsupported file type')
                    print(f'Try printing in these formats: {self.arq_suport}\n')
            
            except:
                print(f'Printing error: {path+arq} - {self.printer_name}\n')

class PathLookOut:
    def __init__(self, live_path):
        self.live_path = live_path

        self.folder_before = os.listdir(self.live_path)
        self.folder_after = self.folder_before[:]
    
    def look(self, time_delay=1):
        self.folder_after = os.listdir(self.live_path)

        len_fb, len_fa = len(self.folder_before), len(self.folder_after)

        if len_fb > len_fa:
            self.folder_before = self.folder_after[:]
            print('Arq removed')
        elif len_fb < len_fa:
            new_arqs = []
            for i in self.folder_after:
                if not i in self.folder_before: new_arqs.append(i)

            self.folder_before = self.folder_after[:]

            print(f'New arq: {new_arqs}')
            return new_arqs
    
        sleep(time_delay)

def main():
    #------------------------------------------------
    spy_folder = r'C:\Users\Admin\Meu Drive (crucilandiapmmg@gmail.com)\imprimir'
    printer_num = 2
    #------------------------------------------------

    print('### Spy Print Folder RUNNING ###\n')
    print(f'Path spy setted: {spy_folder}')
    print(f'Printer setted: {printer_num}\n')

    path_lookout = PathLookOut(spy_folder)
    printer = PyPrinter(printer_num)

    running = True
    while running:
        resp = path_lookout.look(time_delay=0.5)

        if resp:
            printer.new_print(spy_folder, resp)

if __name__ == '__main__':
    main()
