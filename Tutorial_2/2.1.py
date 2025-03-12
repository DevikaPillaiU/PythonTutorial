def rem_vowels(text):
    return "".join(character for character in text if character.lower() not in "aeiou")

input_text = "Hello, World!"
print("String after removing vowels:", rem_vowels(input_text))
