

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

def save_result(word, result):
    with open("history.txt", "a") as f:
        f.write(f"{word} -> {'Palindrome' if result else 'Not Palindrome'}\n")

def show_history():
    try:
        with open("history.txt", "r") as f:
            print("\n--- History ---")
            print(f.read())
    except FileNotFoundError:
        print("No history yet!")

while True:
    print("\n1. Check Palindrome\n2. Show History\n3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        word = input("Enter word/sentence: ")
        result = is_palindrome(word)
        print("Palindrome!" if result else "Not Palindrome!")
        save_result(word, result)
    elif choice == "2":
        show_history()
    elif choice == "3":
        break
