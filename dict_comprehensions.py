#-*- coding UTF-8 -*-


def run():
    dict_cube={i:i**3 for i in range(1,101) if i%3!=0}
    print(dict_cube)


if __name__ == '__main__':
    run()