#-*- coding UTF-8 -*-


def run():
    list_square=[i for i in range(1,100000) if i%36==0]
    print(list_square)


if __name__ == '__main__':
    run()