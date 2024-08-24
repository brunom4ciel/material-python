from src import DocumentoAbstrata

class DocumentoPdfConcreta(DocumentoAbstrata):
    def abrir(self):
        return "Abrindo um documento PDF"