from src import DocumentoFactoryMethodConcreta

# Cliente usando a Factory Method
def codigo_cliente_factory_method2(tipo_documento: str):

    if(tipo_documento == "word" or tipo_documento == "pdf"):

        documento = DocumentoFactoryMethodConcreta(tipo_documento)

        print(documento.abrir())

    else:

        print("Tipo de documento desconhecido")
