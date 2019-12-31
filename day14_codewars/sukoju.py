class Sudoku(object):

    def __init__(self, data):
        self.data = data

    def is_valid(self):
        for lst in self.data:
            for number in lst:
                if not isinstance(number, int) or isinstance(number, bool):
                    return False

        num = int(len(self.data[0]) ** 0.5) #3
        first_sum = sum(self.data[0]) #45
        sum_list = [sum(lis[0:int(num)]) for lis in self.data] #[6, 6, 6, 15, 15, 15, 24, 24, 24]
        n = 0
        while n < len(self.data[0]):
            if sum(sum_list[n:n+num]) != first_sum:
                return False
            else:
                n+= num

        length = [len(lis) for lis in self.data]
        max_number = [max(lis) for lis in self.data]

        if length != max_number:
            return False
        else:
            sum_list = [sum(lis) for lis in self.data]
            uniq = set(sum_list)
            if len(uniq) == 1:
                return True
            else:
                return False


bad = [
[1, 2, 3,  4, 5, 6,  7, 8, 9],
[2, 3, 1,  5, 6, 4,  8, 9, 7],
[3, 1, 2,  6, 4, 5,  9, 7, 8],

[4, 5, 6,  7, 8, 9,  1, 2, 3],
[5, 6, 4,  8, 9, 7,  2, 3, 1],
[6, 4, 5,  9, 7, 8,  3, 1, 2],

[7, 8, 9,  1, 2, 3,  4, 5, 6],
[8, 9, 7,  2, 3, 1,  5, 6, 4],
[9, 7, 8,  3, 1, 2,  6, 4, 5]
]

good = [
[7, 8, 4, 1, 5, 9, 3, 2, 6],
[5, 3, 9, 6, 7, 2, 8, 4, 1],
[6, 1, 2, 4, 3, 8, 7, 5, 9],

[9, 2, 8, 7, 1, 5, 4, 6, 3],
[3, 5, 7, 8, 4, 6, 1, 9, 2],
[4, 6, 1, 9, 2, 3, 5, 8, 7],

[8, 7, 6, 3, 9, 4, 2, 1, 5],
[2, 4, 3, 5, 6, 1, 9, 7, 8],
[1, 9, 5, 2, 8, 7, 6, 3, 4]
]

test = Sudoku(good)
# test2 = Sudoku(bad)
# test3 = Sudoku(sample3)
print(test.is_valid())
# print(test2.is_valid())
# print(test3.is_valid())