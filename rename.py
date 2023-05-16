import os

def rename_images(folder_path):
    # Verifica se o caminho é um diretório
    if not os.path.isdir(folder_path):
        print(f'O caminho "{folder_path}" não é um diretório válido.')
        return
    
    # Lista todos os arquivos no diretório
    files = os.listdir(folder_path)
    
    # Filtra apenas os arquivos de imagem
    image_files = [file for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    
    # Ordena os arquivos de imagem em ordem alfabética
    image_files.sort()
    
    # Define um contador inicial
    count = 1
    
    # Renomeia cada arquivo de imagem
    for file in image_files:
        # Obtém o caminho completo do arquivo antigo
        old_path = os.path.join(folder_path, file)
        
        # Extrai a extensão do arquivo
        file_extension = os.path.splitext(file)[1]
        
        # Cria o novo nome de arquivo
        new_filename = f'image{count}{file_extension}'
        
        # Obtém o caminho completo do novo arquivo
        new_path = os.path.join(folder_path, new_filename)
        
        # Renomeia o arquivo
        os.rename(old_path, new_path)
        
        # Incrementa o contador
        count += 1

# Exemplo de uso
folder_path = '/home/victorroza/PycharmProjects/extracting_frames/Frames'
rename_images(folder_path)
