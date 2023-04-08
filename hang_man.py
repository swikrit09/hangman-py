import random
def hangman():
    list_of_Friends=['hema','vaishali','aastha','ishika','pranjal','sparsh','ashutosh','leo','swikrit']
    word= random.choice(list_of_Friends) #word selected
    turns=10
    guess_made=""
    valid_entry= set('abcdefghijklmnopqrstuvwxyz')

    while len(word)>0:
        main_word=""
        for letter in word:
            if letter in guess_made:
                main_word= main_word+letter
            else:
                main_word = main_word + "_ "

        if main_word ==word:
            print(main_word)
            print('Wohooo!! YOU WON :-]')
            break

        print("\nguess MY friend's name ",main_word)
        guess= input()

        if guess in valid_entry:
            guess_made= guess_made+guess
        else:
            print("Enter  a Valid Character")
            guess= input()
        if guess not in word:
            turns= turns-1


        if turns==9:
            print("9 turns left!!")
            print("______________")
        if turns==8:
            print("8 turns left!!")
            print("______________")
            print("      O        ")
        if turns==7:
            print("7 turns left!!")
            print("______________")
            print("      O      ")
            print("      |       ")
        if turns==6:
            print("6 turns left!!")
            print("______________") 
            print("      O      ")
            print("      |       ")
            print("     /        ")
 
        if turns==5:
            print("5 turns left!!")
            print("______________")
            print("      O      ")
            print("      |       ")
            print("     / \       ")
        if turns==4:
            print("4 turns left!!")
            print("______________")
            print("     \O      ")
            print("      |       ")
            print("     / \       ")
        if turns==3:
            print("3 turns left!!")
            print("______________")
            print("     \O/     ")
            print("      |       ")
            print("     / \       ")
        if turns==2:
            print("2 turns left!!")
            print("______________")
            print("     \O/ |    ")
            print("      |       ")
            print("     / \       ")
        if turns==1:
            print("Only 1 turn left, Play carefully!!")
            print("______________")
            print("     \O/_|    ")
            print("      |       ")
            print("     / \       ")
        if turns==0:
            print("AAhhh!!, You let a kind man die :-[ ")
            print("______________")
            print("      O_|    ")
            print("     /|\       ")
            print("     / \      \n\n ")
            print("YOU LOST!!!")
            print('\nThe Name was',word,"\n")
            break
   
    

name=input("\n\n\n\n\nWELCOME TO HANGMAN\n\nEnter Your Name:-- ")
print("Welcome",name," !")
print("-------------------------------------")
print("In this game, you have to guess My friend's name under 10 turns ")
hangman()