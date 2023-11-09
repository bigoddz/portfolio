name_solo=[]#creating a list
squadnames=["t1","t2","t3","t4"]

name_squad1=[]
name_squad2=[]
name_squad3=[]
name_squad4=[]

event1=[]
event2=[]
event3=[]
event4=[]

e1_order=[]
e2_order=[]
e3_order=[]
e4_order=[]

score_event_first=10
score_event_second=8
score_event_third=6
score_event_fourth=4

squad1=0
squad2=0
squad3=0
squad4=0

name_solo_score=0

print("Welcome to the NAYTHEN")

print("In this tournament there will be up to 20 invdividuals participating")

print("There could be 4 squads with 5 group members")

print("The events that are available in this tournament are Music, Automobiles and Technology")

print("An solo or a squad will need at least 95 out of 100 score to be 1st")

print("An solo gets 5+ extra for each question")

print("The 2nd place will be the 1st place minus 5 score and the same for 3rd place etc")


while True:
        squadorind=str(input("press T for squad or I for solo competition: ")).upper()
        if squadorind=="I":
            for a in range(1,21):
                print("type the name of the solo: ",a)
                name=input()
                name_solo.append(name)

            for a in range(0,4):
                    print("type the name of the solo in order that came 1st,2nd,3rd and 4th in the 1st event")
                    order1=input()
                    e1_order.append(order1)

            if e1_order[0]=='name_solo_0':
                    name_solo=name_solo_score+score_event_first
            elif e1_order[1]=='name_solo_1':
                    name_solo=name_solo_score+score_event_second
            elif e1_order[2]=='name_solo_2':
                    name_solo=name_solo_score+score_event_third
            else:
                    name_solo=name_solo_score+score_event_fourth

            for a in range(0,4):
                    print("type the name of the solo in order that came 1st,2nd,3rd and 4th in the 2nd event")
                    order1=input()
                    e2_order.append(order1)

            if e2_order[0]=='name_solo_0':
                    name_solo=name_solo_score+score_event_first
            elif e2_order[1]=='name_solo_1':
                    name_solo=name_solo_score+score_event_second
            elif e2_order[2]=='name_solo_2':
                    name_solo=name_solo_score+score_event_third
            else:
                    name_solo=name_solo_score+score_event_fourth

            for a in range(0,4):
                    print("type the name of the solo in order that came 1st,2nd,3rd and 4th in the 3rd event")
                    order3=input()
                    e3_order.append(order1)


            if e3_order[0]=='name_solo_0':
                    name_solo=name_solo_score+score_event_first
            elif e3_order[1]=='name_solo_1':
                    name_solo=name_solo_score+score_event_second
            elif e3_order[2]=='name_solo_2':
                    name_solo=name_solo_score+score_event_third
            else:
                    name_solo=name_solo_score+score_event_fourth

            for a in range(0,4):
                    print("type the name of the solo in order that came 1st,2nd,3rd and 4th in the 4th event")
                    order4=input()
                    e4_order.append(order1)

            if e4_order[0]=='name_solo_0':
                    name_solo=name_solo_score+score_event_first
            elif e4_order[1]=='name_solo_1':
                    name_solo=name_solo_score+score_event_second
            elif e4_order[2]=='name_solo_2':
                    name_solo=name_solo_score+score_event_third
            else:
                    name_solo=name_solo_score+score_event_fourth

            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)
            print("the solo Scored: ",name_solo)


        elif squadorind=="T": #naming squads
            
                for a in range(1,6):
                    print("type the name of the squad member of squad 1 members: ",a)
                    name1=input()
                    name_squad1.append(name1)

                for a in range(1,6):
                    print("type the name of the squad member of squad 2 members: ",a)
                    name2=input()
                    name_squad2.append(name2)

                for a in range(1,6):
                    print("type the name of the squad member of squad 3 members: ",a)
                    name3=input()
                    name_squad3.append(name3)

           
                for a in range(1,6):
                    print("type the name of the squad member of squad 4 members: ",a)
                    name4=input()
                    name_squad4.append(name4)

                for a in range(0,4):
                    print("type the name of the squads in order that came 1st,2nd,3rd and 4th in the 1st event") #ranking for squads
                    print("squadnames are t1,t2,t3,t4")
                    order1=input()
                    e1_order.append(order1)
                    

                if e1_order[0]=='t1':
                            squad1=squad1+score_event_first
                elif e1_order[1]=='t1':
                        squad1=squad1+score_event_second
                elif e1_order[2]=='t1':
                        squad1=squad1+score_event_third
                else:
                        squad1=squad1+score_event_fourth

                if e1_order[0]=='t2':
                        squad2=squad2+score_event_first
                elif e1_order[1]=='t2':
                        squad2=squad2+score_event_second
                elif e1_order[2]=='t2':
                        squad2=squad2+score_event_third
                else:
                        squad2=squad2+score_event_fourth

                if e1_order[0]=='t3':
                        squad3=squad3+score_event_first
                elif e1_order[1]=='t3':
                        squad3=squad3+score_event_second
                elif e1_order[2]=='t3':
                        squad3=squad3+score_event_third
                else:
                        squad3=squad3+score_event_fourth

                if e1_order[0]=='t4':
                        squad4=squad4+score_event_first
                elif e1_order[1]=='t4':
                        squad4=squad4+score_event_second
                elif e1_order[2]=='t4':
                        squad4=squad4+score_event_third
                else:
                        squad4=squad4+score_event_fourth

                for x in range(0,4):
                    print("type the name of the squads in order that came 1st,2nd,3rd and 4th in the 2nd event") #ranking for squads
                    print("squadnames are t1,t2,t3,t4")
                    order2=input()
                    e2_order.append(order2)

                if e2_order[0]=='t1':
                    squad1=squad1+score_event_first
                elif e2_order[1]=='t1':
                    squad1=squad1+score_event_second
                elif e2_order[2]=='t1':
                    squad1=squad1+score_event_third
                else:
                    squad1=squad1+score_event_fourth

                if e2_order[0]=='t2':
                    squad2=squad2+score_event_first
                elif e2_order[1]=='t2':
                    squad2=squad2+score_event_second
                elif e2_order[2]=='t2':
                    squad2=squad2+score_event_third
                else:
                    squad2=squad2+score_event_fourth

                if e2_order[0]=='t3':
                    squad3=squad3+score_event_first
                elif e2_order[1]=='t3':
                    squad3=squad3+score_event_second
                elif e2_order[2]=='t3':
                    squad3=squad3+score_event_third
                else:
                    squad3=squad3+score_event_fourth

                if e2_order[0]=='t4':
                    squad4=squad4+score_event_first
                elif e2_order[1]=='t4':
                    squad4=squad4+score_event_second
                elif e2_order[2]=='t4':
                    squad4=squad4+score_event_third
                else:
                    squad4=squad4+score_event_fourth

                
                for x in range(0,4):
                    print("type the name of the squads in order that came 1st,2nd,3rd and 4th in the 3rd event") #ranking for squads
                    print("squadnames are t1,t2,t3,t4")
                    order3=input()
                    e3_order.append(order3)

                if e3_order[0]=='t1':
                    squad1=squad1+score_event_first
                elif e3_order[1]=='t1':
                    squad1=squad1+score_event_second
                elif e3_order[2]=='t1':
                    squad1=squad1+score_event_third
                else:
                    squad1=squad1+score_event_fourth

                if e3_order[0]=='t2':
                    squad2=squad2+score_event_first
                elif e3_order[1]=='t2':
                    squad2=squad2+score_event_second
                elif e3_order[2]=='t2':
                    squad2=squad2+score_event_third
                else:
                    squad2=squad2+score_event_fourth

                if e3_order[0]=='t3':
                    squad3=squad3+score_event_first
                elif e3_order[1]=='t3':
                    squad3=squad3+score_event_second
                elif e3_order[2]=='t3':
                    squad3=squad3+score_event_third
                else:
                    squad3=squad3+score_event_fourth

                if e3_order[0]=='t4':
                    squad4=squad4+score_event_first
                elif e3_order[1]=='t4':
                    squad4=squad4+score_event_second
                elif e3_order[2]=='t4':
                    squad4=squad4+score_event_third
                else:
                    squad4=squad4+score_event_fourth

                for x in range(0,4):
                    print("type the name of the squads in order that came 1st,2nd,3rd and 4th in the 4th event") #ranking for squads
                    print("squadnames are t1,t2,t3,t4")
                    order4=input()
                    e4_order.append(order4)

                if e4_order[0]=='t1':
                    squad1=squad1+score_event_first
                elif e4_order[1]=='t1':
                    squad1=squad1+score_event_second
                elif e4_order[2]=='t1':
                    squad1=squad1+score_event_third
                else:
                    squad1=squad1+score_event_fourth

                if e4_order[0]=='t2':
                    squad2=squad2+score_event_first
                elif e4_order[1]=='t2':
                    squad2=squad2+score_event_second
                elif e4_order[2]=='t2':
                    squad2=squad2+score_event_third
                else:
                    squad2=squad2+score_event_fourth

                if e4_order[0]=='t3':
                    squad3=squad3+score_event_first
                elif e4_order[1]=='t3':
                    squad3=squad3+score_event_second
                elif e4_order[2]=='t3':
                    squad3=squad3+score_event_third
                else:
                    squad3=squad3+score_event_fourth

                if e4_order[0]=='t4':
                    squad4=squad4+score_event_first
                elif e4_order[1]=='t4':
                    squad4=squad4+score_event_second
                elif e4_order[2]=='t4':
                    squad4=squad4+score_event_third
                else:
                    squad4=squad4+score_event_fourth

                print("squad 1 has Scored: ",squad1)
                print("squad 2 has Scored: ",squad2)
                print("squad 3 has Scored: ",squad3)
                print("squad 4 has Scored: ",squad4)



        else:
            print("Incorrect Input, Try Again!")
            continue



        opt=str(input("To Add More press Enter to Quit Press Q: ")).upper()
        if opt=="Q":
            break



   


