import sys
import os
from pathlib import Path

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Print para verificação
# print("Caminho configurado no sys.path:", sys.path)
