N = int(input("������� ����������� �����: "))
numbers = list(map(int, input(f'������� ����� ������ {N} �����: ').split()))
number_list = set(numbers)
print(len(number_list))