import string

def solve(s):
    # _list = []
    # for words in s.split():
    #     _list.append(words.capitalize())
    # return " ".join(_list)
    return string.capwords(s, ' ')


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    print(result)
    # fptr.write(result + '\n')

    # fptr.close()
