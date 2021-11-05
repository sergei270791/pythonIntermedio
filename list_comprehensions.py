#-*- coding UTF-8 -*-


def run():
    list_square=[i**2 for i in range(1,101) if i%3!=0]
    print(list_square)


if __name__ == '__main__':
    run()