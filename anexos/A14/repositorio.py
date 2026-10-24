# A14: assinaturas de apoio; traga sua implementação anterior.
from contextlib import closing
from pathlib import Path
import sqlite3

def validar_nome(nome):
    """TODO A14: implemente validar_nome conforme o contrato e reutilize seu código anterior."""
    raise NotImplementedError('Implemente e teste esta operação.')

def validar_id(codigo):
    """TODO A14: implemente validar_id conforme o contrato e reutilize seu código anterior."""
    raise NotImplementedError('Implemente e teste esta operação.')

def validar_preco(preco):
    """TODO A14: implemente validar_preco conforme o contrato e reutilize seu código anterior."""
    raise NotImplementedError('Implemente e teste esta operação.')

class RepositorioSqlite:

    def __init__(self, caminho):
        """TODO A14: implemente __init__ conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def conectar(self):
        """TODO A14: implemente conectar conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def iniciar(self):
        """TODO A14: implemente iniciar conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def adicionar_produto(self, nome, preco):
        """TODO A14: implemente adicionar_produto conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def listar_produtos(self):
        """TODO A14: implemente listar_produtos conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def adicionar_cliente(self, nome):
        """TODO A14: implemente adicionar_cliente conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def listar_clientes(self):
        """TODO A14: implemente listar_clientes conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')
