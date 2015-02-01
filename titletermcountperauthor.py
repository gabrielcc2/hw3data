### wordcount.py


#SERVER
#Source Configuration
import sys

import glob

text_files = glob.glob('test/*.*')

def file_contents(file_name):
    f = open(file_name)
    try:
        return f.read()
    finally:
        f.close()

source = dict((file_name, file_contents(file_name))
              for file_name in text_files)

#Final Configuration (get results)
def final(key, value):
    print key, value
#sys.exit()

# CLIENTS
#Mappers
def mapfn(key, value):
    for line in value.splitlines():
#Aqui tendria que parsear, agarrar los campos que me interesan, y agarrar las palabras que me interesan, esas son las que voy a yield, junto al nombre del #autor...
#Teoricamente la primera es la palabra, la segunda el count. Yo tendria que enviar palabra, autor y count.
        for word in line.split():
          yield word.lower(), 1
#sys.exit()

#Reducers
def reducefn(key, value):
    return key, len(value) #La primera es la palabra, la segunda es el numero de repeticiones. Yo tendria que hacer lo mismo, pero todavia llevar al autor junto a la palabra como key...
#sys.exit()
