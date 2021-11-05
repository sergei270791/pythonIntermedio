#-*- coding UTF-8 -*-


def run():
    list_square=list()
    for i in range(1,101):
        if i%3==0:
            continue
        list_square.append(i**2)
    print(list_square)


if __name__ == '__main__':
    run()