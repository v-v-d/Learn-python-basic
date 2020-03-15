# 5
# Создать (программно) текстовый файл, записать в него программно набор
# чисел, разделенных пробелами. Программа должна подсчитывать сумму
# чисел в файле и выводить ее на экран.


if __name__ == '__main__':
    nums = [str(num) for num in range(15)]

    with open('task_5.txt', 'w', encoding='utf-8') as file:
        file.write(' '.join(nums))

    with open('task_5.txt', encoding='utf-8') as file:
        for line in file:
            nums = line.split()
            print(sum(int(num) for num in nums))
