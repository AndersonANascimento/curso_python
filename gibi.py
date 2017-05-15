# -*- coding: UTF-8 -*-
# Módulo de Data Science - 15/05/2017

class Gibi(object):
    def __init__(self, id=None, numero=None, titulo=None, personagem=None, editora=None):
        self.id = id
        self.numero = numero
        self.titulo = titulo
        self.personagem = personagem
        self.editora = editora

    def __str__(self):
        return self.titulo + ' - ' + self.personagem + ' - ' + self.editora

    def __repr__(self):
        return "Gibi(id=%s, numero=%s, titulo=%s, personagem=%s, editora=%s)" % \
               (self.id, self.numero, self.titulo, self.personagem, self.editora)

    @classmethod
    def carregar(cls, arq):
        """Função para carga de lista de GIBIS
            Args:
                nome_arquivo (str): Nome do arquivo a ser carregado.
            Returns: 
                list: Lista contendo Gibis.
        """
        lista = []
        arquivo = None
        try:
            print 'Carregando arquivo...'
            arquivo = open(arq, 'r')
            print 'Arquivo carregado'
            for linha in arquivo:
                atributos = linha.strip().split(';')
                lista.append(cls(*atributos))
            print 'Fechando arquivo...'
            arquivo.close()
            print 'Arquivo fechado'
            lista.pop(0)
        except IOError as error:
            print "Capim na palhetaaa - %s" % error
        except TypeError as error:
            print "Falha no nro de atributos %s" % error
        finally:
            if (not arquivo.closed):
                print 'Fechando arquivo...'
                arquivo.close()
                print 'Arquivo fechado'
        return lista

class GibiAmericano(Gibi):
    def __init__(self, id=None, numero=None, titulo=None, personagem=None, editora=None, tipo_capa=None):
        super(GibiAmericano, self).__init__(id, numero, titulo, personagem, editora)
        self.tipo_capa = tipo_capa

    def __repr__(self):
        return "GibiAmericano(id=%s, numero=%s, titulo=%s, personagem=%s, editora=%s, tipo_capa=%s)" % \
               (self.id, self.numero, self.titulo, self.personagem, self.editora, self.tipo_capa)
