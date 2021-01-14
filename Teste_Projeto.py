#Teste 1
import urllib.request

resposta = urllib.request.urlopen('https://download.inep.gov.br/educacao_superior/enade/provas/2017/13_ENG_COM_BACHAREL_BAIXA.pdf')

print(resposta)

html = resposta.read()

print(html)



#Teste 2

import tika
import PyPDF2
import os
from time import perf_counter
from tika import parser
from nltk.tokenize import RegexpTokenizer


arqPDF1 = "Prova_2017.pdf";


# lista de arqs
PDFlist = [arqPDF1]

def saveText(texto, fileName, nameLib):
    """Save the text in a file
    Arguments:
        texto {str} -- text in str format
        fileName {str} -- filename (without path in this code)
        nameLib {str} -- name of extractor project
    """
    arq = open(fileName + "-" + nameLib + ".txt", "w",encoding = "utf-8")
    arq.write(texto)
    arq.close()

def printMiniReport(texto, fileName, nameLib, timeConversion):
    """Shows in the screen, some informations to help compare performance in extract file
    Arguments:
        texto {str} -- text in str format
        fileName {str} -- filename (without path in this code)
        nameLib {str} -- name of extractor project
        timeConversion {float} -- time in seconds
    """
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(texto)
    print(nameLib, " - ", fileName, " - Total of chars: ", str(len(texto)) )
    print(nameLib, " - ", fileName, " - Total of tokens: ", str(len(tokens)) )
    print(nameLib, " - ", fileName, " - Extract time in seconds: ", str(timeConversion) )

def extractPDFwithTika(arqs):
    """Using Apache Tika to extract PDF text - https://pypi.org/project/tika/
    Arguments:
        arqs {str} -- A list of filenames with path
    """
    #the time for load the Tika .jar server impact in first time of use
    tika.initVM()
    for arq in arqs:
        timeIni = perf_counter()
        textoCompleto = parser.from_file(arq)
        fileName = os.path.basename(arq)
        timeEnd = perf_counter()
        timeTotal = timeEnd - timeIni
        printMiniReport(textoCompleto["content"], fileName, "Tika", timeTotal)
        saveText(textoCompleto["content"], fileName, "Tika")
    print("--- Tika ---")


if __name__ == "__main__":
    print(PDFlist)
    extractPDFwithTika(PDFlist)

