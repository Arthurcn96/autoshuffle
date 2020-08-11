#
#   Programa que automaticamente altera os arquivos da
#   pasta de Download para as respectivas pastas de destino.
#   Autor: Arthur Novais
#


from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import time
import json
import os

class MyHandler(FileSystemEventHandler):
    #Caso ocorra modificacao
    def on_modified(self, event):
        #Para cada arquivo na pasta de origem
        for arquivo in os.listdir(pastaOrigem):
            #Salvo o caminho do arquivo
            src = pastaOrigem + "/" + arquivo
            #salva o tamanho do arquivo atual
            tamanhoArquivo = os.path.getsize(src)
            #Salvo o novo caminho do arquivo
            novoDestino = src;
            #Espera um segundo
            time.sleep(1)
            if os.path.isfile(src):
                #Enquanto o arquivo estiver mudando o valor(sendo baixado/transferido) espere

                while (tamanhoArquivo != os.path.getsize(src)):
                    #print ("O arquivo "+arquivo+" ainda está baixando")
                    tamanhoArquivo = os.path.getsize(src)
                    time.sleep(1)

                if arquivo.lower().endswith(('.png', '.jpg', '.jpeg')):
                    novoDestino = pastaImagem
                elif arquivo.lower().endswith('.deb'):
                    novoDestino = pastaDeb
                elif arquivo.lower().endswith('.pdf'):
                    novoDestino = pastaPdf
                elif arquivo.lower().endswith('.mp3'):
                    novoDestino = pastaMusica
                elif arquivo.lower().endswith(('.gz', '.tar', '.zip')):
                    novoDestino = pastaCompactado
                elif arquivo.lower().endswith(('.webm', '.mp4', '.avi', '.wmv', '.mov', 'flv')):
                    novoDestino = pastaVideo
                else:
                    novoDestino = pastaDocumento
                #Salvo o arquivo no novo caminho
                os.rename(src,novoDestino + "/" + arquivo)

#Pasta de origem
pastaOrigem = '/home/arthur/Downloads'
pastaImagem = '/home/arthur/Imagens'
pastaCompactado = '/home/arthur/Downloads/Compactado'
pastaPdf = '/home/arthur/Documentos/PDF'
pastaDocumento = '/home/arthur/Documentos'
pastaMusica = '/home/arthur/Música'
pastaVideo = '/home/arthur/Vídeos'
pastaDeb = '/home/arthur/Downloads/deb'

#Evento observando se tem alteração na pasta de Origem
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, pastaOrigem, recursive=True)
observer.start()

try:
    while True:
        #Tempo até a próxima verificação
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join
