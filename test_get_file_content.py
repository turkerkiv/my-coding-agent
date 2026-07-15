from functions.get_file_content import get_file_content

def main():
    result1 = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt sliced: {result1[:1000]}")
    print(f"lorem.txt truncated: {"truncated" in result1}")
    
    result2 = get_file_content("calculator", "main.py")
    print(f"main.py: {result2}")
    print(f"main.py truncated: {"truncated" in result2}")

    result3 = get_file_content("calculator", "pkg/calculator.py")
    print(f"calculator.py: {result3}")
    print(f"calculator.py truncated: {"truncated" in result3}")

    result4 = get_file_content("calculator", "/bin/cat") 
    print(f"bin/cat: {result4}")
    print(f"bin/cat truncated: {"truncated" in result4}")

    result5 = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"does_not_exist.py: {result5}")
    print(f"does_not_exist.py truncated: {"truncated" in result5}")


if __name__ == "__main__":
    main()