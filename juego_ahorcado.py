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
    os.system('clear')
    while '_' in mostrar:
        print('Adivina la palabra: ')
        print("".join(mostrar))
        try:
            letra=input('Ingrese una letra: ')
            if not letra.isalpha():
                raise ValueError('Solo puede ingresar letras, intenta denuevo')
            for i,char in enumerate(list(palabra)):
                letra=letra.upper()
                char=char.upper()
                if char==letra:
                    mostrar[i]=char.upper()
            os.system('clear')
        except ValueError as ve:
            os.system('clear')
            print('Error:', ve)
            continue
    os.system('clear')
    print('¡Ganaste!, La palabra era '+palabra.upper())


if __name__=='__main__':
    run()