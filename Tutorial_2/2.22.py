def rem_words(texts, words_removed):
    word_list = texts.split()  
    filtered_list = [word for word in word_list if word not in words_removed]
    return " ".join(filtered_list) 

user_input = input("Enter a string: ")

words_removed = input("Enter words to remove (separated by spaces): ").split()

result_text = rem_words(user_input, words_removed)
print("\nString after removing given words:")
print(result_text)
