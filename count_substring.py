def count_substring(string, sub_string):
    count = 0
    for counter, _ in enumerate(range(0, len(string) + 1)):
        new_string = string[counter:]
        if new_string.startswith(sub_string):
            # print(f"{new_string} starts with {sub_string}")
            count += 1
            
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
