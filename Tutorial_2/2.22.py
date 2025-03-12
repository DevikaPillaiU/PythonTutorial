def filter_words(sentence, words_to_exclude):
    word_list = sentence.split()  
    filtered_list = [word for word in word_list if word not in words_to_exclude]
    return " ".join(filtered_list) 

user_input = input("Enter a string: ")

excluded_words = input("Enter words to remove (separated by spaces): ").split()

result_text = filter_words(user_input, excluded_words)
print("\nString after removing given words:")
print(result_text)
