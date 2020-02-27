while True:
    num = input('Введите целое положительное число: ')
    if num.isdigit():
        num = int(num)
        k = num
        maxi_num = 0
        while num > 0:
            last_digit = num % 10
            if last_digit > maxi_num:
                maxi_num = last_digit
            num = num // 10
        print(f'Наибольшая цифра в числе {k} - это {maxi_num}')
        break
    else:
        print('Ввод некорректный...')
