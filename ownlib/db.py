class db:
    import shelve
    def __init__(self,plik):
        self.plik=plik
    def __enter__(self):
        self.dbas = shelve.open(self.plik)
        return self
    def write(self,row,stac,utim):
        d[(utim,stac)] = row
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.dbas.close()
        print exc_type,exc_val,exc_tb
