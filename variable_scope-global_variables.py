cool_variable_name = "Hello, Evil World!"


def main():
    # if I make a mistake (or don't know better) or don't know that there are somewhere in the other modules global variables,
    # I can accidentally use the same name for my variable and it my cause unexpected behavior.

    inner_function(cool_variable_name)


def inner_function(variable):
    # But passing it as an argument will work
    print(f"Inner function received: {variable=}")


if __name__ == "__main__":
    main()
