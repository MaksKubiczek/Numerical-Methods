# function for loading data from a file
def load_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        A = []
        b = []
        for i in range(n):
            row = lines[i+1].split()
            A.append([float(x) for x in row[:-1]])
            b.append(float(row[-1]))
        return A, b


def Gauss(tab):
    for i in range(len(tab)-1):
        if tab[i][i] == 0:
            return print("zero on diagonal - unable to perform calculations\n")
    print("\n")
    size = len(tab)
    for g in range(size-1):
        for i in range(g+1, size):
            m = tab[i][g]/tab[g][g]
            for j in range(size+1):
                if m != 0:
                    tab[i][j] -= tab[g][j]*m
    for j in tab:
        print(j)
    print()

    x = [0 for x in range(size)]
    x[size-1] = round(tab[i][size]/tab[size-1][size-1], 5)
    for i in range(size-2, -1, -1):
        SUM = tab[i][size]
        for k in range(i+1, size):
            SUM -= tab[i][k]*x[k]   # formula for summing xi
        SUM /= tab[i][i]
        x[i] = round(SUM, 5) # rounding to 5 decimal places
    print(x)


if __name__ == '__main__':

    print("Dataset No.1\n")
    A1, b1 = load_data('data1.txt')
    print("Augmented matrix before calculations:")
    for i in range(len(A1)):
        print(A1[i], b1[i])

    f1 = open('data1.txt', 'r')
    for i, line in enumerate(f1):
        if i == 0:
            size = int(line[0])
            tab1 = [[0 for x in range(size+1)] for y in range(size)]
        else:
            for j in range(len(line.split())):
                tab1[i-1][j] = float(line.split()[j])

    f1.close()
    Gauss(tab1)

    print("Dataset No.2\n")
    A2, b2 = load_data('data2.txt')
    print("Augmented matrix before calculations:")
    for i in range(len(A2)):
        print(A2[i], b2[i])

    f2 = open('data2.txt', 'r')
    for i, line in enumerate(f2):
        if i == 0:
            size = int(line[0])
            tab2 = [[0 for x in range(size+1)] for y in range(size)]
        else:
            for j in range(len(line.split())):
                tab2[i-1][j] = float(line.split()[j])

    f2.close()
    Gauss(tab2)
