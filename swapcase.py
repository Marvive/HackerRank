def swap_case(s):
    string_list = []
    for letter in s:
        if letter.isupper():
            string_list.append(letter.lower())
        else:
            string_list.append(letter.upper())

    return "".join(string_list)


if __name__ == '__main__':
    # s = input()
    s = "thiS Is A Test"
    result = swap_case(s)
    print(result)
