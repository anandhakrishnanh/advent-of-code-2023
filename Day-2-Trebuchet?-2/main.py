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
            print(number, possible_number, number_is_probable)
            return number_is_probable
        print(number, possible_number, number_is_probable)

    return number_is_probable


# main
def main(path):
    lines = read_input(path)

    possible_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    numbers = []
    for line in lines:
        line = "seightwoone8qxcfgszninesvfcnxc68"
        print(line)
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
                    print(number, possible_number, number_is_probable)

                if not number_is_probable:
                    for possible_number in possible_numbers:
                        if possible_number.startswith(number):
                            number = char
                            print(number, possible_number, True)

                if not number_is_probable:
                    # TODO: what happens if the number[-2] or [-3] or [-n] data should be used for another number
                    number = number[-1]

                if number in possible_numbers:
                    if first_number is None:
                        first_number = possible_numbers.index(number) + 1
                    else:
                        second_number = possible_numbers.index(number) + 1
                    number = number[-1]

            print("Char", char)
            print("first number", first_number)
            print("second number", second_number)
            print("number", number)
            print("#####")

        if first_number is None:
            print("No numbers found in line")
            print(line)
            break

        if second_number is None:
            second_number = first_number

        numbers.append(int(str(first_number) + str(second_number)))
        print(numbers[-1])

        break



    print(sum(numbers))


if __name__ == "__main__":
    start_time = time.time()
    input_txt_path = "input.txt"
    main(input_txt_path)
    print("Execution time: ", time.time() - start_time)
