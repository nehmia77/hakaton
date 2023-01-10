def geez(g):
    geez_number = ["፩", "፪", "፫", "፬", "፭", "፮", "፯", "፰", "፱", "፲", "፳", "፴", "፵", "፶", "፷", "፸", "፹", "፺", "፻", "፼"]
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 10000]
    i = 19
    geez = " "
    while g != 0:
        if g >= number[i]:
            geez += geez_number[i]
            g = g - number[i]
        else:
            i -= 1
    print(geez)
geez(int(input("Enter number:")))