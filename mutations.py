def mutate_string(string, position, character):
    splitted = list(string)
    splitted[position] = character
    return "".join(splitted)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
