
test_cases = int(input())


def triangle(number):
    return number * (number+1) / 2


for _ in range(0, test_cases):
    total = 0
    input_string = input()
    set_dict = dict()

    for i in range(0, len(input_string)):
        j = i
        for j in range(0, len(input_string)-i):
            new_array = ''.join(sorted(input_string[i:i+j+1]))
            print((sorted(input_string[i:i+j+1])))
            print(new_array)
            if new_array in set_dict:

                set_dict[new_array] += 1
            else:
                set_dict[new_array] = 1
print(set_dict)
