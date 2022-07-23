def iva(importe_bruto:int, impuesto:int):
    importe_neto = (importe_bruto*impuesto)/100 + importe_bruto
    
    return(importe_neto)

def guardar_importes(importe_bruto:int, importe_neto:int, impuesto:int):
    with open("registros_de_iva.txt", "a") as f:
        f.write(f"Importe bruto:{importe_bruto}, Impuesto:{impuesto}, Importe neto:{importe_neto}\n")

importe_bruto = int(input("Ingrese el importe neto: "))

try:
    impuesto = int(input("Ingrese el porcentaje de impuesto (Por defecto 21%. 'Enter' para confirmar): "))
except ValueError:
    impuesto = 21

importe_neto = iva(importe_bruto, impuesto)
print(f"El usuario debe abonar ${importe_neto}.")

guardar_importes(importe_bruto,importe_neto,impuesto)
