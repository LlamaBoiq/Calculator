def math():
    methods = {
        "+" : f"{e1inp + e2inp}",
        "-" : f"{e1inp - e2inp}",
        "*" : f"{e1inp * e2inp}",   # Switch case to make life ez
        "/" : f"{e1inp / e2inp}",
        "%" : f"{e1inp % e2inp}"
    }
    output = methods.get(meinp, "Enter right method pleb")
    return output

def main():
    global e1inp, e2inp, meinp 

    try:
        e1inp = float(input("Enter First Number: "))
        meinp = input("Enter Method: ")
        e2inp = float(input("Enter Second Number: "))
    except ValueError:
        print("Enter correct thing")
        return
    if e1inp == 0 and e2inp == 0:
        print("you cant divide 0 by 0 :(")  # for some reason didnt work when i tried excepting the error
        return
    answer = math()
    if str(answer).endswith(".0"):
        print("".join(answer[0:-2]))
    else:
        print("".join(answer))


if __name__ == '__main__':
    while True:
        main() # <<<<<--------         runs program
     #  ^^^^^^^^
     #  |||||||| 
     #  |||||||| 
     #  |||||||| 
        # runs program if it isnt obvious
