def jc(n):
    count = 1
    for i in range(1, n + 1):
        count *= i

    return count


num = int(input())
print(f"{num}! = {jc(num)}")
