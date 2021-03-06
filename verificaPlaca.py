import re

class VerificaPlaca:
    def __init__(self):
        pass

    def verificar(self,placa):
        pattern = re.compile("[A-Z]{3}-?[0-9]{4}")
                     
        placa = placa.upper()
        placa = ''.join(e for e in placa if e.isalnum())
        placa = list(placa)

        if len(placa) < 7:
            return -1

        if len(placa) > 7:
            placa = placa[:7]

        for pos, letra in enumerate(placa[:3]):
            if not letra.isalpha():
                if letra == '1':
                    placa[pos] = 'I'
                if letra == '3':
                    placa[pos] = 'E'
                if letra == '8':
                    placa[pos] = 'B'
                if letra == '!':
                    placa[pos] = 'I'
                if letra == '0':
                    placa[pos] = 'O'
        
        for pos, numero in enumerate(placa[3:]):
            if not numero.isdigit():
                if numero == 'i' or numero == 'ì' or numero == 'í' or numero == 'I' or numero == "Ì" or numero == "Í" or numero == '!':
                    placa[pos + 3] = '1'
                if numero == 'B':
                    placa[pos + 3] = '8'
                if numero == 'O' or numero == 'o':
                    placa[pos + 3] = '0'

        placa.insert(3,'-')
        placa = ''.join(placa)

        if pattern.match(placa):
            return placa
        else:
            return -1
#
## placas = ["AYH-2598|", "AYH-25 98", "|AYH-259i","|AYH-25988","|AYH-259I", "|AYH-25"]
#placas = ['A1H-259I', 'AY3-259I ', 'ab117i5']
#vp = VerificaPlaca()
#for placa in placas:
#    vp.verificar(placa)
#    placa = ''.join(e for e in placa if e.isalnum())
#    
#    placa = list(placa)
#
#    if len(placa) < 7:
#        print(str(placa) + " erro")
#    
#    if len(placa) > 7:
#        placa = placa[:7]
#    
#    for pos, numero in enumerate(placa[3:]):
#        if not numero.isdigit():
#            if numero == 'i' or numero == 'ì' or numero == 'í' or numero == 'I' or numero == "Ì" or numero == "Í":
#                placa[pos + 3] = '1'
#    
#    for pos, letra in enumerate(placa[:3]):
#        if not letra.isalpha():
#            if letra == '1':
#                placa[pos] = 'I'
#            if letra == '3':
#                placa[pos] = 'E'
#
#    print("placa: " + str(placa))
#
#
# placa = "AYH-2598"
# placa = ''.join(e for e in placa if e.isalnum())
# print(placa)

# i = 0
# for char in placa:
#     if char[i] = 

