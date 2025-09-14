import sys


#add dog functionality 


def cat():
    print("miaww")
def dog ():
    print("woof woof")
def default():
    print("This is the default function.")


def main():
    if sys.argv[1]=="cat":
        cat()
    else if sys.argvb[2]=="dog":
        dog()
    else:
        default()
      
    

if __name__ == "__main__":
    main()
