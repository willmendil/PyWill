
def inputConf(msg):
    userValue = None
    while 1:
        userValue = input(f"{msg}: ")
        check = input("Are you sure ? (Y/n)")
        if check.lower() == "y":
            return userValue


if __name__ == "__main__":
    t = inputConf("Test input")
    print(t)