import os
# no borrar, sirven para la primera solucion
import random
import math

os.system("cls")

# ? SIRVE PERO TIENE PROBABILIDAD DE FALLAR, ES A FUERZA BRUTA
# ? Y NO SE SABE SI SE CONSIGUIO EL RESULTADO COMPLETO, SOLO SE APROXIMA BASTANTE BIEN
# def permutations(s):
#     size_s = len(s)
#     list_s = list(s)
#     ans = []
#     null_attempts = 0

#     attempts = math.factorial(size_s)
#     ans.append("".join(list_s))

#     while len(ans)<attempts:
#         random.shuffle(list_s)
#         str_perm = "".join(list_s)
#         if str_perm in ans:
#             str_perm = ""
#             null_attempts += 1
#         else:
#             ans.append(str_perm)
#             str_perm = ""
#             null_attempts = 0

#         if null_attempts>5*attempts:
#             break

#     return ans


# ? MEJOR RESPUESTA QUE PUDE LLEGAR SIN RECURSION, PROBABILIDADES NI LIBRERIAS,
# ? DA SIEMPRE LA RESPUESTA CORRECTA, SOLO QUE ES MUY PESADA

def permutations(s):

    dict_nums_to_letters = {}
    perm_with_nums = []
    translation = [0 for i in range(len(s)**4)] # why 4? pa probar :v
    range_values = list(range(len(s)+1))
    # preparing needed lists
    temp_values = [0 for i in range(len(s))]
    full_i = [0 for i in range(len(s))]
    # for i in range(10**len(s)):
    #     temp_values[i] = 0
    # print(len(temp_values))

    for index, letter in enumerate(s):  # Crea el diccionario correspondiente
        dict_nums_to_letters[index] = letter

    for i in range(10**len(s)):
        s_i = str(i)  # lo pasamos de int a str para poder iterar sobre el
        # enlistador del numero actual, separa cada digito
        list_i = [y for y in s_i]

        # con este iterador eliminamos los valores que sean mayores al rango de numeros
        temp_values = list(map(lambda a: True if int(
            a) in range_values else False, list_i))

        if not all(temp_values):  # si i no esta en [0,1,2,3,...], pasa
            continue

        # rellenador de 0 para que quede tan largo como queremos
        full_i = ["0"]*(len(s)-len(s_i)) + list_i

        # Si al full_i de esta iteracion tiene todos sus valores diferentes lo guardamos
        if len(set(full_i)) == len(s):
            perm_with_nums.append(full_i)

        # Hacemos la traduccion de numeros a letras
        for idx, comb in enumerate(perm_with_nums):
            translation[idx] = [dict_nums_to_letters[int(x)] for x in comb]

    # Unimos las listas en strings y seteamos para que no haya repetidos
    translation = [x for x in translation if x != 0]
    ans = list(set(list(map(lambda a: "".join(a), translation))))
    # print(len(ans))

    return ans


final = sorted(permutations('vfjkh'))
print(final)



