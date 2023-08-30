x = input("Valor de x: ")
match x:
    case "Hola" | "Adios":
        resp = "Es un Hola"
    case x if (20 > float(x)/4 > 10):
        resp = "Numero entre 10 y 20"
    case _:  # Quiere decir, de lo contrario / Otra cosa / Otherwise
        resp = "Diferente"
print(resp)