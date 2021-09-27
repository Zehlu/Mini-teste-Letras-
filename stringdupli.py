import sys

def main():

    entrada = str(raw_input())

    saida = rmduplic(entrada)

    print(saida)

def rmduplic(frase):
    x = 0
    frase = frase.split(" ")
    resposta = ""  

    for palavra in frase:
        n = len(palavra) 

        for i in range(n-1, 0, -1):
            if palavra[i:n] == palavra[i-(n-i):i]:
                palavra = palavra[0:i]
                x = x+1
                 
        resposta = resposta + " " + palavra
    
    if x == len(frase):
        return resposta[1:] + "."
    else:
        resposta = " ".join(frase) 
        return resposta + "."

main()