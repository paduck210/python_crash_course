undone_list = ['robot', 'song', 'warm']
done_list = []
#
# while undone_list:
#     done = undone_list.pop()
#     print(done)
#     done_list.append((done))
# print(done_list)
#

def move_list(undone_list, done_list):
    while undone_list:
        done = undone_list.pop()
        done_list.append(done)
        print(done)
    show_done_list(done_list)

def show_done_list(done_list):
    print(done_list)


move_list(undone_list[:], done_list)

print(undone_list)