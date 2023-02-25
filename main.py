# represa Hidroituango

# entrado

nivelAgua = int(input('Escribe el nivel del agua; '))

if (nivelAgua >= 0 and nivelAgua <= 250):
    print(f'Nuvel de agua esta por bajo {nivelAgua} metros')
elif (nivelAgua > 250 and nivelAgua <= 400):
    print(f'Nivel de agua esta estable {nivelAgua} metros')
else:
    print(f'Alerta nivel de agua esta por arriba de {nivelAgua} metros')
