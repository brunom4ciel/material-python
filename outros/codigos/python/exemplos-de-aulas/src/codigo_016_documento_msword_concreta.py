from src import DocumentoAbstrata

class DocumentoMsWordConcreta(DocumentoAbstrata):
    def abrir(self):
        return "Abrindo um documento Microsoft Word"