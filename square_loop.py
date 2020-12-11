# Created by Ryan Nguyen
# Created on December 2020
# This program calculates the powers of 0 to a
#   user inputted positive integer


def main():
    # This function calculates powers

    # loop counter starts at 0
    loop_counter = 0
    # input
    integer_as_string = input("Enter positive integer: ")
    print("")

    # process + output
    try:
        integer_as_number = int(integer_as_string)
        power = integer_as_number
        if integer_as_number >= 0:
            for loop_counter in range(integer_as_number + 1):
                power = loop_counter**2
                print("{}²={}".format(loop_counter, power))
        else:
            print("Integer must be positive")
    except Exception:
        print("Invalid integer")


if __name__ == "__main__":
    main()
