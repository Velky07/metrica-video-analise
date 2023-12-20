import os
import psutil
import time
from moviepy.editor import VideoFileClip

def convert_video(input_file, output_file, format):
    start_time = time.time()
    clip = VideoFileClip(input_file)
    
    if format == 'mp4':
        clip.write_videofile(output_file + '.mp4', codec='libx264')
    elif format == 'avi':
        clip.write_videofile(output_file + '.avi', codec='rawvideo')
    elif format == 'mov':
        clip.write_videofile(output_file + '.mov', codec='libx264')
    
    clip.close()
    end_time = time.time()

    return end_time - start_time

def main():
    input_file = 'Videos\Copias\Alta - 2 min.wmv'
    output_file = 'Videos\\Outputs\\'

    format_choice = input("Escolha o formato de saída (mp4, avi, mov): ")

    time_format = convert_video(input_file, output_file, format_choice)

    print(f"Tempo de conversão para {format_choice.upper()}: {time_format} segundos")

    # Monitorando o uso de memória
    process = psutil.Process()
    memory_usage = process.memory_info().rss / (1024 * 1024)  # Em MB
    print("Consumo de memória:", memory_usage, "MB")

    # Verificando o tamanho do arquivo resultante
    file_size = os.path.getsize(output_file + '.' + format_choice) / (1024 * 1024 * 1024)  # Em GB
    print(f"Tamanho do arquivo {format_choice.upper()}: {file_size} GB")

if __name__ == "__main__":
    main()
