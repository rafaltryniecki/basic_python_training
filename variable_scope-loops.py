def loop_example():
    total = 0
    # Python starts indexing at 0. This makes range(5) produce values 0, 1, 2, 3, 4
    for i in range(5):
        total += i
    print(f"Total sum equals {total=}")
    # The variable 'i' is accessible here after the loop
    print(f"Final value of i after loop: {i}")
    # I could even modify the value of i inside the loop, causing potentially confusing behavior
    total = 0
    for i in range(5):
        i += 10
        print(f"Value of i is equal to {i}")
        total += i
    # After each loop iteration, the value of i is set to the next value.
    print(f"Total sum equals {total=}")
    print(f"Final value of i after loop: {i}")


if __name__ == "__main__":
    loop_example()
