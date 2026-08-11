from functions.write_file import write_file


def main():
    # Test 1: Overwrite existing/new file in working dir
    print(
        write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    )

    # Test 2: Write file inside a subdirectory (creates missing folder if needed)
    print(
        write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    )

    # Test 3: Attempt to write outside the permitted working directory
    print(
        write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    )


if __name__ == "__main__":
    main()
