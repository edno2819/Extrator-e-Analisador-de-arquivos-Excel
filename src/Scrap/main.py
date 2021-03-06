from Scrap.site_web import Site
from utils import set_folder
import pandas as pd
import shutil


class ModelScrap:
    def __init__(self, PATH) -> None:
        self.PATH = PATH

    def readExcel(self):
        self.df = pd.read_excel(self.PATH['LISTA DE CODIGOS'])
        self.codigos = self.df['CODIGOS'].values
        self.PATH = self.PATH['DOWNLOAD']

    def start(self):
        self.site = Site()
        self.site.open_page()
        for cod in self.codigos:
            cod = str(cod)
            name = self.site.pross(cod)
            if name:
                path = self.PATH + name
                self.set_enviroment(name)
                self.moveFolder()
                print(f'Salvo: {name}')
        self.site.close()
        
    def save(self, itens_data):
        self.to_excel.write(itens_data, self.path_scraps)

    def moveFolder(self, path_file, new_path):
        shutil.move(path_file, new_path)

    def set_enviroment(self, path):
        set_folder(path)

    def run(self):
        self.site = Site()
        name = self.site.teste()
        path = f"{self.PATH}{self.PATH['SPLITER']}{name.split('.')[0]}"
        self.set_enviroment(path)
        self.moveFolder(
            self.PATH + self.PATH['SPLITER'] + name, path + self.PATH['SPLITER'] + name)
        self.site.close()
