import win32print

printers = win32print.EnumPrinters(2)
for i in printers: print(f'{printers.index(i)}: ' + str(i[1]))