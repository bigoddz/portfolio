name_individual=[]#creating a list
teamnames=["t1","t2","t3","t4"]

name_team1=[]
name_team2=[]
name_team3=[]
name_team4=[]

event1=[]
event2=[]
event3=[]
event4=[]

e1_order=[]
e2_order=[]
e3_order=[]
e4_order=[]

point_event_first=10
point_event_second=8
point_event_third=6
point_event_fourth=4

Team1=0
Team2=0
Team3=0
Team4=0

name_individual_point=0

print("Welcome to the O2 Tournament")

print("In this tournament there will be up to 20 invdividuals participating")

print("There could be 4 teams with 5 group members")

print("The events that are available in this tournament are Film, History and Gaming")

print("An individual or a Team will need at least 95 out of 100 points to be 1st")

print("An individual gets 5+ extra for each question")

print("The 2nd place will be the 1st place minus 5 points and the same for 3rd place etc")

while True:
        teamorind=str(input("press T for Team or I for individual competition: ")).upper()
        if teamorind=="I":
            for a in range(1,21):
                print("type the name of the individual: ",a)
                name=input()
                name_individual.append(name)

        for a in range(0,4):
                print("type the name of the individual in order that came 1st,2nd,3rd and 4th in the 1st event")
                order1=input()
                e1_order.append(order1)

        if e1_order[0]=='name_individual_0':
                name_individual=name_individual_point+point_event_first
        elif e1_order[1]=='name_individual_1':
                name_individual=name_individual_point+point_event_second
        elif e1_order[2]=='name_individual_2':
                name_individual=name_individual_point+point_event_third
        else:
                name_individual=name_individual_point+point_event_fourth

        for a in range(0,4):
                print("type the name of the individual in order that came 1st,2nd,3rd and 4th in the 2nd event")
                order1=input()
                e2_order.append(order1)

        if e2_order[0]=='name_individual_0':
                name_individual=name_individual_point+point_event_first
        elif e2_order[1]=='name_individual_1':
                name_individual=name_individual_point+point_event_second
        elif e2_order[2]=='name_individual_2':
                name_individual=name_individual_point+point_event_third
        else:
                name_individual=name_individual_point+point_event_fourth

        for a in range(0,4):
                print("type the name of the individual in order that came 1st,2nd,3rd and 4th in the 3rd event")
                order3=input()
                e3_order.append(order1)


        if e3_order[0]=='name_individual_0':
                name_individual=name_individual_point+point_event_first
        elif e3_order[1]=='name_individual_1':
                name_individual=name_individual_point+point_event_second
        elif e3_order[2]=='name_individual_2':
                name_individual=name_individual_point+point_event_third
        else:
                name_individual=name_individual_point+point_event_fourth

        for a in range(0,4):
                print("type the name of the individual in order that came 1st,2nd,3rd and 4th in the 4th event")
                order4=input()
                e4_order.append(order1)

        if e4_order[0]=='name_individual_0':
                name_individual=name_individual_point+point_event_first
        elif e4_order[1]=='name_individual_1':
                name_individual=name_individual_point+point_event_second
        elif e4_order[2]=='name_individual_2':
                name_individual=name_individual_point+point_event_third
        else:
                name_individual=name_individual_point+point_event_fourth


        opt=str(input("To Add More press Enter to Quit Press Q: "))
    
        if opt=="Q":
            break

while True:        
                
        if teamorind=="T":
            
            for a in range(1,6):
                print("type the name of the team member of team 1 members: ",a)
                name1=input()
                name_team1.append(name1)

            for a in range(1,6):
                print("type the name of the team member of team 2 members: ",a)
                name2=input()
                name_team2.append(name2)

            for a in range(1,6):
                print("type the name of the team member of team 3 members: ",a)
                name3=input()
                name_team3.append(name3)

       
            for a in range(1,6):
                print("type the name of the team member of team 4 members: ",a)
                name4=input()
                name_team4.append(name4)

            for a in range(0,4):
                print("type the name of the teams in order that came 1st,2nd,3rd and 4th in the 1st event")
                print("teamnames are t1,t2,t3,t4")
                order1=input()
                e1_order.append(order1)

        if e1_order[0]=='t1':
                Team1=Team1+point_event_first
        elif e1_order[1]=='t1':
                Team1=Team1+point_event_second
        elif e1_order[2]=='t1':
                Team1=Team1+point_event_third
        else:
                Team1=Team1+point_event_fourth

        if e1_order[0]=='t2':
                Team2=Team2+point_event_first
        elif e1_order[1]=='t2':
                Team2=Team2+point_event_second
        elif e1_order[2]=='t2':
                Team2=Team2+point_event_third
        else:
                    Team2=Team2+point_event_fourth

        if e1_order[0]=='t3':
                Team3=Team3+point_event_first
        elif e1_order[1]=='t3':
                Team3=Team3+point_event_second
        elif e1_order[2]=='t3':
                Team3=Team3+point_event_third
        else:
                Team3=Team3+point_event_fourth

        if e1_order[0]=='t4':
                Team4=Team4+point_event_first
        elif e1_order[1]=='t4':
                Team4=Team4+point_event_second
        elif e1_order[2]=='t4':
                Team4=Team4+point_event_third
        else:
                Team4=Team4+point_event_fourth

        for x in range(0,4):
            print("type the name of the teams in order that came 1st,2nd,3rd and 4th in the 2st event")
            print("teamnames are t1,t2,t3,t4")
            order2=input()
            e2_order.append(order2)

        if e2_order[0]=='t1':
            Team1=Team1+point_event_first
        elif e2_order[1]=='t1':
            Team1=Team1+point_event_second
        elif e2_order[2]=='t1':
            Team1=Team1+point_event_third
        else:
            Team1=Team1+point_event_fourth

        if e2_order[0]=='t2':
            Team2=Team2+point_event_first
        elif e2_order[1]=='t2':
            Team2=Team2+point_event_second
        elif e2_order[2]=='t2':
            Team2=Team2+point_event_third
        else:
            Team2=Team2+point_event_fourth

        if e2_order[0]=='t3':
            Team3=Team3+point_event_first
        elif e2_order[1]=='t3':
            Team3=Team3+point_event_second
        elif e2_order[2]=='t3':
            Team3=Team3+point_event_third
        else:
            Team3=Team3+point_event_fourth

        if e2_order[0]=='t4':
            Team4=Team4+point_event_first
        elif e2_order[1]=='t4':
            Team4=Team4+point_event_second
        elif e2_order[2]=='t4':
            Team4=Team4+point_event_third
        else:
            Team4=Team4+point_event_fourth

        
        for x in range(0,4):
            print("type the name of the teams in order that came 1st,2nd,3rd and 4th in the 2st event")
            print("teamnames are t1,t2,t3,t4")
            order3=input()
            e3_order.append(order3)

        if e3_order[0]=='t1':
            Team1=Team1+point_event_first
        elif e3_order[1]=='t1':
            Team1=Team1+point_event_second
        elif e3_order[2]=='t1':
            Team1=Team1+point_event_third
        else:
            Team1=Team1+point_event_fourth

        if e3_order[0]=='t2':
            Team2=Team2+point_event_first
        elif e3_order[1]=='t2':
            Team2=Team2+point_event_second
        elif e3_order[2]=='t2':
            Team2=Team2+point_event_third
        else:
            Team2=Team2+point_event_fourth

        if e3_order[0]=='t3':
            Team3=Team3+point_event_first
        elif e3_order[1]=='t3':
            Team3=Team3+point_event_second
        elif e3_order[2]=='t3':
            Team3=Team3+point_event_third
        else:
            Team3=Team3+point_event_fourth

        if e3_order[0]=='t4':
            Team4=Team4+point_event_first
        elif e3_order[1]=='t4':
            Team4=Team4+point_event_second
        elif e3_order[2]=='t4':
            Team4=Team4+point_event_third
        else:
            Team4=Team4+point_event_fourth

        for x in range(0,4):
            print("type the name of the teams in order that came 1st,2nd,3rd and 4th in the 2st event")
            print("teamnames are t1,t2,t3,t4")
            order4=input()
            e4_order.append(order4)

        if e4_order[0]=='t1':
            Team1=Team1+point_event_first
        elif e4_order[1]=='t1':
            Team1=Team1+point_event_second
        elif e4_order[2]=='t1':
            Team1=Team1+point_event_third
        else:
            Team1=Team1+point_event_fourth

        if e4_order[0]=='t2':
            Team2=Team2+point_event_first
        elif e4_order[1]=='t2':
            Team2=Team2+point_event_second
        elif e4_order[2]=='t2':
            Team2=Team2+point_event_third
        else:
            Team2=Team2+point_event_fourth

        if e4_order[0]=='t3':
            Team3=Team3+point_event_first
        elif e4_order[1]=='t3':
            Team3=Team3+point_event_second
        elif e4_order[2]=='t3':
            Team3=Team3+point_event_third
        else:
            Team3=Team3+point_event_fourth

        if e4_order[0]=='t4':
            Team4=Team4+point_event_first
        elif e4_order[1]=='t4':
            Team4=Team4+point_event_second
        elif e4_order[2]=='t4':
            Team4=Team4+point_event_third
        else:
            Team4=Team4+point_event_fourth

        opt1=str(input("To Add More press Enter to Quit Press Q: "))
    
        if opt=="Q":
            break
