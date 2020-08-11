# if __name__ == '__main__':
#     N = int(input())
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

N = int(input())
my_list = []
for _ in range(N):
    entry = input()
    if entry == "print":
        print(my_list)
    elif "insert" in entry:
        inserter = entry.split()
        sliced = list(map(int, inserter[1:]))
        my_list.insert(sliced[0], sliced[1])
    elif "remove" in entry:
        remover = entry.split()[1]
        remove_int = int(remover)
        my_list.remove(remove_int)
    elif "append" in entry:
        appender = entry.split()
        my_list.append(int(appender[1]))
    elif entry == "sort":
        my_list.sort()
    elif entry == "pop":
        my_list.pop()
    elif entry == "reverse":
        my_list.reverse()

        

