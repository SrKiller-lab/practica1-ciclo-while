#se le da el valor a la contraseña
cont_corr = "quepasachaval"

#se inicia el bucle
while True:
    for i in range(5):
        cont_use = input("Dame la contraseña  ")
        if cont_corr == cont_use:
            print("Contraseña correcta")
            break #se rompe el bucle al ingresar la contraseña correcta
        print(f"Contraseña incorrecta, intentos,{i + 1}")
    else: 
        print("Contraseña incorrecta")
        
    break #se rompe el bucle cuando fallas los 5 intentos
