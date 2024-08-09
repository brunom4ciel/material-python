def obtem_nome_arquivo(caminho_arquivo: str) -> str:
    """
    Retorna o nome do arquivo a partir do caminho do arquivo.
    """
    try:
        return caminho_arquivo.split('/')[-1]
    except Exception as error:
        raise ValueError(error)
    
def obtem_extensao_arquivo(caminho_arquivo: str) -> str:
    """
    Retorna a extensão do arquivo a partir do caminho do arquivo.
    """
    try:
        return caminho_arquivo.split('.')[-1]
    except Exception as error:
        raise ValueError(error)
    
def obtem_nome_arquivo_sem_extensao(caminho_arquivo: str) -> str:
    """
    Retorna o nome do arquivo sem a extensão a partir do caminho do arquivo.
    """
    try:
        return caminho_arquivo.split('/')[-1].split('.')[0]
    except Exception as error:
        raise ValueError(error)
    
def obtem_caminho_arquivo(caminho_arquivo: str) -> str:
    """
    Retorna o caminho do arquivo a partir do caminho do arquivo.
    """
    try:
        return "/".join(caminho_arquivo.split('/')[:-1])
    except Exception as error:
        raise ValueError(error)
    
caminho_arquivo = '/home/usuario/Downloads/arquivo.txt'

nome_arquivo = obtem_nome_arquivo(caminho_arquivo)
extensao_arquivo = obtem_extensao_arquivo(caminho_arquivo)
nome_arquivo_sem_extensao = obtem_nome_arquivo_sem_extensao(caminho_arquivo)
caminho_arquivo = obtem_caminho_arquivo(caminho_arquivo)

print(nome_arquivo, extensao_arquivo, nome_arquivo_sem_extensao, caminho_arquivo)
