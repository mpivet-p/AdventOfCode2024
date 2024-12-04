if __name__ == "__main__":

    list_a = []
    list_b = []

    with open('./input', 'r') as file:
        for line in file:
            t = line.split()
            list_a.append(int(t[0]))
            list_b.append(int(t[1]))

    list_a.sort()
    list_b.sort()

    result = 0
    for i in range(len(list_a)):
        c = list_b.count(list_a[i])
        result += list_a[i] * c 

    print(result)