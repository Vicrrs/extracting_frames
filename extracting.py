import cv2


def extracting(video_path, output_path):
    # Abrindo o video
    video = cv2.VideoCapture(video_path)

    # Verificar se vídeo foi aberto corretamente
    if not video.isOpened():
        print("Erro ao abrir o video")
        return

    # Inicializando variavel
    frame_count = 0

    while True:
        # Lendo proximo frame do video
        ret, frame = video.read()

        # verificar se o frame  foi lido corretamente
        if not ret:
            break

        # Salvar o frame como uma imagem
        frame_filname = f"{output_path}/frame_{frame_count}.jpg"
        cv2.imwrite(frame_filname, frame)

        # Mostrar o numero de frame na saida padrao
        print(f"Salvando frame {frame_count}")

        # Incrementar o contador de frames
        frame_count += 1

    # Liberar o video e fechar as janelas
    video.release()
    cv2.destroyAllWindows()


# Exemplo de uso
video_path = "caminho/do/video.mp4"  # Substitua pelo caminho do seu vídeo
output_path = "caminho/do/diretorio/de/saida"  # Substitua pelo caminho do diretório de saída
extracting(video_path, output_path)
