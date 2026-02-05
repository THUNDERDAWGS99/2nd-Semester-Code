#problem narrative
"""
Problem Narrative:
A large worldwide news agency published articles a few years ago based on the scientific
discovery of how cows are the number 1 cause of pollution. Since these articles were made
a few years ago, they now contain outdated information. The phrase "Number 1 cause" is now
false and needs to be replaced. The news agent needs a quick way to replace "Number 1 cause."
with "Rumored to be a large cause" and other words in the text. 

To do this, the news agent decides to use a Find and Replace Program, but they do not have it yet.
Your task is to write a program that:
1. Let the user enter the original text 
2. Asks the user what they want to change in the text
3. Then asks the user what it wants replaced
4. Lastly, it shows the finished edited text that was changed using this process
"""

#the program the news agent uses to find and replace things
print("Text Editor")

text = input("Enter the original text:\n")
find_word = input("Enter the word or phrase you want to find and replace: ")
replace_word = input("Enter the replacement text here: ")

updated_text = text.replace(find_word, replace_word)
print("\nUpdated the text.:")
print(updated_text)
