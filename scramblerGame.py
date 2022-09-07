from ast import IsNot
import requests
import codecs
import string
import random as rancho


def generateWords():
    i = 0 
    j = 0
    wordsDecoded = [] #emptylist
    mydict = {} # empty dictionary
    alphabetList = list(string.ascii_uppercase) #Create an alphabet list
    site = "https://www.mit.edu/~ecprice/wordlist.10000" # create the site address
    response = requests.get(site)# a 200 response if site is available
    #print(response) it is a 200
    byteWords = response.content.splitlines() #will split all our words by lines but contents will be on bytes
    #print("How Many words are there on this site in bytes :", len(byteWords))#count list of wordslength

    #This loop will help us convert the byte words to string words
    while i < len(byteWords):
        wordsDecoded.append(codecs.decode(byteWords[i], 'UTF-8'))
        i = i + 1
    #print(type(wordsDecoded))

    #this loop will help us assign a set of words per alphabet letter to our dictionary note I decided to make our keys for our dictionary upper case while our site has only lower case letters so it needs to be converted 
    # accordingly to find them and append it to our keys
    while j < len(alphabetList):
        mydict["Letter:" + alphabetList[j]+""] = [spec for spec in wordsDecoded if spec.startswith((alphabetList[j]).lower())]
        j = j + 1 
    
    return mydict, alphabetList




def getPlayerLetter():
    correctInputcheck = False
    while correctInputcheck == False:
        PlayerInput = input("Please Select a letter of the Alphabet to Continue : ")
        if any([letter == PlayerInput.upper() for letter in alphabetList ]):        
           return PlayerInput.upper()
           correctInputcheck == True
        else:
            print("No, that is not right Please enter a correct Value from the Alphabet!")
            

def pickWords(letter=None):
    # If the user has selected a letter or if user has selected random
    #lets pick a random word by choosing and random word in the dictionary by selecting a random letter from our alphabet list 
    if letter == None: 
     randWord = rancho.choice(mydict['Letter:'+rancho.choice(alphabetList)])
    elif letter != None:
     randWord = rancho.choice(mydict['Letter:'+rancho.choice(letter)])   
    
    
   
    return randWord


mydict, alphabetList = generateWords()
randWord = pickWords()

def getPlayerChoice():
    PlayerInput = input("Please Make a Choice to Continue.. ")
    return PlayerInput

def wordScrambler(randWord):
    #wrong word var
    randWord = ''.join(rancho.sample(randWord,len(randWord)))
    print("Your Scrambled Word is : ")
    return randWord       

def decodeByUser():
    correctGuess = False
    while correctGuess == False:
        playerGuess = input("Please Enter your solution: ")
        if playerGuess != randWord:
            print("NO! that is not right, please try again!!")
        else:    
         correctGuess = True
    return playerGuess

        
def automaticDecode():
    desorden = ""
    correctCounter = 0
    #this loop would try to decode to the correct word by running the same word on random characters
    while desorden != randWord:
        desorden = ''.join(rancho.sample(randWord,len(randWord)))
        correctCounter = correctCounter + 1             
        if desorden != randWord:
         print(desorden)
        if correctCounter == 5000:
         desorden = randWord 
    return desorden
    

waitingfForInput = True

while waitingfForInput:
    print("Ahh Welcome Welcome! to your word Scrambler!! Please make a choice: ")
    print("  1: Select 1 if you want to choose a letter from the Alphabet for your word")
    print("  2: Select 2 if you wish to get a random word to decipher")
    print("  3: Select any other key to quit ")
    playerChoice = getPlayerChoice()
    if playerChoice == '1':
         letterChosen = getPlayerLetter()         
         randWord  = pickWords(letterChosen)  
         scrambledWord = wordScrambler(randWord)
         print("Your Scrambled Word is: ", scrambledWord)
         print("Would you like to decipher it? Select 1; If you want Python to try to decode it Press 2; Press any other key to exit")
         scrambleChoice = getPlayerChoice() 
         if scrambleChoice == '1':
            wordDecoded = decodeByUser()
            print("Correct! you have decoded to the word ", wordDecoded + " Succesfully! ")
         elif scrambleChoice == '2':
            wordDecoded = automaticDecode()
            print("Your word Decoded is : ", wordDecoded)
         elif scrambleChoice != 1 or scrambleChoice != 2:
            waitingfForInput = False

    elif playerChoice == '2':        
         randWord, correctWord = pickWords()         
    elif playerChoice != '1' or playerChoice != '2':
         print("Exiting Program ... --")
         waitingfForInput = False
