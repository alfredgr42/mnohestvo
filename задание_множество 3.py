list = input('Ââåäèòå ÷åðåç ïðîáåë ÷èñëà : ')
numbers = map(int, list.split())
seen = set()
for number in numbers:
    if number in seen:
    print("YES")
else:
    print("NO")
    seen.add(number)
