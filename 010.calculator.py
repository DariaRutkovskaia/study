def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


calc_dictionary = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calculator():
    frst_number = float(input("What is the first number? "))
    with_rusult = True
    while with_rusult:
        for symbol in calc_dictionary:
            print(symbol)
        operation = input("Pick an operation  ")
        scnd_number = float(input("What is the next  number? "))
        calc_function = calc_dictionary[operation]
        result = round(calc_function(frst_number, scnd_number), 2)
        print(f"{frst_number}{operation}{scnd_number} = {result}")
        if input(f'Print "y" if you want to continue with {result}, or "n" if you want to start again ') == "y":
            frst_number = result
        else:
            with_rusult = False
            calculator()


calculator()