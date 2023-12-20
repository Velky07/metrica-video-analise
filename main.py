import os
import psutil
import time
from moviepy.editor import VideoFileClip

def converter_video(arquivo_entrada, arquivo_saida, formato):
    tempo_inicio = time.time()
    clip = VideoFileClip(arquivo_entrada)
    
    if formato == 'mp4':
        clip.write_videofile(arquivo_saida + '.mp4', codec='libx264')
    elif formato == 'avi':
        clip.write_videofile(arquivo_saida + '.avi', codec='rawvideo')
    elif formato == 'mov':
        clip.write_videofile(arquivo_saida + '.mov', codec='libx264')
    
    clip.close()
    tempo_fim = time.time()

    return tempo_fim - tempo_inicio

def main():
    arquivo_entrada = 'videos/2 mim - 360p - A.mov'
    arquivo_saida = 'videos\\outputs\\'

    escolha_formato = input("Escolha o formato de saída (mp4, avi, mov): ")

    tempo_formato = converter_video(arquivo_entrada, arquivo_saida, escolha_formato)

    print(f"Tempo de conversão para {escolha_formato.upper()}: {tempo_formato} segundos")

    # Monitorando o uso de memória
    processo = psutil.Process()
    uso_memoria = processo.memory_info().rss / (1024 * 1024)  # Em MB
    print("Consumo de memória:", uso_memoria, "MB")

    # Verificando o tamanho do arquivo resultante
    tamanho_arquivo = os.path.getsize(arquivo_saida + '.' + escolha_formato) / (1024 * 1024 * 1024)  # Em GB
    print(f"Tamanho do arquivo {escolha_formato.upper()}: {tamanho_arquivo} GB")

if __name__ == "__main__":
    main()

