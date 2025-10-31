# Changing case
name = "Rose Shade"
print(name.upper()) # Output: ROSE SHADE
print(name.lower()) # Output: rose shade
print(name.title()) # Output: Rose Shade

text = "I love Python programming"
print(text.count("o")) 
# Counts how many 'o' are in the string
print("Python" in text)
# Checks if 'Python' is a substring of text
print(text.replace("Python", "Java"))
# Replaces 'Python' with 'Java' in the string

sentence = "I am learning Python"
words = sentence.split() 
# Splits the sentence into a list of words
print(words)

joined = "_".join(words)
# Joins words with "_"
print(joined)

msg = "   Hello World!      "
print(msg.strip())
# Remove extra spaces from both ends

quote = input("Enter your favorite quote:")
print("Uppercase:", quote.upper())
print("Lowercase:", quote.lower())
print("Title Case:", quote.title())
print("Number of 'a':", quote.count("a"))
print("You" in quote)
print("Replaced quote", quote.replace("stay positive", "be happy"))
print("Words in quote:", quote.split())
print("Joined with '/':", "/".join(quote.split()))
print("Remove extra spaces:", quote.strip())


