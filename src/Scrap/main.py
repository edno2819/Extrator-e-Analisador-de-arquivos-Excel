from Scrap.site_web import Site
from utils import set_folder
import pandas as pd
import pathlib
import shutil


class ModelScrap:
    PATH = pathlib.Path().resolve().__str__()+'/download'

    
    def readExcel(self, path):
        try:
            self.df = pd.read_excel(path)
            self.codigos = self.df['CODIGOS'].value_counts
            return True
        except:
            print('Arquivo ou Coluna "CODIGOS" não encontrados!')
            return False
    

    def start(self, date):
        self.site = Site()
        self.site.open_page()
        for cod in self.codigos:
            name = self.site.pross(cod)
            if name:
                path = self.PATH + name
                self.set_enviroment(name)
                self.moveFolder()
                print(f'Salvo: {name}')
        self.site.close()
        print('\nConcluido com sucesso!\n')


    def save(self, itens_data):
        self.to_excel.write(itens_data, self.path_scraps)
    
    def moveFolder(self, path_file, new_path):
        shutil.move(path_file, new_path)

    def set_enviroment(self, path):
        set_folder(path)
    
    def teste(self):
        self.site = Site()
        name = self.site.teste()
        path = f"{self.PATH}/{name.split('.')[0]}"
        self.set_enviroment(path)
        self.moveFolder(self.PATH+'/'+name, path+'/'+name)
        self.site.close()
        print('\nConcluido com sucesso!\n')


if __name__ == '__main__':
    a = ModelScrap()
    a.readExcel('LISTA_REVENDAS.xlsx')
    a.teste()
    a.start(['1092651'])
    a