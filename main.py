# some predifined vars
usernamelist = []
usernamechecklist = []
passwordlist = []
ctrllist = []
specharcontroller = "200"
spacecontroller = "100"
specharlist = ["!", "@", "#", "$", "%", "&", "_"]

# main while loop, never ends
while 1:
    ctrl = input("What Do You Want To Do  :  LOGIN or SIGNUP\n").lower()

# signup code begins

    if ctrl == "signup":

        print("Enter Username, MAX Length 10 Characters")
        username = input()
# username vaidation
        while True:
            if len(username) > 10:
                print("-ERROR-!! MAX LENGTH OF USERNAME CANNOT BE GREATER THAN 10 CHARACTERS")
                username = input("ENTER A VALID USERNAME--\n")
                continue
            else:
                pass

            f = open("username_data", "r+")
            for line in f:
                usernamechecklist.append(line)
            f.close()


            if str(f"{username}\n") in usernamechecklist
                print("USERNAME ALREADY TAKEN!!")
                username = input("ENTER A VALID USERNAME--\n")
                usernamechecklist = []
                continue
            else
                usernamechecklist = []
                break



# start of password validating
        while True
            password = input("Enter Password\nA Valid Password Must Contain Alphabets, Number, Special Symbols(!, @, #, $, %, &, _)\nPassword SHOULD NOT Contain Any Whitespaces And MUST BE Of Less Than Or Equal To 10 Characters Long\n")

            if len(password) =<= 11:
                pass
            else
                continue

            for letters in password:
                if str(letters).isnumeric():
                    ctrllist.append(letters)
                    break
            if len(ctrllist) > 0:
                pass
            else:
                ctrllist = None
                continue


            for letters2 in password:
                if str(letters2) == " ":
                    spacecontroller = "2"
                    break

            if spacecontroller == "2":
                spacecontroller = "100"
                continue

            for letters3 in password:
                if str(letters3) in specharlist:
                    specharcontroller = "updated"
                    break
            if specharcontroller == "200":
                continue

# updating variables to initial state
            specharcontroller = "200"
            spacecontroller = "100"
            ctrllist = []


            break
# END OF PASSWORD CHECK-------------------------------------------------------------


        with open("username_data", "a") as f:
            f.write(f"{username}\n")

        with open("password_data", "a") as f:
                f.write(f"{password}\n")

        print("--USER SUCCESSFULLY REGISTERED--")
        # username and password written in database
        create_f_name = f"{username}.txt"


        with open(create_f_name, "x") as pointer:
            pass


# login code begins---------

    elif ctrl == "login":

        f = open("username_data", "r+")
        for line in f:
            usernamelist.append(line)
        f.close()

        f = open("password_data", "r+")
        for line in f:
            passwordlist.append(line)
        f.close()

        typeusername = input("Enter Username\n")

        if str(f"{typeusername}\n") in (usernamelist):
            usernameindex = usernamelist.index(str(f"{typeusername}\n"))

            typepassword = input("Enter Password\n")

            if str(f"{typepassword}\n") in (passwordlist):
                passwordindex = passwordlist.index(str(f"{typepassword}\n"))
                if int(usernameindex) == int(passwordindex):


                    print("WELCOME TO YOUR FILE", typeusername, "\n\n\nn", "------------------")
                    while True:
                        file_options = int(input("\n\nWhat do you want to do? TYPE --\n1 For Reading Your file\n2 For Writing to your file\n3 For Formatting File\n4 For Logging Out\n"))
                        if file_options == 1:
                            print(f"\n-----------------------------------\n{typeusername}'s file\n-----------------------------------\n")
                            with open(f"{typeusername}.txt") as userpointer:
                                print(userpointer.read())

                        elif file_options == 2:
                            append_to_file = input("PLEASE ENTER WHAT YOU WANT TO WRITE TO YOUR FILE\nTYPE \'EXIT\' FOR EXITTING WITHOUT MAKING ANY CHANGES\n")
                            if append_to_file == "EXIT":
                                print("EXITING ...")
                            else:
                                with open(f"{typeusername}.txt", "a") as userpointer:
                                    userpointer.write(append_to_file)
                                    userpointer.write("\n")

                        elif file_options == 3:
                            with open(f"{typeusername}.txt", "x") as userpointer:
                                userpointer.write("")

                        elif file_options == 4:
                            print(f"logging out {typeusername}")
                            break

                        else:
                            print("ERROR\nPLEASE ENTER A VALID CHOICE\n")






                else:
                    print("WRONG USERNAME OR PASSWORD COMBINATION")
            else:
                print("WRONG USERNAME OR PASSWORD COMBINATION")

        else
            print("USER NOT FOUND")


# refreshing var list

        usernamelist = []
        passwordlist = []
