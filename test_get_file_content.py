from functions.get_file_content import get_file_content


def main():
    # Test lorem.txt truncation
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")

    # Test main.py
    print(get_file_content("calculator", "main.py"))

    # Test pkg/calculator.py
    print(get_file_content("calculator", "pkg/calculator.py"))

    # Test path outside working directory
    print(get_file_content("calculator", "/bin/cat"))

    # Test non-existent file
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    main()
