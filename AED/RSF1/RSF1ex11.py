print("Qual é a sua fase de vida, neste momento? Vamos ver")
idade = int(input("Seleccione a sua idade: "))

match idade:
    case idade if 0 <= idade <= 2:
        print(f"Para alguém com {idade} anos, o resultado esperado deve ser infância- primeira infância.")
    case idade if 3 <= idade <= 6:
        print(f"Para alguém com {idade} anos, o resultado esperado deve ser infância- infancia intermediaria.")
    case idade if 7 <= idade <= 12:
        print(f"Para alguém com {idade} anos, o resultado esperado deve ser infância- pré adolescencia.")
    case idade if 10 <= idade <= 14:
        print(f"Para alguém com {idade} anos, o resultado esperado deve ser adolescência- puberdade.")
    case idade if 15 <= idade <= 19:
        print(f"Para alguém com {idade} anos, o resultado esperado deve ser adolescência- adolescencia tardia.")
    case idade if 20 <= idade <= 39:
        print(f"Para alguém com {idade} anos, o resultado esperado deve ser adultez- jovem adulto.")
    case idade if 40 <= idade <= 59:
        print(f"Para alguém com {idade} anos, o resultado esperado deve ser adultez- media-idade.")
    case idade if 60 <= idade <= 74:
        print(f"Para alguém com {idade} anos, o resultado esperado deve ser terceira idade- idosos jovens.")
    case idade if idade >=75:
        print(f"Para alguém com {idade} anos, o resultado esperado deve ser terceira idade- idosos velhos.")
    case _:
        print("Repete")