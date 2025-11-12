def main():
    brand_new_cool_variable = "Hello, World!"
    inner_function(brand_new_cool_variable)


def inner_function(variable):
    # But passing it as an argument will work
    print(f"Inner function received: {variable=}")


if __name__ == "__main__":
    main()
