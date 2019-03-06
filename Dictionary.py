#importing the libraries.
import json
from difflib import get_close_matches

'''importing the data of dictionary and assigning it to a variable.
this json file contains words and it's meaning in form of key and values.
So the dataset we going to import will automatically gonna convert to dictionary.'''
data = json.load(open('data.json'))

#Creating a class which going to return the meaning of the word.
def translate(w):
    #making the word lowercase in case user type the first word in capital.
    w = w.lower()

    #checking if the  word exist in our diction if yes then it gona return it's value.
    if w in data:
        return data[w]

    '''get_close_match function will return the simiar looking words from w in
    data.keys(which is all the words include in the dictionary). '''
    elif len(get_close_matches(w,data.keys())) > 0:
        '''it will return a list the first element in string will the close guess.
        if that's what user looking for than it will return the meaning of it's word.'''
        yn = input("Do you mean %s if yes press Y else N : " % get_close_matches(w,data.keys())[0])
        if yn == 'y' and 'n' and 'Y' and 'N':
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == '':
            return 'This word doen\'t exist check the word twice.'
        else:
            return 'Give proper input'
    #if the word wasn't in the list then it will return this.
    else:
        return 'This word doen\'t exist check the word twice.'


#printing the number of words dictionary contains
print("The dictionary contain {} words of english language ".format(len(data)))        
while(True):
    #taking the word user need to take it's input on
    word = input("\nEnter the word you want to see the meaning : ")

    #store the meaning on variable called output
    output = translate(word)

    #if the word has multiple meaning it will return a list so we will iterate over it and print it i next lines
    if type(output) == list:
        for i in output:
            print(i)
    else :
        print(output)

    #asking if he wanna see the meaning of another word
    check = input("\n\nDo you want to get meaning of another word if yes press Y else N : ")

    #if it's yes then the loop will continue else it will break
    if check == 'y' and 'Y':
        pass
    elif check == 'n' and 'N':
         print("\nHave a Nice day")
         sign = False
         break
    #in case if user don't give a proper input
    else:
        while(True):
            print("\nEnter the proper commad")
            check = input("Do you want to get meaning of another word if yes press Y else N : ")
            if check == 'y' and 'Y':
                break
            elif check == 'n' and 'N':
                print("\nHave a Nice day")
                sign = False
                break
            else:
                pass
       
