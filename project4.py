def count_words(text):
    # Split the text into words using whitespace as a delimiter
    words = text.split()
    return len(words)

def main():
    # Prompt the user for input
    user_input = input("Please enter a sentence or paragraph: ")

    # Check for empty input
    if not user_input.strip():
        print("Error: You must enter a sentence or paragraph.")
        return

    # Count the words using the count_words function
    word_count = count_words(user_input)

    # Output the result
    print(f"The number of words in the input is: {word_count}")
main()
