# from Scrap.main import ModelScrap
from Anality.main import moduleAnality


class ExecuteGui:
    PATH = 'Scraps'

    def button2():
        a = moduleAnality('/home/edno/Desktop/jobs/SrapRaphael/download',
                          '/home/edno/Desktop/jobs/SrapRaphael/filesTest/PARÂMETRO COM INSTRUÇÕES.xlsm')
        a.CompareAll()


if __name__ == '__main__':
    ExecuteGui.button2()
