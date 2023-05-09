def calculate_check_digits(distributor, free_assignment):
    # Concatenar y convertir a entero
    cups = int(distributor + free_assignment)

    # Calcular resto R0
    rest_R0 = cups % 529

    # Calcular cociente C y resto R
    cons_C = rest_R0 // 23
    rest_R = rest_R0 % 23

    # Tabla de equivalencias
    equivalenceTable = {
        0: 'T', 1: 'R', 2: 'W', 3: 'A', 4: 'G',
        5: 'M', 6: 'Y', 7: 'F', 8: 'P', 9: 'D',
        10: 'X', 11: 'B', 12: 'N', 13: 'J', 14: 'Z',
        15: 'S', 16: 'Q', 17: 'V', 18: 'H', 19: 'L',
        20: 'C', 21: 'K', 22: 'E'
    }

    letter_C = equivalenceTable[cons_C]
    letter_R = equivalenceTable[rest_R]

    return letter_C + letter_R
