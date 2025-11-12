def data_types_examples():
    # Example 1: Integer
    x = 10
    y = -3
    print(x + y)  # addition
    print(x * y)  # multiplication
    print(x**2)  # exponentiation
    print(x // 3)  # floor division

    # Example 2: Float
    pi = 3.14
    price = 9.99

    print(pi * 2)
    print(price + 0.01)
    print(pi / price)

    # Example 3: String
    name = "Alice"
    greeting = "Hello!"
    len(name)  # length of the string
    name.upper()  # uppercase
    print(greeting + name)  # concatenation
    # or if we have it in list, we can join it
    chars = ["H", "e", "l", "l", "o"]
    word = ":)".join(chars)
    print(f"Joined word: {word}")

    # We can refer to strings the same way as to lists:
    first_letter = name[0]  # 'A'
    print(f"First letter: {first_letter}")
    middle_part = name[1:3]  # 'li'
    print(f"Middle part: {middle_part}")
    last_letter = name[-1]  # 'e'
    print(f"Last letter: {last_letter}")

    # Example 4: Boolean
    is_student = True
    is_sunny = False
    print("Is Student:", is_student)

    # Example 5: List
    colors = ["red", "green", "blue"]
    print("Colors:", colors)
    # We can add to the list
    colors.append("yellow")
    print("Updated Colors:", colors)
    # we can slice through lists like strings
    first_two_colors = colors[0:2]
    print("First two colors:", first_two_colors)

    # we can remove from the list
    colors.remove("green")
    print("Colors after removal:", colors)
    # Or by pop method - removes last item by default or item at given index and returns it
    last_color = colors.pop()
    print("Popped color:", last_color)
    print("Colors after pop:", colors)

    # Example 6: Tuple
    # Tuples are immutable lists. Once created, their values cannot be changed.
    # Tuple creation
    point = (10, 20)
    print("Point:", point)
    # point[1] = 30  # This will raise an error if uncommented

    # Tuples are also returned by functions that return multiple values
    def get_coordinates():
        return (5, 15)

    coordinates = get_coordinates()
    print("Coordinates:", coordinates)

    # We can unpack tuples
    x_coord, y_coord = coordinates
    print(f"x: {x_coord}, y: {y_coord}")

    # Example 7: Dictionary
    person = {"name": "Alice", "age": 30}
    print("Person:", person)

    # Accessing values
    print("Name:", person["name"])
    print("Age:", person["age"])
    # Adding a new key-value pair
    person["city"] = "New York"
    print("Updated Person:", person)
    # We can also iterate through keys and values
    for key, value in person.items():
        print(f"{key}: {value}")

    # Example 8: Set
    unique_numbers = {1, 2, 3, 4, 5, 1.0, 2 - 1, 3 * 1, True}
    print("Unique Numbers:", unique_numbers)


def data_types_training():
    # Identify each datatype. You can verify your answers by using the type() function.
    a = 42
    b = 3.14
    c = "hello"
    d = [1, 2, 3]
    e = (4, 5, 6)
    f = {"name": "Alice", "age": 25}
    g = True

    # Write a function that takes a list of numbers and returns their sum and average.
    def sum_and_average(numbers):
        pass

    # Write a function that takes as argument a string and returns the string reversed and in uppercase.
    def reverse_and_uppercase(s):
        pass

    # Write a function that takes a dictionary and returns a list of its keys sorted alphabetically.
    def sorted_keys(d):
        pass

    # Create a list that contains: an integer, a float, a string, a boolean and a dictionary iterate through the list and print each item's type.


if __name__ == "__main__":
    data_types_examples()
