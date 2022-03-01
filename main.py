
def calculate():
    while True:
        try:
            bid=float(input("Введи размер ставки (фрибета) "))
            break
        except ValueError:
            print("Значение введено не корректно, допустимы только целые числа ")
    while True:
        try:
            coef1 = float(input("Введи значение коефициента БК1 "))
            break
        except ValueError:
            print("Значение введено не корректно,используй точку как разделитель")
    while True:
        try:
            coef_cover= float(input("Введи коефициент противоположенного исхода БК2 "))
            break
        except ValueError:
            print("Значение введено не корректно,используй точку как разделитель")
    net_income = bid*coef1-bid
    bid_cover = (net_income/coef_cover)
    bid_cover_round = "%.0f" % bid_cover
    net_income_round = "%.2f" % net_income

    print(f"Значение ставки(фрибета) противоположенного исхода БК2 равна {bid_cover_round}")
    print(f"Ожидаемая чистая прибыль составит  {net_income_round}")


if __name__ == "__main__":
    calculate()

while True:
    user_answer = input("Продолжить подсчет  Yes/No? ").lower()
    if user_answer == 'yes':
        calculate()
    else:
        break


