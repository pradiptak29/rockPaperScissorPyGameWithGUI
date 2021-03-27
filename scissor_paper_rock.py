# rock-paper-scissor
from tkinter import *
from PIL import Image, ImageTk, ImageFile
from random import randint

ImageFile.LOAD_TRUNCATED_IMAGES = True

print('Loading Rock-Paper-Scissor...')

opening_window = Tk()
opening_window.title("Lets Start")
opening_window.configure(background="#7e1ab8")
opening_window.resizable(0, 0)
lbl1 = Label(opening_window, text="**Rock-Paper-Scissors**\n\n  Hello, I'm Jarvis. Do you want to play?  ", font=('calibre', 12, 'bold'), bg="#7e1ab8", fg="#c3d408")
lbl1.grid(column=1, row=0)
lbl2 = Label(opening_window, text="--------------------------\nRules:-\n1. Rock wins over Scissor\n2. Scissor wins over Paper\n3. Paper wins over Rock\n--------------------------", font=('calibre', 10, 'bold'), bg="#7e1ab8", fg="#c3d408")
lbl2.grid(column=1, row=3)
name_var = StringVar()


def submit():
    player_name = name_var.get()
    print("Player Name : " + player_name)

    if player_name.lower() != '':
        opening_window.destroy()
        print('Information fetched.\n')
        print('\nOkay', player_name + ', lets start our game.\nPlease check out for the lobby.')

        # main window
        root = Tk()
        root.title("Rock Paper Scissor")
        root.configure(background="#1ea66b")
        root.resizable(0, 1)

        # picture
        rock_user_img = ImageTk.PhotoImage(Image.open("images/rock_user.png"))
        paper_user_img = ImageTk.PhotoImage(Image.open("images/paper_user.png"))
        scissor_user_img = ImageTk.PhotoImage(Image.open("images/scissors_user.png"))
        rock_comp_img = ImageTk.PhotoImage(Image.open("images/rock_comp.png"))
        paper_comp_img = ImageTk.PhotoImage(Image.open("images/paper_comp.png"))
        scissor_comp_img = ImageTk.PhotoImage(Image.open("images/scissors_comp.png"))

        # insert picture
        user_label = Label(root, image=scissor_user_img, bg="#1ea66b")
        comp_label = Label(root, image=scissor_comp_img, bg="#1ea66b")
        comp_label.grid(row=1, column=0)
        user_label.grid(row=1, column=4)

        # scores
        player_score = Label(root, text=0, font=100, bg="#1ea66b", fg="white")
        computer_score = Label(root, text=0, font=100, bg="#1ea66b", fg="white")
        player_score.grid(row=1, column=3)
        computer_score.grid(row=1, column=1)

        # indicators
        user_indicator = Label(root, text=player_name, font=50, bg="#1ea66b", fg="white")
        computer_indicator = Label(root, text="Jarvis", font=50, bg="#1ea66b", fg="white")
        user_indicator.grid(row=0, column=3)
        computer_indicator.grid(row=0, column=1)

        # messages
        msg = Label(root, font=50, bg="#1ea66b", fg="white")
        msg.grid(row=3, column=2)

        # update message
        def update_message(x):
            msg["text"] = x

        # update user score
        def update_user_score():
            score = int(player_score["text"])
            score += 1
            player_score["text"] = str(score)

        # update computer score
        def update_comp_score():
            score = int(computer_score["text"])
            score += 1
            computer_score["text"] = str(score)

        # check winner
        def check_win(player, computer):
            if player == computer:
                update_message("Its a tie!!")
            elif player == "rock":
                if computer == "paper":
                    update_message("You loose.")
                    update_comp_score()
                else:
                    update_message("You win.")
                    update_user_score()
            elif player == "paper":
                if computer == "scissor":
                    update_message("You loose.")
                    update_comp_score()
                else:
                    update_message("You win.")
                    update_user_score()
            elif player == "scissor":
                if computer == "rock":
                    update_message("You loose.")
                    update_comp_score()
                else:
                    update_message("You win.")
                    update_user_score()
            else:
                pass

        # update choices
        choices = ["rock", "paper", "scissor"]

        def update_choice(x):
            # for computer
            comp_choice = choices[randint(0, 2)]
            if comp_choice == "rock":
                comp_label.configure(image=rock_comp_img)
            elif comp_choice == "paper":
                comp_label.configure(image=paper_comp_img)
            else:
                comp_label.configure(image=scissor_comp_img)

            # for user
            if x == "rock":
                user_label.configure(image=rock_user_img)
            elif x == "paper":
                user_label.configure(image=paper_user_img)
            elif x == "scissor":
                user_label.configure(image=scissor_user_img)
            else:
                pass

            check_win(x, comp_choice)

        # close button

        def close():
            close_now["state"] = "disabled"
            rock["state"] = "disabled"
            paper["state"] = "disabled"
            scissor["state"] = "disabled"
            cl = Tk()
            cl.title("Exit?")
            cl.configure(background="white")
            cl.resizable(0, 0)

            cl_exit = Label(cl, text="Do you want to exit?", font=150, bg="white", fg="black")
            cl_exit.grid(row=1, column=1)

            cl_yes = Button(cl, width=20, height=2, text="YES", bg="#1dd909", fg="white",
                            command=lambda: exit())
            cl_yes.grid(row=2, column=1)
            cl_no = Button(cl, width=20, height=2, text="NO", bg="#ed3305", fg="white",
                           command=lambda: destroy())
            cl_no.grid(row=2, column=2)

            def destroy():
                cl.destroy()
                close_now["state"] = "normal"
                rock["state"] = "normal"
                paper["state"] = "normal"
                scissor["state"] = "normal"


        # buttons
        rock = Button(root, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="white",
                      command=lambda: update_choice("rock"))
        paper = Button(root, width=20, height=2, text="PAPER", bg="#FAD02E", fg="white",
                       command=lambda: update_choice("paper"))
        scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#0ABDE3", fg="white",
                         command=lambda: update_choice("scissor"))
        close_now = Button(root, width=20, height=2, text="EXIT", bg="#781ac9", fg="white",
                           command=lambda: close())
        rock.grid(row=2, column=1)
        paper.grid(row=2, column=2)
        scissor.grid(row=2, column=3)
        close_now.grid(row=4, column=2)

        root.mainloop()
    else:
        print('Please enter an user name.')
        pass


def clicked():
    print('Getting Information...')
    lbl3 = Label(opening_window, text="\n    Please Enter an User Name Below    \n", font=('calibre', 12, 'bold'), bg="#7e1ab8", fg="#c3d408")
    lbl3.grid(column=1, row=0)
    name_entry = Entry(opening_window, textvariable=name_var, font=('calibre', 18, 'bold'), bg="white", fg="black")
    name_entry.grid(row=1, column=1)
    sub_btn = Button(opening_window, width=10, height=1, font=('calibre', 12, 'bold'), bg="#1dd909", text='Submit', command=submit)
    sub_btn.grid(column=1, row=2)


play_btn_yes = Button(opening_window, width=10, height=1, font=('calibre', 12, 'bold'), text="Yes", bg="#1dd909", fg="white", command=lambda: clicked())
play_btn_no = Button(opening_window, width=10, height=1, font=('calibre', 12, 'bold'), text="No", bg="#ed3305", fg="white", command=lambda: opening_window.destroy())
play_btn_yes.grid(column=1, row=1)
play_btn_no.grid(column=1, row=2)

opening_window.mainloop()
