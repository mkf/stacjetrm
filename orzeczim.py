class orzeczim:
    "To jest klasa orzeczenia imiennego, w trybach u i l"
    
    def __init__(self,row,stac,tryb,dz,cz):
        self.row = row
        self.stac = stac
        self.tryb = tryb
        self.dz = dz
        self.cz = cz

    def orz(self):
        if row == 0:
            self.wyd = "estas neniu bicikloj"
        elif row == -1:
            self.wyd = "okazis iun eraron, cxar gxi transdonas ke tie estas -1 biciklo - kaj tio estas negativa kvanto"
        elif row <= 0:
            self.wyd = "okazis iun eraron, cxar gxi transdonas ke tie estas " + str(row) + " bicikloj - kaj tio estas negativa kvanto"
        elif row == 1:
            self.wyd = "estas 1  biciklo"
        elif row >= 2:
            if row <= 9:
                self.wyd = ("estas " + str(row) + "  bicikloj")
            if row >= 10:
                self.wyd = ("estas " + str(row) + " bicikloj")
        else:
            self.wyd = ", ni ne scias kiom bicikloj estas tie, cxar dum la akiroprovon de la biciklokvanto okazis la eraro"
        wyd = self.wyd

    def pisul(self):
        wyd = self.wyd
        cz = self.cz
        dz = self.dz
        st = self.stac
        row = self.row
        print dz, cz, "Al la biciklastacion", st, wyd

    def pisp(self):
        cz = self.cz
        dz = self.dz
        st = self.stac
        row = self.row
        print dz, cz, st, row

    def pisc(self):
        cz = self.cz
        dz = self.dz
        st = self.stac
        row = self.row
        print dz, cz, st, row

