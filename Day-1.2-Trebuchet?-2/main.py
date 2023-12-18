# Question : https://adventofcode.com/2023/day/1#part2
# importing libraries
import time

# importing custom functions


# useful functions
def read_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


def is_number_probable(possible_numbers, number):
    number_is_probable = False
    for possible_number in possible_numbers:
        if possible_number.startswith(number):
            number_is_probable = True
            return number_is_probable

    return number_is_probable


# main
def main(path):
    lines = read_input(path)

    possible_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    numbers = []
    for line in lines:
        first_number = None
        second_number = None
        number = ''
        for char in line:
            try:
                char = int(char)
                if first_number is None:
                    first_number = char
                else:
                    second_number = char
                number = ''
            except:
                number = number + char

                number_is_probable = is_number_probable(possible_numbers, number)
                for possible_number in possible_numbers:
                    if possible_number.startswith(number):
                        number_is_probable = True

                if not number_is_probable:
                    for possible_number in possible_numbers:
                        if possible_number.startswith(number):
                            number = char

                if not number_is_probable:

                    number_is_probable = False
                    for i in range(len(number)):
                        maybe_number_from_previous = number[i: len(number)]
                        if is_number_probable(possible_numbers, number[i: len(number)]):
                            number = number[i: len(number)]
                            number_is_probable = True
                            break

                    if not number_is_probable:
                        number = number[-1]

                if number in possible_numbers:
                    if first_number is None:
                        first_number = possible_numbers.index(number) + 1
                    else:
                        second_number = possible_numbers.index(number) + 1
                    number = number[-1]

        if first_number is None:
            break

        if second_number is None:
            second_number = first_number

        numbers.append(int(str(first_number) + str(second_number)))

    print(sum(numbers))


if __name__ == "__main__":
    start_time = time.time()
    input_txt_path = "input.txt"
    main(input_txt_path)
    print("Execution time: ", time.time() - start_time)
