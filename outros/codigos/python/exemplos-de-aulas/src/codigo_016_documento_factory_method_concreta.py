from src import DocumentoMsWordConcreta, DocumentoPdfConcreta

class DocumentoFactoryMethodConcreta:

    def __init__(self, tipo_documento: str):
        if tipo_documento == "word":
            self.document = DocumentoMsWordConcreta()
        elif tipo_documento == "pdf":
            self.document = DocumentoPdfConcreta()

    def abrir(self):
        return self.document.abrir()