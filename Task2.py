# my name is enas mostafa . i am twenty years old. i am a student at the faculty of computers and artificial intelligence. my major is information systems. 
#import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
text=input("Enter  a text , please:\n")
print(" Enter : \n 1 for word tokenization \n 2 for sentence tokenization \n 3 for  original text \n your choice is :")
choice=int(input())
if choice == 1:
    print(word_tokenize(text))
elif choice==2:
    print(sent_tokenize(text))
elif choice==3:
    print(text)
else:
    print("please , enter a right number")





