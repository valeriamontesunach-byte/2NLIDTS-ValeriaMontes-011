def sumar_digitos_recursivo(numero: int) -> int:
    if numero <= 9:
        return numero
    return(numero % 10) + sumar_digitos_recursivo (numero // 10)


def sumar_digitos_iterativo(numero: int) -> int:
    suma_total = 0
    while numero > 0:
        suma_total += numero % 10
        numero //= 10
    return suma_total


def main():
    print("Suma de Dígitos")
    
    try:
        cantidad = int(input("¿Cuántos números quieres ingresar? "))
    except ValueError:
        print("Ingresa un número entero válido")
        return

    for i in range(1, cantidad + 1):
        numero = int(input(f"Número {i} de {cantidad}: "))
        
        num_abs = abs(numero)

        res_rec = sumar_digitos_recursivo(num_abs)
        res_ite = sumar_digitos_iterativo(num_abs)

        print(f"  > Suma de dígitos (Recursiva): {res_rec}")
        print(f"  > Suma de dígitos (Iterativa): {res_ite}")

    print("\nProceso finalizado")


if __name__ == "__main__":
    main()
