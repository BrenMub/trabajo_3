def main():
    number_1 = int(input("Type the first number: "))
    number_2 = int(input("Type the second number: "))
    result = sum(number_1, number_2)
    print(f"The result is: {result}")


def sum(number_1, number_2):
    return number_1 + number_2


if __name__ == "__main__":
    main()
