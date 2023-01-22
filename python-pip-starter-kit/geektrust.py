from sys import argv
from src.trains1 import TrainJourney1

def main():
    
    """
    Sample code to read inputs from the file

    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    Lines = f.readlines()
    //Add your code here to process the input commands
    """
    f=open('textfile.txt','r')
    TrainA:list=list(f.readline().split(' '))
    TrainB:list=list(f.readline().split(' '))
    TrainAB:list=[]
    train_journey=TrainJourney1()

    TrainA,TrainB,TrainAB=train_journey.get_trains_information(TrainA[2:],TrainB[2:])
    TrainA.insert(0,"ENGINE")
    TrainA.insert(0,"Train_A")
    TrainA.insert(0,"ARRIVAL")
    TrainB.insert(0,"ENGINE")
    TrainB.insert(0,"Train_A")
    TrainB.insert(0,"ARRIVAL")
    TrainAB.insert(0,"ENGINE")
    TrainAB.insert(0,"ENGINE")
    TrainAB.insert(0,"Train_AB")
    TrainAB.insert(0,"DEPARTURE")
    k=0
    for i in TrainA:
        if k==0:
            print(i,end="   ")
        else:
            print(i,end=" ")
    k=0
    for i in TrainB:
        if k==0:
            print(i,end="   ")
        else:
            print(i,end=" ")
    k=0
    for i in TrainAB:
        if k==0:
            print(i,end="   ")
        else:
            print(i,end=" ")


    

    
    
if __name__ == "__main__":
    main()