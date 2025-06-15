def format_filename(filename: str) -> str:
    cleaned = []
    for char in filename:
        if char.isalnum():
            cleaned.append(char)
        elif char == ' ':
            cleaned.append('_')
        # Ignore all other characters (special characters)
    return ''.join(cleaned) + '.py'


def main():
    user_input = input("Enter file name: ")
    result = format_filename(user_input.strip())
    print("Formatted file name:", result)


if __name__ == "__main__":
    main()
