def rgb(r, g, b):
    redhex=decimaltohex(r)
    greenhex=decimaltohex(g)
    bluehex=decimaltohex(b)
    finalhex=redhex+greenhex+bluehex
    return finalhex
       

# Funcion para convertir de decimal a hex de dos digitos
def decimaltohex(decimal):
    hexadecimal=""
    hexvalues=['0','1','2','3','4','5','6','7','8','9',"A","B","C","D","E","F"] # vars necesarios

    decimal = decimal if decimal <= 255 else 255
    decimal = decimal if decimal >= 0 else 0  # si exceden los limites [0,255] se redondea al mas cercano

    if decimal == 0:  # caso 0
        return f"00"

    if decimal / 16 < 1:  # caso un solo digito
        return f"0{hexvalues[decimal]}"

    while decimal > 0:   # caso dos digitos
        residuo = decimal % 16
        verdadero_caracter = hexvalues[residuo]
        hexadecimal = verdadero_caracter + hexadecimal
        decimal = int(decimal / 16)

    return hexadecimal



print(rgb(1,-100,255)) # test