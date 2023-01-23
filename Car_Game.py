car_command=""

command=input("Press Help to start the game command ")

started=False
if command.upper()=="HELP":
    print("""Press Start to Start the car
            Press Stop to Stop the car
            Press Quit to Exit the game""")
    while car_command.lower() !="quit":
        car_command=input("> ")
        if car_command.upper()=="START":
            print("Car started!! Ready to move......")
            if started==True:
                print("car already started!")
            started=True
        elif car_command.upper()=="STOP":
            print("car Stopped!!")
        # else:
        #     print("Plese Enter a valid Command!!")
    else:
        print("Game Over!")

else:
    print("Wrong Command received!!")
        