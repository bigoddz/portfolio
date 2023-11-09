while True:

    print("Welcome to the Quiz!")
    print("Press 1 for Film")
    print("Press 2 for History")
    print("Press 3 for Gaming")

    option=int(input("Please choose a number to start the quiz: "))
    points=0

def film():
    
    if option==1:
        print("The Movie Quiz, Question 1")
        print("What year did Home Alone come out?: ")
        print("A:1991")
        print("B:1992")
        print("C:1995")
        print("D:1990")

        ans_film1=str(input("Please choose A, B, C or D: ")).upper()
          
        if ans_film1=="A":
            points=points-5
        elif ans_film1=="B":
            points=points-5
        elif ans_film1=="C":
            points=points-5
        elif ans_film1=="D":
            points=points+10

        print("The Movie Quiz, Question 2")
        print("How many Matrix Films are there?: ")
        print("A:5")
        print("B:4")
        print("C:6")
        print("D:3")

        ans_film1=str(input("Please choose A, B, C or D: ")).upper()
          
        if ans_film1=="A":
            points=points-5
        elif ans_film1=="B":
            points=points+10
        elif ans_film1=="C":
            points=points-5
        elif ans_film1=="D":
            points=points-5

        print("The Movie Quiz, Question 3")
        print("What colour were the pills Neo had to choose from in The Matrix?: ")
        print("A:Blue&Red")
        print("B:Red&White")
        print("C:Red&Green")
        print("D:Red")

        ans_film1=str(input("Please choose A, B, C or D: ")).upper()
          
        if ans_film1=="A":
            points=points+10
        elif ans_film1=="B":
            points=points-5
        elif ans_film1=="C":
            points=points-5
        elif ans_film1=="D":
            points=points-5

        print("The Movie Quiz, Question 4")
        print("How many Rocky movies are there?: ")
        print("A:8")
        print("B:5")
        print("C:7")
        print("D:6")

        ans_film1=str(input("Please choose A, B, C or D: ")).upper()
          
        if ans_film1=="A":
            points=points-5
        elif ans_film1=="B":
            points=points-5
        elif ans_film1=="C":
            points=points-5
        elif ans_film1=="D":
            points=points+10

        print("The Movie Quiz, Question 5")
        print("Who was the first James Bond?: ")
        print("A:Roger Moore")
        print("B:Sean Connery")
        print("C:Daniel Craig")
        print("D:Pierce Brosnan")

        ans_film1=str(input("Please choose A, B, C or D: ")).upper()
          
        if ans_film1=="A":
            points=points-5
        elif ans_film1=="B":
            points=points+10
        elif ans_film1=="C":
            points=points-5
        elif ans_film1=="D":
            points=points-5
            

    option=int(input("Please choose a number to start the quiz: "))

def history():
    
    if option==2:
        print("The History Quiz, Question 1")
        print("What year did D-Day take place?: ")
        print("A:1944")
        print("B:1940")
        print("C:1943")
        print("D:1945")

        ans_his1=str(input("Please choose A, B, C or D: ")).upper()
          
        if ans_his1=="A":
            points=points+10
        elif ans_his1=="B":
            points=points-5
        elif ans_his1=="C":
            points=points-5
        elif ans_his1=="D":
            points=points-5

        print("The History Quiz, Question 2")
        print("When did Che Guevara die?: ")
        print("A:1968")
        print("B:1970")
        print("C:1965")
        print("D:1967")

        ans_his1=str(input("Please choose A, B, C or D: ")).upper()
          
        if ans_his1=="A":
            points=points-5
        elif ans_his1=="B":
            points=points-5
        elif ans_his1=="C":
            points=points-5
        elif ans_his1=="D":
            points=points+10

        print("The History Quiz, Question 3")
        print("When did WW2 End?: ")
        print("A:1945")
        print("B:1943")
        print("C:1940")
        print("D:1946")

        ans_his1=str(input("Please choose A, B, C or D: ")).upper()
          
        if ans_his1=="A":
            points=points+10
        elif ans_his1=="B":
            points=points-5
        elif ans_his1=="C":
            points=points-5
        elif ans_his1=="D":
            points=points-5

        print("The History Quiz, Question 4")
        print("How many Wives did Henry VIII have?: ")
        print("A:5")
        print("B:8")
        print("C:7")
        print("D:6")

        ans_his1=str(input("Please choose A, B, C or D: ")).upper()
          
        if ans_his1=="A":
            points=points-5
        elif ans_his1=="B":
            points=points-5
        elif ans_his1=="C":
            points=points+10
        elif ans_his1=="D":
            points=points-5

        print("The History Quiz, Question 5")
        print("How old was Queen Elizabeth II when she died?: ")
        print("A:100")
        print("B:96")
        print("C:98")
        print("D:95")

        ans_his1=str(input("Please choose A, B, C or D: ")).upper()
          
        if ans_his1=="A":
            points=points-5
        elif ans_his1=="B":
            points=points+10
        elif ans_his1=="C":
            points=points-5
        elif ans_his1=="D":
            points=points-5

    option=int(input("Please choose a number to start the quiz: "))

def gaming():

    if option==3:
        print("The Gaming Quiz, Question 1")
        print("Who created valve?: ")
        print("A:Gabe Nevel")
        print("B:Bill Gates")
        print("C:Gabe Nawell")
        print("D:Keith Carlsen")

        ans_game1=str(input("Please choose A, B, C or D: ")).upper()
          
        if ans_game1=="A":
            points=points-5
        elif ans_game1=="B":
            points=points-5
        elif ans_game1=="C":
            points=points+10
        elif ans_game1=="D":
            points=points-5

        print("The Gaming Quiz, Question 2")
        print("When did the first Call of Duty come out?: ")
        print("A:2003")
        print("B:2005")
        print("C:2000")
        print("D:2004")

        ans_game1=str(input("Please choose A, B, C or D: ")).upper()
          
        if ans_game1=="A":
            points=points+10
        elif ans_game1=="B":
            points=points-5
        elif ans_game1=="C":
            points=points-5
        elif ans_game1=="D":
            points=points-5

        print("The Gaming Quiz, Question 3")
        print("What is the best selling console of all time?: ")
        print("A:PlayStation 4")
        print("B:Nintendo NES")
        print("C:PlayStation 2")
        print("D:Xbox 360")

        ans_game1=str(input("Please choose A, B, C or D: ")).upper()
          
        if ans_game1=="A":
            points=points-5
        elif ans_game1=="B":
            points=points-5
        elif ans_game1=="C":
            points=points+10
        elif ans_game1=="D":
            points=points-5

        print("The Gaming Quiz, Question 4")
        print("Which was the first video game to be played in space?: ")
        print("A:Super Mario")
        print("B:Donkey Kong")
        print("C:Pokemon")
        print("D:Tetris")

        ans_game1=str(input("Please choose A, B, C or D: ")).upper()
          
        if ans_game1=="A":
            points=points-5
        elif ans_game1=="B":
            points=points-5
        elif ans_game1=="C":
            points=points-5
        elif ans_game1=="D":
            points=points+10

        print("The Gaming Quiz, Question 5")
        print("What is the name of the final course of all Mario Kart?: ")
        print("A:Rainbow Road")
        print("B:Peach Beach")
        print("C:Koopa Cape")
        print("D:Coconut Mall")

        ans_game1=str(input("Please choose A, B, C or D: ")).upper()
          
        if ans_game1=="A":
            points=points-5
        elif ans_game1=="B":
            points=points-5
        elif ans_game1=="C":
            points=points-5
        elif ans_game1=="D":
            points=points+10

        print("Your Final Score out of 75 is: ",points)

while True:
    print("Welcome to the Quiz!")
    print("Press 1 for Film")
    print("Press 2 for History")
    print("Press 3 for Gaming")

    option=int(input("Please choose a number to start the quiz: "))

    if option==1:
        movies()
    elif option==2:
        history()
    elif option==3:
        gaming()
    else:
        print("Wrong Input")

    opt0=str(input("Press N to exit or Enter to continue ")).upper()
    if opt0=="N":
             break
        


        





