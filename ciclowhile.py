cont_corr = "quepasachaval"

while True:
    for i in range(5):
        cont_use = input("Dame la contraseña  ")
        if cont_corr == cont_use:
            print("Contraseña correcta")
            break
        print(f"Contraseña incorrecta, intentos,{i + 1}")
    else: 
        print("Contraseña incorrecta")
        
    break
