class SingletonLazy:
    __instance = None
    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = SingletonLazy()
        return cls.__instance
    # Um \@classmethod é um método que recebe a classe como primeiro argumento
    # em vez da instância. Isso significa que você pode acessar atributos e 
    # métodos de nível de classe a partir deste método. Um uso comum de 
    # \@classmethod é para definir construtores alternativos ou implementar
    # método que gerencia instancias de classe.

    # Neste exemplo, get\_instance é um método de classe que nos permite pegar
    # uma instância da classe por meio do atributo \_\_instance. 
    # O argumento cls refere-se a própria classe SingletonLazy, não a uma instância. Isso é útil porque se criarmos uma classe SingletonLazy, o método get\_instance consulta automaticamente se há uma instância da classe, e não apenas um objeto SingletonLazy.


