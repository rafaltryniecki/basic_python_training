def loops_examples():
    # Example 1: Using a for loop to iterate over a list
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)

    # Example 2: Using a while loop to count down from 5
    count = 5
    while count > 0:
        print(count)
        count -= 1

    # Example 3: Using a for loop with range to print numbers from 0 to 4
    for i in range(5):
        print(i)

    # Example 4: Using a loop to iterate in reverse order. Remember, that the last value will not be visited.
    for i in range(6, 1, -1):
        print(i)


def loops_training():
    # 1. Create a variable that prints out a sum of numbers from 1 to n using loop
    n = 10

    # 2. Create nxm multiplication table
    n = 5
    m = 3

    # 3. Create a loop that prints out even numbers from 1 to n in reverse order
    n = 20

    # 4. Create a loop that iterates through a list of names and prints a greeting for each name
    names = [
        "Alice",
        "Bob",
        "Charlie",
        "Diana",
        "Ethan",
        "Fiona",
        "George",
        "Hannah",
        "Ian",
        "Jane",
        "Kevin",
        "Luna",
        "Mia",
        "Nora",
        "Owen",
        "Paula",
        "Quinn",
        "Riley",
        "Sophia",
        "Tom",
        "Usher",
        "Vera",
        "Wendy",
        "Xander",
        "Yara",
        "Zane",
    ]
    # 5. Move each of above tasks into seperate functions and call them from main function

    # 6. Add type hints to each function


if __name__ == "__main__":
    loops_examples()
