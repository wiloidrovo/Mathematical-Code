"""
Registros <==> Estructuras <==> Diccionarios

key_n = atributo, value_n = valor del atributo

{key_1: value_1,
 key_2: value_2,
 .          .
 .          .
 .          .
 key_n: value_n}
 


{"ID": "value",
 "name": "value",
 "mobile": "value",
 "email": "value",
 "adress": "value"}

def Create_Contact(): # devuelve un contacto

def Search_Contact(): # devuelve una sublista que cumplen con el criterio de búsqueda

def Delete_Contact(): # 

def Update_Contact(): # devuelve un contacto actualizado

def Show_Contact(): # recibe un cintacto y lo muestra

"""

invoices = {}
paid = 0
unpaid = 0
go = True
while go:
    read(op)
    match(op):
        case 0:
            go = False
        case 1:
            read(cod)
            read(amount)
            unpaid += amount
            invoices[cod] = amount
        case 2:
            read(cod)
            amount = invoices.pop(cod, 0)
            unpaid -= amount
            paid += amount
print(paid)
print(unpaid)