#-*- coding UTF-8 -*-


def run():
    dict_cube=dict()
    for i in range(1,101):
        if i%3!=0:
            dict_cube[i]=i**3
    print(dict_cube)


if __name__ == '__main__':
    run()