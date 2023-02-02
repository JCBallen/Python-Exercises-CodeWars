# A Narcissistic Number (or Armstrong Number) is a positive number which is the sum of its own digits,
# each raised to the power of the number of digits in a given base. In this Kata,
# we will restrict ourselves to decimal (base 10).

# For example, take 153 (3 digits), which is narcisstic:

#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

# and 1652 (4 digits), which isn't:

#     1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938

def narcissistic(value):
    if value <= 0:
        return "Invalid input"  # Solo valido para positivos y mayores a 0
    finalValue = 0
    numToStr = str(value)
    # Asi dividimos en numero en sus digitos
    lista = [int(x) for x in numToStr]
    # Comprobamos la logica de los numeros narcisistas
    fList = list(map(lambda x: pow(x, len(numToStr)), lista))
    for x in fList:
        finalValue += x   # Sumamos los valores de la lista
    return True if finalValue == value else False


print(narcissistic(153))  # Si es un numero narcisista
print(narcissistic(1652))  # No es un numero narcisista

# ---------------------------------------------------------------------------------------------------------------------------
# ? BEST SOLUTION


def best_narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))

# ---------------------------------------------------------------------------------------------------------------------------
def Twonarcissistic(value):
    if value <= 0:
        return "Invalid input"  # Solo valido para positivos y mayores a 0
    finalValue = 0
    # Asi dividimos en numero en sus digitos
    listas = [int(x)**len(str(value)) for x in str(value)]
    # Comprobamos la logica de los numeros narcisistas
    for x in listas:
        finalValue += x   # Sumamos los valores de la lista
    return True if finalValue == value else False


print(Twonarcissistic(153))  # Si es un numero narcisista
