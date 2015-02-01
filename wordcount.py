### wordcount.py

#SERVER
#Source Configuration
import sys

import glob


text_files = glob.glob('/home/gabriel/Escritorio/hw3data/test/*')

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
    print key.split('Z9z9z9')[0], key.split('Z9z9z9')[1], value[1]
#sys.exit()

# CLIENTS
#Mappers
def mapfn(key, value):
    badchars= {'@':' ','[':' ',',':' ','.':" ",'!':' ',',':' ',';':' ',']':' ','-':' ','?':' ','_':' ',':':' ', '/':' '}
    stop_words={'about','above','after','again','against','all','am','an','and','any','are','arent','as','at','be','because','been','before','being','below','between','both','but','by','cant','cannot','could','couldnt','did','didnt','do','does','doesnt','doing','dont','down','during','each','few','for','from','further','had','hadnt','has','hasnt','have','havent','having','he','hed','hell','hes','her','here','heres','hers','herself','him','himself','his','how','hows','i','id','ill','im','ive','if','in','into','is','isnt','it','its','its','itself','lets','me','more','most','mustnt','my','myself','no','nor','not','of','off','on','once','only','or','other','ought','our','ours ','ourselves','out','over','own','same','shant','she','shed','shell','shes','should','shouldnt','so','some','such','than','that','thats','the','their','theirs','them','themselves','then','there','theres','these','they','theyd','theyll','theyre','theyve','this','those','through','to','too','under','until','up','very','was','wasnt','we','wed','well','were','weve','were','werent','what','whats','when','whens','where','wheres','which','while','who','whos','whom','why','whys','with','wont','would','wouldnt','you','youd','youll','youre','youve','your','yours','yourself','yourselves'}
    for line in value.splitlines(): #De todas las lineas

	word1=line.split(':::') #Separo en directorio, autores y titulo
	word2=word1[1].split('::') #Ahora separo autores para un dado titulo

    	for i, j in badchars.iteritems():
        	word1[2] = word1[2].replace(i, j)

	word4=word1[2].split()
	new_string=" "
        for item1 in word4:
		if (item1 not in stop_words):
#		       print new_string
	               new_string = new_string + item1 + " "      

	word4=new_string.split() #Ahora separo palabras de ese titulo... (Falta por iterar quitando palabras invalidas)

#	word4=word1[2].split()

    	for item in word2: #A cada autor le anexo palabras y envio...
		for item2 in word4:
			if (item2.__len__()>1):
				word3=item+'Z9z9z9'+item2.lower() #Combo autor codigo palabra
#				print word3
				yield word3, 1
#sys.exit()

#Reducers
def reducefn(key, value):
    return key, len(value)
#sys.exit()
