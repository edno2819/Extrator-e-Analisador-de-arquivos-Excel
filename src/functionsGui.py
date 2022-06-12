from Scrap.main import ModelScrap
from Anality.main import moduleAnality
import os

CONFIGS = {
    'SO': 'LINUX',
}
CONFIGS['SPLITER'] = '\\'  if CONFIGS['SO']=='WINDOWS'else '/'
CONFIGS['CURRENT-PATH'] =  os.path.abspath(os.getcwd())+f'{CONFIGS["SPLITER"]}src',


PATHS = {
    'LISTA DE CODIGOS': f'{CONFIGS["CURRENT-PATH"]}{CONFIGS["SPLITER"]}fileTemplate{CONFIGS["SPLITER"]}LISTA_REVENDAS.xlsx',
    'DOWNLOAD': f'{CONFIGS["CURRENT-PATH"]}{CONFIGS["SPLITER"]}download',
    'TEMPLATES': f'{CONFIGS["CURRENT-PATH"]}{CONFIGS["SPLITER"]}fileTemplate{CONFIGS["SPLITER"]}template.xlsm',
    'PATH_ERRO': f'{CONFIGS["CURRENT-PATH"]}{CONFIGS["SPLITER"]}Erro',
    'PATH_SURE': f'{CONFIGS["CURRENT-PATH"]}{CONFIGS["SPLITER"]}OK',
}

PATHS.update(CONFIGS)



class ExecuteGui:
    PATH = 'Scraps'

    def button1():
        scrapFiles = ModelScrap(PATHS)
        scrapFiles.readExcel()
        scrapFiles.start()

    def button2():
        analy = moduleAnality(PATHS)
        analy.CompareAll()

    def button3():
        scrapFiles = ModelScrap()
        scrapFiles.readExcel()
        scrapFiles.start()


if __name__ == '__main__':
    ExecuteGui.button1()
