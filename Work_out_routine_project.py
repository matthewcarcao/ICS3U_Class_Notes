import random, time
correct = 0
done = 0
while correct==0:
    print("Welcome to your Fitness routine. This software is meant to be used once to make a routine.\nIf you have changed in age, height, weight or anything else please come back to this program later on.\nTo begin, we will need you to answer a few simple questions.")
    time.sleep(4)
    name=(input("What is your name?"))
    time.sleep(0.1)
    age=int(input("How old are you?"))
    time.sleep(0.1)
    loop=0
    while loop==0:
        height=str(input("How tall are you in feet? Write it out like so: #'#"))
        if "\'" not in height or"\"" in height:
            print("Please print the height in the proper format.")
        else:
            loop=1
    time.sleep(0.1)
    weight=int(input("How much do you weigh in pounds?"))
    time.sleep(0.1)
    print("If you would like to focus on muscles in your arms press 1\nIf you would like to focus on muscles in your legs press 2\nIf you would like to focus on muscles in your abs press 3\nIf you would like to focus on arms, legs, and abs press 4\n")
    muscle_group=int(input(" "))
    print("Your basic questions are done for now. Thank you!")
    difficulty=0
    print("What are using this program for?")
    usage=int(input("If you are using this program to get in shape press 1\nIf you are using this program to get fit press 2\nIf you are using this program to get toned press 3\nIf you are using this program to get yolked press 4\nIf you are not in the shape of the previous group, please use that program instead."))
    if usage==1:
        difficulty=1
        print("Nice, this may take a while depending on how out of shape you are.\nDon't be discouraged, every journey needs to start somewhere!")
    if usage==2:
        difficulty=2
        print("Sounds good, say goodbye to your flabby arms and legs, and prepare for a flat stomach and firm muscles")
    if usage==3:
        difficulty=3
        print("Alrighty, some good defenition for a nice beach bod.")
    if usage==4:
        difficulty=4
        print("Right on, some strength that will make your muscles huge.")
    print("Your name is",name)
    print("You are",age,"years old")
    print("You are",height,"feet tall")
    print("You weigh",weight,"pounds")
    height = height.split('\'')
    height = (int(height[0])*12)+int(height[1])

    if difficulty==1:
        print("You are using this program to get in shape")
    elif difficulty==2:
        print("You are using this program to get fit")
    elif difficulty==3:
        print("You are using this program to get toned")
    elif difficulty==4:
        print("You are using this program to get yolked")
    if muscle_group==1:
        print("You are using this program to build arm muscles")
    elif muscle_group==2:
        print("You are using this program to build leg muscles")
    elif muscle_group==3:
        print("You are using this program to build ab muscles")
    elif muscle_group==4:
        print("You are using this program to build leg, arm, and ab muscles")
    correct=int(input("If this is correct press 1\nIf it is not correct press 0"))
    if correct==1:
        print("Perfect, let's get started")
import math
intensity = int(math.fmod((703*int(weight)/(height))*(703*int(weight)/(height)), 31))
if muscle_group==1 and difficulty==1:
    random=(random.randint(1,3))
    workout_repeat=0
    while workout_repeat==0:
        if random==1:
            print("Lets start with "+str(int(intensity))+" push ups")
            done=int(input("Click 1 when you are done"))
            if done==1:print("Next a  "+str(intensity)+" punches")
                done=0
                done = int(input("Click 1 when you are done"))
                if done==1:print ("Finally  "+str(intensity)+" shoulder taps")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
                        workout_repeat=1
        elif random==2:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with  "+str(intensity)+" tricep dips")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity)+" arm circles")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally  "+str(intensity)+" triangle push ups")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
        elif random==3:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with  "+str(intensity)+" uppercut punches")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity)+" seconds of plank")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally  "+str(intensity)+" spiderman push ups")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1

elif muscle_group==1 and difficulty==2:
    random=(random.randint(1,3))
    workout_repeat=0
    while workout_repeat==0:
        if random==1:
            print("Lets start with"+int(intensity+ 10)+" push ups")
            done=int(input("Click 1 when you are done"))
            if done==1:if done==1:print("Next a  "+str(intensity+ 10)+" punches")
                done=0
                done = int(input("Click 1 when you are done"))
                if done==1:print ("Finally  "+str(intensity+ 10)+" shoulder taps")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:
                        print ("Thank you for using this workout program. You are on track towards your goal.")
                        workout_repeat=1
        elif random==2:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with  "+str(intensity+ 10)+" tricep dips")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity+ 10)+" arm circles")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally  "+str(intensity+ 10)+" triangle push ups")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
        elif random==3:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with  "+str(intensity+ 10)+" uppercut punches")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity+ 10)+" seconds of plank")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally  "+str(intensity+ 10)+" spiderman push ups")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
elif muscle_group==1 and difficulty==3:
    random=(random.randint(1,3))
    workout_repeat=0
    while workout_repeat==0:
        if random==1:
            print("Lets start with  "+str(intensity+ 20)+" push ups")
            done=int(input("Click 1 when you are done"))
            if done==1:print("Next a  "+str(intensity+ 20)+" punches")
                done=0
                done = int(input("Click 1 when you are done"))
                if done==1:print ("Finally  "+str(intensity+ 20)+" shoulder taps")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
                        workout_repeat=1
        elif random==2:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with "+str(intensity+ 20)+" tricep dips")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity+ 20)+" arm circles")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally "+str(intensity+ 20)+" triangle push ups")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:

    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
        elif random==3:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with "+str(intensity+ 20)+" uppercut punches")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a "+str(intensity+ 20)+" seconds of plank")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally "+str(intensity+ 20)+" spiderman push ups")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
elif muscle_group==1 and difficulty==4:
    random=(random.randint(1,3))
    workout_repeat=0
    while workout_repeat==0:
        if random==1:
            print("Lets start with  "+str(intensity+ 30)+" push ups")
            done=int(input("Click 1 when you are done"))
            if done==1:print("Next a  "+str(intensity+ 30)+" punches")
                done=0
                done = int(input("Click 1 when you are done"))
                if done==1:print ("Finally  "+str(intensity+ 30)+" shoulder taps")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
                        workout_repeat=1
        elif random==2:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with "+str(intensity+ 30)+" tricep dips")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity+ 30)+" arm circles")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally "+str(intensity+ 30)+" triangle push ups")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
        elif random==3:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with "+str(intensity+ 30)+" uppercut punches")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a "+str(intensity+ 30)+" seconds of plank")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally "+str(intensity+ 30)+" spiderman push ups")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
if muscle_group==2 and difficulty==1:
    random=(random.randint(1,3))
    workout_repeat=0
    while workout_repeat==0:
        if random==1:
            print("Lets start with "+str(int(intensity))+" deep squats")
            done=int(input("Click 1 when you are done"))
            if done==1:print("Next a  "+str(intensity)+" second wall sit")
                done=0
                done = int(input("Click 1 when you are done"))
                if done==1:print ("Finally  "+str(intensity)+" side lunges")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
                        workout_repeat=1
        elif random==2:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with  "+str(intensity)+" side leg lifts")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity)+" lunges")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally  "+str(intensity)+" side leg raises")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
        elif random==3:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with  "+str(intensity)+" step ups")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity)+" calf raises")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally  "+str(intensity)+" sumo squats")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
elif muscle_group==2 and difficulty==2:
    random=(random.randint(1,3))
    workout_repeat=0
    while workout_repeat==0:
        if random==1:
            print("Lets start with"+int(intensity)+10+" deep squats")
            done=int(input("Click 1 when you are done"))
            if done==1:print("Next a  "+str(intensity+ 10)+" second wall sit")
                done=0
                done = int(input("Click 1 when you are done"))
                if done==1:print ("Finally  "+str(intensity+ 10)+" side lunges")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
                        workout_repeat=1
        elif random==2:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with  "+str(intensity+ 10)+" side leg lifts")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity+ 10)+" lunges")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally  "+str(intensity+ 10)+" side leg raises")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
        elif random==3:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with  "+str(intensity+ 10)+" step ups")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity+ 10)+" calf raises")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally  "+str(intensity+ 10)+" sumo squats")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
elif muscle_group==2 and difficulty==3:
    random=(random.randint(1,3))
    workout_repeat=0
    while workout_repeat==0:
        if random==1:
            print("Lets start with  "+str(intensity+ 20)+" deep squats")
            done=int(input("Click 1 when you are done"))
            if done==1:print("Next a  "+str(intensity+ 20)+" second wall sit")
                done=0
                done = int(input("Click 1 when you are done"))
                if done==1:print ("Finally  "+str(intensity+ 20)+" side lunges")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
        elif random==2:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with "+str(intensity+ 20)+" side leg lifts")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity+ 20)+" lunges")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally "+str(intensity+ 20)+" side leg raises")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
        elif random==3:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with "+str(intensity+ 20)+" step ups")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a "+str(intensity+ 20)+" calf raises")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally "+str(intensity+ 20)+" sumo squats")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")

elif muscle_group==2 and difficulty==4:
    random=(random.randint(1,3))
    workout_repeat=0
    while workout_repeat==0:
        if random==1:
            print("Lets start with  "+str(intensity+ 30)+" deep squats")
            done=int(input("Click 1 when you are done"))
            if done==1:print("Next a  "+str(intensity+ 30)+" second wall sit")
                done=0
                done = int(input("Click 1 when you are done"))
                if done==1:print ("Finally  "+str(intensity+ 30)+" side lunges")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
        elif random==2:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with "+str(intensity+ 30)+" side leg lifts")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity+ 30)+" lunges")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally "+str(intensity+ 30)+" side leg raises")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
        elif random==3:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with "+str(intensity+ 30)+" step ups")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a "+str(intensity+ 30)+" calf raises")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally "+str(intensity+ 30)+" sumo squats")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
if muscle_group==3 and difficulty==1:
    random=(random.randint(1,3))
    workout_repeat=0
    while workout_repeat==0:
        if random==1:
            print("Lets start with "+str(int(intensity))+" sit ups")
            done=int(input("Click 1 when you are done"))
            if done==1:print("Next a  "+str(intensity)+" seconds of plank")
                done=0
                done = int(input("Click 1 when you are done"))
                if done==1:print ("Finally  "+str(intensity)+" mountain climbers")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
                        workout_repeat=1
        elif random==2:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with  "+str(intensity)+" v-sits")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity)+" knee to chest")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally  "+str(intensity)+" sitting twists")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
        elif random==3:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with  "+str(intensity)+" crunches")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity)+" flutter kicks")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally  "+str(intensity)+" scissors")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
                            workout_repeat=1
elif muscle_group==3 and difficulty==2:
    random=(random.randint(1,3))
    workout_repeat=0
    while workout_repeat==0:
        if random==1:
            print("Lets start with"+int(intensity)+10+" sit ups")
            done=int(input("Click 1 when you are done"))
            if done==1:print("Next a  "+str(intensity+ 10)+" seconds of plank")
                done=0
                done = int(input("Click 1 when you are done"))
                if done==1:print ("Finally  "+str(intensity+ 10)+" mountain climbers")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
                        workout_repeat=1
        elif random==2:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with  "+str(intensity+ 10)+" crunches")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity+ 10)+" flutter kicks")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally  "+str(intensity+ 10)+" scissors")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
        elif random==3:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with  "+str(intensity+ 10)+" v-sits")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity+ 10)+" knee to chest")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally  "+str(intensity+ 10)+" sitting twists")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
elif muscle_group==3 and difficulty==3:
    random=(random.randint(1,3))
    workout_repeat=0
    while workout_repeat==0:
        if random==1:
            print("Lets start with  "+str(intensity+ 20)+" sit ups")
            done=int(input("Click 1 when you are done"))
            if done==1:print("Next a  "+str(intensity+ 20)+" seconds of plank")
                done=0
                done = int(input("Click 1 when you are done"))
                if done==1:print ("Finally  "+str(intensity+ 20)+" mountain climbers")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
                        workout_repeat=1
        elif random==2:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with "+str(intensity+ 20)+" v-sits")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity+ 20)+" knee to chest")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally "+str(intensity+ 20)+" sitting twists")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
        elif random==3:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with "+str(intensity+ 20)+" crunches")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a "+str(intensity+ 20)+" flutter kicks")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally "+str(intensity+ 20)+" scissors")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
elif muscle_group==4 and difficulty==4:
    random=(random.randint(1,3))
    workout_repeat=0
    while workout_repeat==0:
        if random==1:
            print("Lets start with  "+str(intensity+ 30)+" sit ups")
            done=int(input("Click 1 when you are done"))
            if done==1:print("Next a  "+str(intensity+ 30)+" seconds of plank")
                done=0
                done = int(input("Click 1 when you are done"))
                if done==1:print ("Finally  "+str(intensity+ 30)+" mountain climbers")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
                        workout_repeat=1
        elif random==2:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with "+str(intensity+ 30)+" v-sits")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity+ 30)+" knee to chest")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally "+str(intensity+ 30)+" sitting twists")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
        elif random==3:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with "+str(intensity+ 30)+" crunches")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a "+str(intensity+ 30)+" flutter kicks")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally "+str(intensity+ 30)+" scissors")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
if muscle_group==4 and difficulty==1:
    random=(random.randint(1,3))
    workout_repeat=0
    while workout_repeat==0:
        if random==1:
            print("Lets start with "+str(int(intensity))+" push ups")
            done=int(input("Click 1 when you are done"))
            if done==1:print("Next a  "+str(intensity)+" squats")
                done=0
                done = int(input("Click 1 when you are done"))
                if done==1:print ("Finally  "+str(intensity)+" sit ups")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
                        workout_repeat=1
        elif random==2:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with  "+str(intensity)+" punches")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity)+" lunges")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally  "+str(intensity)+" crunches")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
        elif random==3:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with  "+str(intensity)+" step ups")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity)+" tricep dips")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally  "+str(intensity)+" knee to chest")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
                        workout_repeat=1
elif muscle_group==4 and difficulty==2:
    random=(random.randint(1,3))
    workout_repeat=0
    while workout_repeat==0:
        if random==1:
            print("Lets start with"+int(intensity)+10+" push ups")
            done=int(input("Click 1 when you are done"))
            if done==1:print("Next a  "+str(intensity+ 10)+" squats")
                done=0
                done = int(input("Click 1 when you are done"))
                if done==1:print ("Finally  "+str(intensity+ 10)+" sit ups")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
                        workout_repeat=1
        elif random==2:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with  "+str(intensity+ 10)+" punches")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity+ 10)+" lunges")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally  "+str(intensity+ 10)+" crunches")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
        elif random==3:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with  "+str(intensity+ 10)+" step ups")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity+ 10)+" tricep dips")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally  "+str(intensity+ 10)+" knee to chest")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
elif muscle_group==4 and difficulty==3:
    random=(random.randint(1,3))
    workout_repeat=0
    while workout_repeat==0:
        if random==1:
            print("Lets start with  "+str(intensity+ 20)+" push ups")
            done=int(input("Click 1 when you are done"))
            if done==1:print("Next a  "+str(intensity+ 20)+" squats")
                done=0
                done = int(input("Click 1 when you are done"))
                if done==1:print ("Finally  "+str(intensity+ 20)+" sit ups")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
                        workout_repeat=1
        elif random==2:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with "+str(intensity+ 20)+" punches")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity+ 20)+" lunges")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally "+str(intensity+ 20)+" crunches")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
        elif random==3:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with "+str(intensity+ 20)+" step ups")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a "+str(intensity+ 20)+" tricep dips")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally "+str(intensity+ 20)+" knee to chest")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
elif muscle_group==4 and difficulty==4:
    random=(random.randint(1,3))
    workout_repeat=0
    while workout_repeat==0:
        if random==1:
            print("Lets start with  "+str(intensity+ 30)+" push ups")
            done=int(input("Click 1 when you are done"))
            if done==1:print("Next a  "+str(intensity+ 30)+" sit ups")
                done=0
                done = int(input("Click 1 when you are done"))
                if done==1:print ("Finally  "+str(intensity+ 30)+" squats")
                    done=0
                    done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                    if done==1:print ("Thank you for using this workout program. You are on track towards your goal.")
                        workout_repeat=1
        elif random==2:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with "+str(intensity+ 30)+" punches")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a  "+str(intensity+ 30)+" lunges")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally "+str(intensity+ 30)+" crunches")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1
        elif random==3:
            workout_repeat = 0
            while workout_repeat == 0:
                print("Lets start with "+str(intensity+ 30)+" step ups")
                done=int(input("Click 1 when you are done"))
                if done==1:print("Next a "+str(intensity+ 30)+" tricep dips")
                    done=0
                    done = int(input("Click 1 when you are done"))
                    if done==1:print ("Finally "+str(intensity+ 30)+" knee to chest")
                        done=0
                        done = int(input("Click 1 when you are done or 0 if you would like to repeat for more reps."))
                        if done==1:if done==1:
    print ("Thank you for using this workout program. You are on track towards your goal.")
    workout_repeat = 1