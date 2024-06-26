import os
import shutil
import zipfile
from datetime import datetime
import json

def compactar_pasta(pasta_origem, nome_arquivo_zip):
    with zipfile.ZipFile(nome_arquivo_zip, "w") as zip_ref:
        for raiz, _, arquivos in os.walk(pasta_origem):
            for arquivo in arquivos:
                caminho_completo = os.path.join(raiz, arquivo)
                zip_ref.write(caminho_completo, os.path.relpath(caminho_completo, pasta_origem))

def compactar_arquivo(origem_arquivo, nome_arquivo_zip):
    with zipfile.ZipFile(nome_arquivo_zip, "w") as zip_ref:
        zip_ref.write(origem_arquivo, os.path.basename(origem_arquivo))

def mover_arquivo(origem, destino):
    if not os.path.exists(destino):
        os.makedirs(destino)
    shutil.move(origem, os.path.join(destino, os.path.basename(origem)))

def main():
    ano_atual = datetime.now().year
    mes_atual = datetime.now().strftime("%m")

    with open("config.json") as f:
        config = json.load(f)

    sub_nome = config["sub_nome"]
    nome_pasta_destino = config["destino"]
    
    for arquivo_info in config["arquivos"]:
        pasta_origem = arquivo_info["pasta"]
        arquivo_origem = arquivo_info["arquivo"]

        print(pasta_origem)
        
        if arquivo_origem:
            nome_arquivo_zip = f"{datetime.now().strftime('%Y%m%d')}_{sub_nome}_{os.path.splitext(arquivo_origem)[0]}.zip"
            # nome_arquivo_zip = os.path.splitext(arquivo_origem)[0] + ".zip"
            arquivo_origem = os.path.join(pasta_origem, arquivo_origem)
            compactar_arquivo(arquivo_origem, nome_arquivo_zip)
        else:
            nome_arquivo_zip = f"{datetime.now().strftime('%Y%m%d')}_{sub_nome}_{os.path.basename(pasta_origem)}.zip"
            # nome_arquivo_zip = os.path.basename(pasta_origem) + ".zip"
            compactar_pasta(pasta_origem, nome_arquivo_zip)

        pasta_destino = os.path.join(nome_pasta_destino, fr"{ano_atual}\MES{mes_atual}")
        mover_arquivo(nome_arquivo_zip, pasta_destino)

if __name__ == "__main__":
    main()