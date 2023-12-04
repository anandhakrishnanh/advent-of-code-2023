# Question : https://adventofcode.com/2023/day/
# importing libraries
import time

# importing custom functions


# useful functions
def read_input(path):
    with open(path, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]


# main
def main(path):
    lines = read_input(path)

    numbers = []
    for line in lines:
        first_number = None
        second_number = None
        for char in line:
            try:
                char = int(char)
                if first_number is None:
                    first_number = char
                else:
                    second_number = char
            except:
                pass

        if first_number is None:
            print("No numbers found in line")
            print(line)
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
