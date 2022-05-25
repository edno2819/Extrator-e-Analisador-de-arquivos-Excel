from Anality.handlerExcel import excelTemplate
from os import walk
import os


CONFIGS = {
    'CURRENT-PATH': os.path.abspath(os.getcwd()),
    'SO': 'LINUX',
    'SPLITER': '/',
    'PATH_ERRO': 'Erro',
    'PATH_SURE': 'OK',
}


class Compare:
    '''
        - Cada método representa uma Regra de análise
        - Cada método retorna uma lista com as strings da localização de cada erro
    '''

    def __init__(self, fileTemplate, fileAnalyzed) -> None:
        self.template = fileTemplate
        self.analyzed = fileAnalyzed

    def compareRaio(self):
        '''Se no arquivo baixado a coluna Q <> vazio E no arquivo baixado a 
        coluna I <> vazio E no arquivo baixado a coluna Q  = valoor da 
        coluna R - Raio  Então a variavel Erro recebe ErroRaio+1, e pinta no 
        arquivo que veio do sistema as celulas com erro na cor vermelha '''

    def compareKM(self):
        '''Se no arquivo baixado sistema a coluna I <> vazio E  a coluna 
        S <> 0 E a coluna S for diferente da variavel VALOR_KM Então marca as 
        celulas de vermelho e  fonte de branco, E a variavel ErrovalorKM recebe +1'''

    def compareInstalacao(self):
        '''Se no arquivo baixado a coluna/celula I <> vazio E na coluna/celula 
        N não CONTEM a palavra DESINSTA  E  a coluna/celula N o vao9r é difeente 
        do valor da variavel <> INSTALACAO então a variavel ErroInstalacao recebe mais 1'''

    def compareDesinstalacao(self):
        '''Se no arquivo baixado a coluna I <> vazio E na coluna N  CONTEM a palavra 
        DESINSTA    E  a coluna P o valor é diferente do valor da variavel <> 
        DESINSTALACAO então a variavel ErroDesinstalacao recebe mais 1'''

    def compareParque(self):
        '''Se a quanrtidade de linhas no arquivo baixado for diferente da variavel 
        QtEquipoParm(recebe valor da coluna H na guia PARAMETROS desse arquivo aqui, 
        então, a varivel Erro parque recebe + 1'''


class moduleAnality:
    PATH_ERRO = CONFIGS['PATH_ERRO']
    PATH_SURE = CONFIGS['PATH_SURE']

    def __init__(self, folderFiles, fileTemplate) -> None:
        self.folder = folderFiles
        self.fileTemplate = fileTemplate
        self.b = excelTemplate(self.fileTemplate)

    def getAllFiles(self):
        'obter um lista de todos os excels dentro da pasta'
        self.filenames = next(walk(self.folder), (None, None, []))[2]
        'checagem de tipo'

    def findRowTemplate(self, cod):
        '''retorna a localização da linha do arquivo template com o mesmo
        código ex: A2, A35'''
        return self.b.findCod(cod)

    def exeRules(self, comparator):
        erros = {}
        erros['raio'] = comparator.compareRaio()
        erros['km'] = comparator.compareKM()
        erros['instalacao'] = comparator.compareInstalacao()
        erros['desistalacao'] = comparator.compareDesinstalacao()
        erros['parque'] = comparator.compareParque()
        return erros

    def fillFile(self, erros, file):
        'Pinta todas as celulas do excel com erro de vermelho'

    def moveFile(self, file, newPath):
        'move files'

    def creatAlert(self):
        'Adicinar erros no arquivo de alerta'

    def hasError(self, file, erros):
        'realiza todos as atividades referentes a arquivos com erros'
        self.fillFile(erros, file)
        self.moveFile(file, self.PATH_ERRO)
        self.creatAlert(erros)

    def hasNotError(self, file):
        'realiza todos as atividades referentes a arquivos sem erros'
        self.moveFile(file, self.PATH_SURE)

    def CompareAll(self):
        self.getAllFiles()
        for file in self.filenames:
            file_path = self.folder + CONFIGS['SPLITER'] + file
            cod = '1092651'  # codigo do arquivo'
            row = self.findRowTemplate(cod)
            if row:
                comparator = Compare(row, file_path)
                errosFile = self.exeRules(comparator)
                if any(type(x) == list for x in errosFile.values()):
                    self.hasError(file, errosFile)
                else:
                    self.hasNotError(file)