# -*- coding: UTF-8 -*-

def Descending_Order(num):
    # Bust a move right here
    list_1 = list(str(num))
    list_1.sort(reverse=True)
    result = "".join(list_1)
    return result

if __name__ == '__main__':
    Descending_Order(987654321)