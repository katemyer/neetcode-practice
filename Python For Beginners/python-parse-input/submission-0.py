from typing import List

def read_integers() -> List[int]:
    line = input()

    string_list = line.split(",")

    result = []

    for num in string_list:

        result.append(int(num))

    return result

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
