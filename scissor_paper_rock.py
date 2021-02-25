# rock-paper-scissor
from tkinter import *
from PIL import Image, ImageTk, ImageFile
from random import randint

ImageFile.LOAD_TRUNCATED_IMAGES = True

# player info
player_name = input("Hello, I'm Jarvis. And you?\n")
print('\nOkay', player_name+', lets start our game.\nPlease check out for the lobby.')
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
                   command=lambda: cl.destroy())
    cl_no.grid(row=2, column=2)


# buttons
rock = Button(root, width=20, height=2, text="ROCK", bg="#FF3E4D", fg="white", command=lambda: update_choice("rock"))
paper = Button(root, width=20, height=2, text="PAPER", bg="#FAD02E", fg="white", command=lambda: update_choice("paper"))
scissor = Button(root, width=20, height=2, text="SCISSOR", bg="#0ABDE3", fg="white",
                 command=lambda: update_choice("scissor"))
close_now = Button(root, width=20, height=2, text="EXIT", bg="#781ac9", fg="white",
                   command=lambda: close())
rock.grid(row=2, column=1)
paper.grid(row=2, column=2)
scissor.grid(row=2, column=3)
close_now.grid(row=4, column=2)

root.mainloop()
