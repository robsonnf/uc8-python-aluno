# A18: assinaturas de apoio; traga sua implementação anterior.
from contextlib import closing
from pathlib import Path
import sqlite3

def validar_nome(nome):
    """TODO A18: implemente validar_nome conforme o contrato e reutilize seu código anterior."""
    raise NotImplementedError('Implemente e teste esta operação.')

def validar_id(codigo):
    """TODO A18: implemente validar_id conforme o contrato e reutilize seu código anterior."""
    raise NotImplementedError('Implemente e teste esta operação.')

def validar_preco(preco):
    """TODO A18: implemente validar_preco conforme o contrato e reutilize seu código anterior."""
    raise NotImplementedError('Implemente e teste esta operação.')

class RepositorioSqlite:

    def __init__(self, caminho):
        """TODO A18: implemente __init__ conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def conectar(self):
        """TODO A18: implemente conectar conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def iniciar(self):
        """TODO A18: implemente iniciar conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def adicionar_produto(self, nome, preco):
        """TODO A18: implemente adicionar_produto conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def listar_produtos(self):
        """TODO A18: implemente listar_produtos conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def adicionar_cliente(self, nome):
        """TODO A18: implemente adicionar_cliente conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def listar_clientes(self):
        """TODO A18: implemente listar_clientes conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def editar_produto(self, codigo, nome, preco):
        """TODO A18: implemente editar_produto conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def excluir_produto(self, codigo, confirmado=False):
        """TODO A18: implemente excluir_produto conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def editar_cliente(self, codigo, nome):
        """TODO A18: implemente editar_cliente conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def excluir_cliente(self, codigo, confirmado=False):
        """TODO A18: implemente excluir_cliente conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def iniciar_vendas(self):
        """TODO A18: implemente iniciar_vendas conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def registrar_venda(self, cliente_id, itens, forma):
        """TODO A18: implemente registrar_venda conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')

    def listar_vendas(self):
        """TODO A18: implemente listar_vendas conforme o contrato e reutilize seu código anterior."""
        raise NotImplementedError('Implemente e teste esta operação.')
