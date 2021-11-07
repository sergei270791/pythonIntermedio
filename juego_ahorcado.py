#-*- coding UTF-8 -*-
import random, os


def read_data():
    palabras=[]
    with open("./archivos/data.txt", "r",encoding='utf-8') as f: 
        for line in f:
            palabras.append(line)
    return str(random.choice(palabras)).rstrip('\n')


def run():
    palabra=read_data()
    mostrar=list('_'*len(palabra))
    while '_' in mostrar:
        os.system('clear')
        print('Adivina la palabra: ')
        print("".join(mostrar))
        letra=input('Ingrese una letra: ')
        for i,char in enumerate(list(palabra)):
            if char==letra:
                mostrar[i]=char.upper()
    os.system('clear')
    print('¡Ganaste!, La palabra era '+palabra.upper())


if __name__=='__main__':
    run()