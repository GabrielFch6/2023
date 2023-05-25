opc=0
auxiliar=0.15
administrativo=0.10
docente=0.05
valor1=250000
valor2=475000
valor3=800000
while opc!=3:
    print("-"*30)
    print("1. Cotizacion")
    print("2. Renunciar")
    print("3. Salir")
    print("-"*30)
    while True:
        try:
            opc=int(input("Ingrese una opcion: "))
            if 1<=opc<=3:
                break
            else:
                raise ValueError
        except ValueError:
            print("Opcion fuera de rango")
    if opc==1:
      opcT=0
      subtotal=0
      total1=0
      total2=0
      total3=0
      cont1=0
      cont2=0
      cont3=0
    while opcT!=4:
       print("-"*30)
       print("Tratamientos")
       print("-"*30)
       print("1. Carillas Porcelana   $250.000")
       print("2. Implantes Dentales   $475.000")
       print("3. Ortodoncia Brackets  $800.000")
       print("4. Finalizar")
       while True:
        try:
         opcT=int(input("Elija su(s) tratamiento(s): "))
         if 1<=opcT<=4:
            if opcT==1:
                subtotal+=valor1
                cont1+=1
                break
            elif opcT==2:
                subtotal+=valor2
                cont2+=1
                break
            elif opcT==3:
                subtotal+=valor3
                cont3+=1
                break
            else:
                cuota=float((subtotal*0.85)/12)
                print("Finalizando")
                print("-"*30)
                print("Cotizacion")
                print("-"*30)
                print(f"{cont1} tratamiento(s) Carillas Porcelana {cont1*valor1}")
                print(f"{cont2} Implantes Dentales {cont2*valor2}")
                print(f"{cont3} Ortodoncia Brackets {cont3*valor3}")
                print(f"Subtotal   ${subtotal}")
                print("Descuento      ")
                print("-"*30)
                print(f"Total ${subtotal*0.85}")
                print("-"*30)
                print(float(f"Son 12 cuotas de {cuota}"))
                print("Sonria bonito!!")
                break
         else:
          raise ValueError
        except ValueError:
          print("Opcion fuera de rango")
    