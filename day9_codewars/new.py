def perimeter(n):
    numbers = [1, 1]
    for i in range(n-1):
        numbers.append(numbers[-1] + numbers[-2])
    return(4 * sum(numbers))

print(perimeter(5)) #, 80)
print(perimeter(7)) #, 216)
print(perimeter(20)) #, 114624)
print(perimeter(30)) #, 14098308)
print(perimeter(100)) #0), 6002082144827584333104)