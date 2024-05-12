def test(hospital, *date, doctor="Олег", **patient):
    print('Ваша больница:', hospital)
    print('Свободные числа для записи на прием в этом месяце:', *date)
    print('Ваш доктор:', doctor)
    print('Ваша личная информация:')
    for key, value in patient.items():
        print(value)


test('Городская больница №3', 12, 15, 17, 28, name='Алиса', surname='Петрова')


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


print(factorial(int(input())))
