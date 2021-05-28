"""
program that takes input from clipboard and pastes it as a table
"""
import pyperclip

num_cols = int(input("Enter number of colons:"))
text = pyperclip.paste().split()
longest = 0                                     # index of longest word

for index in range(len(text)):
    if text[index] > text[longest]:
        longest = index
col = 1
for word in text:
    word = word + ('*' * (len(text[longest]) - len(word))) #adds stars to match the length of the longest word
    print(word, end=" ")
    if col % num_cols == 0:
        print("\n", end="")
    col += 1
