from Anality.handlerExcel import *
from os import walk
import os
import shutil


class Compare:
    """
    - Cada método representa uma Regra de análise
    - Cada método retorna uma lista com as strings da localização de cada erro
    """

    'se não tiver ordem de serviço desconsidera a linha'

    SHEET_NAME_ANALIZED = 'Atendimento'
    SHEET_NAME_TEMPLATE = 'PARAMETROS'
    VALUES_FALSE = [0, '', None]

    def __init__(self, fileTemplate, row_template, fileAnalyzed) -> None:
        self.row_template = row_template
        self.template = fileTemplate
        self.analyzed = fileAnalyzed
        self.row_init = 6
        self.status = 'OK'

    def compareRaio(self):
        """Se no arquivo baixado a coluna Q <> vazio E no arquivo baixado a
        coluna I <> vazio E no arquivo baixado a (coluna Q  =  R - Raio  Então a variavel) 
        Erro recebe ErroRaio+1, e pinta no arquivo que veio do sistema as celulas com erro 
        na cor vermelha"""

        erros = {'celulas': [], 'qtd_error': 0}

        colum_Q = [
            cel.value for cel in self.analyzed.wb[self.SHEET_NAME_ANALIZED]['Q']]
        colum_I = [
            cel.value for cel in self.analyzed.wb[self.SHEET_NAME_ANALIZED]['I']]
        colum_R = [
            cel.value for cel in self.analyzed.wb[self.SHEET_NAME_ANALIZED]['R']]
        raio = self.template.wb[self.SHEET_NAME_TEMPLATE][f'C{self.row_template}'].value

        for row_n in range(self.row_init, len(colum_Q)):
            if colum_Q[row_n] not in self.VALUES_FALSE and colum_I[row_n] not in self.VALUES_FALSE and colum_Q[row_n] == colum_R[row_n]-raio:
                erros['qtd_error'] += 1
                erros['celulas'].append(f'Q{row_n+1}')
                self.status = 'ERROR'

        return erros

    def compareKM(self):
        """Se no arquivo baixado sistema a coluna I <> vazio E  a coluna
        S <> 0 E a coluna S for diferente da variavel VALOR_KM Então marca as
        celulas de vermelho e  fonte de branco, E a variavel ErrovalorKM recebe +1
        caso der erro pinte a culuna S"""

        erros = {'celulas': [], 'qtd_error': 0}

        colum_S = [
            cel.value for cel in self.analyzed.wb[self.SHEET_NAME_ANALIZED]['S']]
        colum_I = [
            cel.value for cel in self.analyzed.wb[self.SHEET_NAME_ANALIZED]['I']]
        template_km = self.template.wb[self.SHEET_NAME_TEMPLATE][f'E{self.row_template}'].value

        for row_n in range(self.row_init, len(colum_S)):
            if colum_I[row_n] not in self.VALUES_FALSE and colum_S[row_n] not in self.VALUES_FALSE and colum_S[row_n] != template_km:
                erros['qtd_error'] += 1
                erros['celulas'].append(f'S{row_n+1}')
                self.status = 'ERROR'

        return erros

    def compareInstalacao(self):
        """Se no arquivo baixado a celula I <> vazio E (na celula
        N não CONTEM a palavra 'DESINS')  E  (Na celula P <> INSTALACAO) 
        então a variavel ErroInstalacao recebe mais 1, PINTA N e P"""

        erros = {'celulas': [], 'qtd_error': 0}

        colum_N = [
            cel.value for cel in self.analyzed.wb[self.SHEET_NAME_ANALIZED]['N']]
        colum_I = [
            cel.value for cel in self.analyzed.wb[self.SHEET_NAME_ANALIZED]['I']]
        colum_P = [
            cel.value for cel in self.analyzed.wb[self.SHEET_NAME_ANALIZED]['P']]

        for row_n in range(self.row_init, len(colum_N)):
            if colum_I[row_n] not in self.VALUES_FALSE and 'DESINS' not in colum_N[row_n] and colum_P[row_n] != 'INSTALACAO':
                erros['qtd_error'] += 1
                erros['celulas'].append(f'N{row_n+1}')
                erros['celulas'].append(f'P{row_n+1}')
                self.status = 'ERROR'

        return erros

    def compareDesinstalacao(self):
        """Se no arquivo baixado a (coluna I <> vazio) E na (coluna N  CONTEM a palavra
        'DESINS')    E  a (coluna P <> DESINSTALACAO) então a variavel ErroDesinstalacao 
        recebe mais 1, PINTAR P e N"""

        erros = {'celulas': [], 'qtd_error': 0}

        colum_N = [
            cel.value for cel in self.analyzed.wb[self.SHEET_NAME_ANALIZED]['N']]
        colum_I = [
            cel.value for cel in self.analyzed.wb[self.SHEET_NAME_ANALIZED]['I']]
        colum_P = [
            cel.value for cel in self.analyzed.wb[self.SHEET_NAME_ANALIZED]['P']]

        for row_n in range(self.row_init, len(colum_N)):
            if colum_I[row_n] not in self.VALUES_FALSE and 'DESINS' not in colum_N[row_n] and colum_P[row_n] != 'DESINSTALACAO':
                erros['qtd_error'] += 1
                erros['celulas'].append(f'N{row_n+1}')
                erros['celulas'].append(f'P{row_n+1}')
                self.status = 'ERROR'

        return erros

    def compareParque(self):
        """Se a quanrtidade de linhas na aba 'Equipamentos' for diferente
        da do valor na coluna 'POR EQUIPAMENTOS' da erro, então, a varivel 
        Erro parque recebe + 1, PINTAR SINTÉTICOS[C8]"""

        erros = {'celulas': [], 'qtd_error': 0}

        qtd_equipamentos = self.analyzed.wb['Sintético']['C8'].value
        qtd_equipamentos_template = self.template.wb[
            self.SHEET_NAME_TEMPLATE][f'H{self.row_template}'].value

        if qtd_equipamentos != qtd_equipamentos_template:
            erros['qtd_error'] += 1
            erros['celulas'].append(f'C8')
            self.status = 'ERROR'

        return erros


class moduleAnality:
    def __init__(self, PATHS) -> None:
        self.PATHS = PATHS
        self.file_template_path = PATHS['TEMPLATES']
        self.folder = PATHS['DOWNLOAD']
        self.fileTemplate = excelTemplate(PATHS['TEMPLATES'])
        self.PATH_ERRO = PATHS['PATH_ERRO']
        self.PATH_SURE = PATHS['PATH_SURE']

    def getAllFiles(self):
        """obter um lista de todos os excels dentro da pasta"""
        self.filenames = next(walk(self.folder), (None, None, []))[2]
        'checagem de tipo'

    def findRowTemplate(self):
        """retorna a localização da linha do arquivo template com o mesmo
        código ex: A2, A35"""
        return self.fileTemplate.findCod(self.cod)

    def exeRules(self, comparator):
        erros = {}
        erros['ErroRaio'] = comparator.compareRaio()
        erros['ErrovalorKM'] = comparator.compareKM()
        erros['instalacao'] = comparator.compareInstalacao()
        erros['desistalacao'] = comparator.compareDesinstalacao()
        erros['parque'] = comparator.compareParque()
        return erros

    def fillFile(self, file_to_anality_path, file_obj,  erros):
        """Pinta todas as celulas do excel com erro de vermelho"""
        file_obj.fill('Atendimento', erros['ErroRaio']['celulas'])
        file_obj.fill('Atendimento', erros['ErrovalorKM']['celulas'])
        file_obj.fill('Atendimento', erros['instalacao']['celulas'])
        file_obj.fill('Atendimento', erros['desistalacao']['celulas'])
        file_obj.fill('Sintético', erros['parque']['celulas'])
        file_obj.salve(file_to_anality_path)

    def moveFile(self, file_to_anality_path, new_folder):
        shutil.move(file_to_anality_path,
                    f'{new_folder}{self.PATHS["SPLITER"]}{self.file}')

    def creatAlert(self, erros):
        """Adicinar erros no arquivo de alerta"""
        infos = {
            'COD': self.cod,
            'ARQUIVO': self.file,
            'RAIO': erros['ErroRaio']['qtd_error'],
            'VALOR_KM': erros['ErrovalorKM']['qtd_error'],
            'INSTALACAO': erros['instalacao']['qtd_error'],
            'DESINSTALACAO': erros['desistalacao']['qtd_error'],
            'POR_EQUIPAMENTO': erros['parque']['qtd_error'],
            'TOTAL_ERROS': (erros['ErroRaio']['qtd_error'] +
                            erros['ErrovalorKM']['qtd_error'] +
                            erros['instalacao']['qtd_error'] +
                            erros['desistalacao']['qtd_error'] +
                            erros['parque']['qtd_error'])
        }

        self.fileTemplate.creat_alert(infos)
        self.fileTemplate.salve(self.file_template_path)

    def hasError(self, file_to_anality_path, file_obj,  erros):
        """realiza todos as atividades referentes a arquivos com erros"""
        self.fillFile(file_to_anality_path, file_obj,  erros)
        self.moveFile(file_to_anality_path, self.PATH_ERRO)
        self.creatAlert(erros)

    def hasNotError(self, file_to_anality_path):
        """realiza todos as atividades referentes a arquivos sem erros"""
        self.moveFile(file_to_anality_path, self.PATH_SURE)

    def findCodInFileName(self):
        return self.file.split('_')[3]

    def CompareAll(self):
        self.getAllFiles()
        for file in self.filenames:
            self.file = file
            file_to_anality_path = self.folder + self.PATHS["SPLITER"] + file
            file_to_anality = excelToAnalyze(file_to_anality_path)
            self.cod = self.findCodInFileName()
            row_location = self.findRowTemplate()
            if row_location:
                comparator = Compare(
                    self.fileTemplate, row_location, file_to_anality)
                errosFile = self.exeRules(comparator)
                if comparator.status == 'ERROR':
                    self.hasError(file_to_anality_path,
                                  file_to_anality, errosFile)
                else:
                    self.hasNotError(file_to_anality_path)
