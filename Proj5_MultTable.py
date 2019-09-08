def multTable():
    maximum_value = int(input("How big of a multiplication table should I make it?\n"))
    table = ''
    for num1 in range(1, maximum_value + 1):
        for num2 in range(1, maximum_value + 1):
            table = '\t'.join((table, '{0:2d}'.format(num1*num2)))
        table = '\n'.join((table, '\n'))
        print(table)


multTable()
