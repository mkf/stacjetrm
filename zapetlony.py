import re
import sys
plik = sys.argv[1]
stacyja = sys.argv[2]
slowniczekkoncowek = {'001TOR.jsp': 'jski', '002TOR.jsp': 'rzyny', '003TOR.jsp': 'packiego', '004TOR.jsp': 'torna', '005TOR.jsp': 'ejskie', '006TOR.jsp': 'sytecka', '007TOR.jsp': 'esco', '008TOR.jsp': 'arket', '009TOR.jsp': 'arket', '010TOR.jsp': 'wny', '011TOR.jsp': 'olicji', '012TOR.jsp': 'aciej'}
file = open(plik, 'r')


odnaleziono = re.search(r'w na stacji.*szt', file.read(), re.S)
odnalezione = odnaleziono.group()
stacjowystring = re.sub(r'\D',"",stacyja)
stacja = int(stacjowystring)
renaleziono = re.search(r'

'''
print odnalezione
print stacja
'''


'''
sztuki = re.sub(r'\D',"",re.sub(r'h7', "", re.search( r'<h7>.*szt.*</h7>', file.read(), re.S)))
znalezione = re.search( r'w na stacji.*szt', file.read(), re.S)
znaleziono = znalezione.group()
stacja = re.sub(r'\D',"",stacyja)
st = int(stacja)
znalezionoo = re.search(str(st), znaleziono)
znalezne = znalezionoo.group
znaleznee = znalezne.group
print znalezne
bezHsiedem = re.sub(r'h7', "", znalezne)
samesztuki = re.sub(r'\D', "", bezHsiedem)
#sztuki = re.sub(r'8138746386958797069451995188515142300400600766956124242424242412430551487974106202476424247642424764247642424122', "", samesztuki)
#sztukia = re.sub(r'12341242242424324242442424524', "", sztuki)
szt = int(sztukia)
print 'Na stacji ', stacyja, ' jest ', szt, ' rowerow miejskich.'

print(file.read())
'''


#tu bedzie jeszcze ladny append do jednego csvka
