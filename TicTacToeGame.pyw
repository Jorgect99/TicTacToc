from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe Game')
root.iconbitmap('D:\Projects\TicTacToe\icon.ico')
root.resizable(False, False) 

# X starts
clicked = True
count = 0
winner = False

# Disable Buttons
def disable_all_buttons():
    button1.config(state = "disabled")
    button2.config(state = "disabled")
    button3.config(state = "disabled")
    button4.config(state = "disabled")
    button5.config(state = "disabled")
    button6.config(state = "disabled")
    button7.config(state = "disabled")
    button8.config(state = "disabled")
    button9.config(state = "disabled")


#Check to see if someone won
def checkifwon():
    global winner
    winner = False

    #Check for X
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        button1.config(bg = "Blue")
        button2.config(bg = "Blue")
        button3.config(bg = "Blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X win!!")
        disable_all_buttons()
    elif button3["text"] == "X" and button4["text"] == "X" and button6["text"] == "X": 
        button3.config(bg = "Blue")
        button4.config(bg = "Blue")
        button5.config(bg = "Blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X win!!")
        disable_all_buttons()
    elif button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X": 
        button7.config(bg = "Blue")
        button8.config(bg = "Blue")
        button9.config(bg = "Blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X win!!")
        disable_all_buttons()
    elif button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X": 
        button1.config(bg = "Blue")
        button4.config(bg = "Blue")
        button7.config(bg = "Blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X win!!")
        disable_all_buttons()
    elif button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X": 
        button2.config(bg = "Blue")
        button5.config(bg = "Blue")
        button8.config(bg = "Blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X win!!")
        disable_all_buttons()
    elif button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X": 
        button3.config(bg = "Blue")
        button6.config(bg = "Blue")
        button9.config(bg = "Blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X win!!")
        disable_all_buttons()
    elif button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X": 
        button1.config(bg = "Blue")
        button5.config(bg = "Blue")
        button9.config(bg = "Blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X win!!")
        disable_all_buttons()
    elif button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X": 
        button3.config(bg = "Blue")
        button5.config(bg = "Blue")
        button7.config(bg = "Blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X win!!")
        disable_all_buttons()
    
    # Check for O
    elif button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        button1.config(bg = "Blue")
        button2.config(bg = "Blue")
        button3.config(bg = "Blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O win!!")
        disable_all_buttons()
    elif button3["text"] == "O" and button4["text"] == "O" and button6["text"] == "O": 
        button3.config(bg = "Blue")
        button4.config(bg = "Blue")
        button5.config(bg = "Blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O win!!")
        disable_all_buttons()
    elif button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O": 
        button7.config(bg = "Blue")
        button8.config(bg = "Blue")
        button9.config(bg = "Blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O win!!")
        disable_all_buttons()
    elif button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O": 
        button1.config(bg = "Blue")
        button4.config(bg = "Blue")
        button7.config(bg = "Blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O win!!")
        disable_all_buttons()
    elif button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O": 
        button2.config(bg = "Blue")
        button5.config(bg = "Blue")
        button8.config(bg = "Blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O win!!")
        disable_all_buttons()
    elif button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O": 
        button3.config(bg = "Blue")
        button6.config(bg = "Blue")
        button9.config(bg = "Blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O win!!")
        disable_all_buttons()
    elif button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O": 
        button1.config(bg = "Blue")
        button5.config(bg = "Blue")
        button9.config(bg = "Blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O win!!")
        disable_all_buttons()
    elif button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O": 
        button3.config(bg = "Blue")
        button5.config(bg = "Blue")
        button7.config(bg = "Blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O win!!")
        disable_all_buttons()

    #Check if tie
    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a Tie!!")
        disable_all_buttons()

#Button clicked funtion
def button_click(button):
    global clicked, count
    
    if button["text"] == " " and clicked == True:
        button["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif button["text"] == " " and clicked == False:
        button["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "That box has already been selected!\nPick another Box.")

# Restart the game
def resetGame():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global clicked, count
    clicked = True
    count = 0
    #Buttons
    button1 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: button_click(button1))
    button2 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: button_click(button2))
    button3 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: button_click(button3))

    button4 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: button_click(button4))
    button5 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: button_click(button5))
    button6 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: button_click(button6))

    button7 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: button_click(button7))
    button8 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: button_click(button8))
    button9 = Button(root, text=" ", font=("Helvetica", 20), height = 3, width = 6, bg = "SystemButtonFace", command = lambda: button_click(button9))

    #Grid
    button1.grid(row = 0, column = 0)
    button2.grid(row = 0, column = 1)
    button3.grid(row = 0, column = 2)

    button4.grid(row = 1, column = 0)
    button5.grid(row = 1, column = 1)
    button6.grid(row = 1, column = 2)

    button7.grid(row = 2, column = 0)
    button8.grid(row = 2, column = 1)
    button9.grid(row = 2, column = 2)

# menu button
menu = Menu(root)
root.config(menu = menu)

#Reset button
menu.add_command(label = "Reset Game", command = resetGame)


resetGame()
root.mainloop()