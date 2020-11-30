for numero in range(1, 10):
    lista_cinco = [5, 10, 15, 20, 25, 30, 35, 40, 45]

    print(f'{"Número da vez " + f"{numero}, utiliza a tabuada do: " + str(numero - 5):^25} ')
    for c in range(1, 10):
        num_opera = 0
        if numero < 5:
            num_opera = '- ' + str(((numero - 5) * c) * - 1)

        elif numero > 5:
            num_opera = '+ ' + str((numero - 5) * c)

        print(f'      {numero} x {c} = {numero * c:<3} '
              f' {lista_cinco[c - 1]:>3} {num_opera:^4} = {numero * c:<3}')
    print()
