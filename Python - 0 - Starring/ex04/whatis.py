import sys

def check_int(av, ac):
    if ac == 1:
        try:
            av_int = int(av)
            if av_int % 2 == 0:
                print("I'm Even")
            elif av_int % 2 != 0:
                print("I'm Odd")
            elif av_int=="":
                print("") 
        except ValueError:
            print("AssertionError: argument is not an integer")
    elif ac < 1:
        print("")
    else:
        print("AssertionError: more than one argument is provided")

if __name__ == "__main__":
    ac = len(sys.argv) - 1
    av = sys.argv[1] if ac > 0 else None
    check_int(av, ac)
