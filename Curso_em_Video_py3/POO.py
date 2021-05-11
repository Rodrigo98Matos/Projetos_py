class Computador():
    def __init__( self ):
        self.marca = 'Dell'
        self.processador = 'Bosta'
        self.usb = 3
        self.ligado = False
    
    def ligar_computador( self ):
        self.ligado = True

    def set_marca( self, marca ):
        self.marca = marca

    def get_marca( self ):
        return self.marca
    
class Notebook( Computador ):
    pass


meu_notebook = Notebook()
print(meu_notebook.marca)
