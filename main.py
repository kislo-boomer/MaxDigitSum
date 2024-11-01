import sys
sys.stdout.reconfigure(encoding='utf-8')

def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

def main():
    print("Введите целые числа по одному. Введите 0, чтобы завершить.")
    max_number = None
    max_sum = -1

    while True:
        try:
            num = int(input("Введите число: "))
            if num == 0:
                break
            current_sum = sum_of_digits(num)
            if current_sum > max_sum:
                max_sum = current_sum
                max_number = num
        except ValueError:
            print("Пожалуйста, введите целое число.")

    if max_number is not None:
        print("Число с максимальной суммой цифр:", max_number)
    else:
        print("Вы не ввели ни одного числа.")

if __name__ == "__main__":
    main()
