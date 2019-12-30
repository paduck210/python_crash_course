def next_bigger(n):
# your code here

    list = [int(i) for i in str(n)]
    list.reverse()
    for n in list:
        print(n)


next_bigger(123)
