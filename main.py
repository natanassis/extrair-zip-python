from zipfile import ZipFile
import shutil
import os
from pathlib import Path

class ExtractZip:
    def __init__(self):
        self.path_inserido = f"{Path(os.getcwd())/ 'output'}"
        self.path_destino = f"{Path(os.getcwd())/ 'extraidos'}"
        
    def extract(self):
        arquivos = os.listdir(self.path_inserido)
        for zip in arquivos:
            caminho_relativo = os.path.join(self.path_inserido, zip)
            if os.path.exists(caminho_relativo):
                
                with ZipFile(caminho_relativo, 'r') as zip_object:
                    
                    zip_object.extractall(self.path_destino)

                name = zip_object.namelist()
                

if __name__ == "__main__":
    
    extrair = ExtractZip()
    
    extrair.extract()