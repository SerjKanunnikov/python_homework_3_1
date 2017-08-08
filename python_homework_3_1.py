# Прошел тест 8.08 в 10.54.


def create_list():
    mass = [3, 12, 24, 1, 2, 36]
    v = [x for x in mass if x % 3 == 0 and x % 4 == 0]
    print(v)

if __name__ == '__main__':
    create_list()
