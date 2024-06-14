from tkinter import*
from PIL import Image,ImageTk
from random import randint

root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="#40f7a5")

rock_img = ImageTk.PhotoImage(Image.open("rps/r.png"))
paper_img = ImageTk.PhotoImage(Image.open("rps/p.png"))
scissor_img = ImageTk.PhotoImage(Image.open("rps/s.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rps/r.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("rps/p.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("rps/s.png"))

user_label = Label(root, image=scissor_img, bg="#40f7a5")
comp_label = Label(root, image=scissor_img_comp, bg="#40f7a5")
user_label.grid(row=1, column=4)
comp_label.grid(row=1, column=0)

playerScore = Label(root, text=0, font=('Arial', 25), bg="black", fg="white")
computerScore = Label(root, text=0, font=('Arial', 25), bg="black", fg="white")
score = Label(root, text='SCORE', font=('Arial', 25), bg="black", fg="white")
playerScore.grid(row=1, column=3)
computerScore.grid(row=1, column=1) 
score.grid(row=1, column=2)

rock = Button(root,width=13,height=1,text="ROCK",font=('Arial', 12, 'bold'),bg="red",fg="black", command = lambda: updateChoice("rock"))
paper = Button(root,width=13,height=1,text="PAPER",font=('Arial', 12, 'bold'),bg="yellow",fg="black", command = lambda: updateChoice("paper"))
scissor = Button(root,width=13,height=1,text="SCISSOR",font=('Arial', 12, 'bold'),bg="green",fg="black", command = lambda: updateChoice("scissor"))
rock.grid(row=2,column=1)
paper.grid(row=2,column=2)
scissor.grid(row=2,column=3)

user_indicator = Label(root, font=('Arial', 16, 'bold'), text="PLAYER", bg="#40f7a5", fg="red")
computer_indicator = Label(root, font=('Arial', 16, 'bold'), text="COMPUTER", bg="#40f7a5", fg="red")
user_indicator.grid(row=0, column=4)
computer_indicator.grid(row=0, column=0)

msg = Label(root, font=('Arial', 20, 'bold'), bg="#40f7a5",fg="red")
msg.grid(row=3, column=2)

def updateMessage(x):
    msg['text'] = x

def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score) 

def checkWin(player, computer):
    outcomes = {
        ("rock", "rock"): "It's a tie!!!",
        ("paper", "paper"): "It's a tie!!!",
        ("scissor", "scissor"): "It's a tie!!!",
        ("rock", "paper"): "You lose",
        ("rock", "scissor"): "You win",
        ("paper", "rock"): "You win",
        ("paper", "scissor"): "You lose",
        ("scissor", "rock"): "You lose",
        ("scissor", "paper"): "You win"
    }

    outcome = outcomes.get((player, computer))
    if outcome:
        updateMessage(outcome)
        if "win" in outcome:
            updateUserScore()
        elif "lose" in outcome:
            updateCompScore()

choices = ["rock","paper","scissor"]
def updateChoice(x):
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp) 
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
         user_label.configure(image=paper_img)
    else:
         user_label.configure(image=scissor_img)
         
    checkWin(x,compChoice)

root.mainloop()
