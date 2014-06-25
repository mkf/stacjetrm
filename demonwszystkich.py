# -*- coding: utf-8 -*-
import sys
import re
import argparse
from paramdemonwszystkich import *
argu = sys.argv
prmdw = paramdemonwszystkich(argu)
lng = paramdemonwszystkich.lng()
argh = argparse.ArgumentParser()
#argh.add_argument("-l", "--lang", type=str, help="Jednoznakowy kod języka: \nOne-character language code: \nUnulitera lingvkodo: \n - a - English \n - e - Esperanto \n - p - Polski \n - d - Deutsch \n ")
argh.add_argument("-la", "--langenglish", type=
argh.add_argument("-t", "--time", type=int, 
