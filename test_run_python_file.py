from functions.run_python_file import run_python_file


def main():
    # Test 1: Run main.py (no args)
    print(run_python_file("calculator", "main.py"))

    # Test 2: Run main.py with expression arg
    print(run_python_file("calculator", "main.py", ["3 + 5"]))

    # Test 3: Run calculator tests
    print(run_python_file("calculator", "tests.py"))

    # Test 4: File outside working directory
    print(run_python_file("calculator", "../main.py"))

    # Test 5: Non-existent file
    print(run_python_file("calculator", "nonexistent.py"))

    # Test 6: Non-python file
    print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    main()
