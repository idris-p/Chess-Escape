#Resolution: 1920x1080

from tkinter import *
from PIL import Image, ImageTk

#Instantiate Variables
global pieces
global piecesImage
global dead
global messageShown
global levelButtons
global moveableSquaresButtons
global bossScreen
global existingNames
global existingScores
global cheatMode
pieces = []
piecesImage = []
boardColour = "#779556"
dead = False
messageShown = False
levelButtons = []
moveableSquaresButtons = []
bossScreen = False
existingNames = []
existingScores = []
cheatMode = False

root = Tk()
root.geometry("1920x1080")
root.title("Chess Escape")
#root.iconbitmap('Images/pawn_black_big.ico')
root["bg"] = '#C4C4C4'

#Define Images
green_board = PhotoImage(file="Images/green.png")
orange_board = PhotoImage(file="Images/orange.png")
blue_board = PhotoImage(file="Images/blue.png")
yellow_board = PhotoImage(file="Images/yellow.png")
move = PhotoImage(file="Images/move.png")
disguise = PhotoImage(file="Images/disguise.png")

#Open text files
leaderboardFile = open("Data/leaderboard.txt", 'a')
saveStateFile = open("Data/saveState.txt", 'a')

#Define each level
level1 = Frame(root, width=1920, height=1080, bg='#C4C4C4')
level2 = Frame(root, width=1920, height=1080, bg='#C4C4C4')
level3 = Frame(root, width=1920, height=1080, bg='#C4C4C4')
level4 = Frame(root, width=1920, height=1080, bg='#C4C4C4')
level5 = Frame(root, width=1920, height=1080, bg='#C4C4C4')
level6 = Frame(root, width=1920, height=1080, bg='#C4C4C4')
level7 = Frame(root, width=1920, height=1080, bg='#C4C4C4')
level8 = Frame(root, width=1920, height=1080, bg='#C4C4C4')
level9 = Frame(root, width=1920, height=1080, bg='#C4C4C4')
level10 = Frame(root, width=1920, height=1080, bg='#C4C4C4')
level = [level1, level2, level3, level4, level5, level6, level7, level8, level9, level10]

#Classes for player and enemys
class Player():
    def __init__(self, x, y, image, animation):
        self.x = x
        self.y = y
        self.level = 1
        self.currentLevel = 1
        self.image = image
        self.spawn = [0, 4]
        self.type = "king"
        self.animation = animation
        self.score = 0

player = Player(0, 4, ImageTk.PhotoImage(Image.open("Images/king_black.png")), ImageTk.PhotoImage(Image.open("Images/king_black_animate.png")))

class Piece():
    def __init__(self, x, y, board, type, image, animation):
        self.x = x
        self.y = y
        self.board = board
        self.type = type
        self.image = image
        self.animation = animation

#Piece positions for each level
level_array = [[["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["player", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ]] * 10
level_array[0] = [["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "pawn", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["player", "", "", "", "", "", "", ""],
                ["", "", "", "", "pawn", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ]
level_array[1] = [["", "", "", "", "", "pawn", "", ""],
                ["", "pawn", "", "pawn", "", "", "", ""],
                ["", "", "", "", "", "", "", "pawn"],
                ["", "", "", "", "pawn", "", "pawn", ""],
                ["player", "", "pawn", "", "", "", "", ""],
                ["", "", "", "", "pawn", "", "", ""],
                ["", "", "", "", "", "", "", "pawn"],
                ["", "", "", "pawn", "", "", "", ""],
                ]
level_array[2] = [["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", "knight"],
                ["", "", "knight", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["player", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "pawn", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "knight", "", "", "", "", "", ""],
                ]
level_array[3] = [["", "", "rook", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "pawn", ""],
                ["", "", "", "", "", "", "", ""],
                ["player", "", "", "", "", "", "", ""],
                ["", "", "", "", "knight", "", "", ""],
                ["", "", "pawn", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ]
level_array[4] = [["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "knight", "", "", "", ""],
                ["", "", "", "", "", "", "rook", ""],
                ["player", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "pawn", ""],
                ["", "", "pawn", "", "", "", "", ""],
                ["", "", "knight", "", "", "", "pawn", ""],
                ]
level_array[5] = [["", "", "rook", "", "", "", "", ""],
                ["player", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "rook", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "pawn", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ]
level_array[6] = [["", "", "", "", "", "rook", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "knight", "", "", "bishop", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["player", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "bishop", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "rook", "", ""],
                ]
level_array[7] = [["", "", "", "", "", "", "", ""],
                ["player", "", "", "", "", "", "", ""],
                ["", "", "bishop", "", "", "", "", ""],
                ["", "", "", "", "", "", "bishop", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["bishop", "", "", "bishop", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ]
level_array[8] = [["", "", "", "", "", "", "", ""],
                ["player", "", "", "", "", "", "", ""],
                ["", "", "", "queen", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "bishop", ""],
                ["", "", "", "", "", "", "", ""],
                ["queen", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ]
level_array[9] = [["", "", "", "", "", "", "", ""],
                ["", "", "pawn", "", "", "", "knight", ""],
                ["", "", "knight", "", "", "", "", ""],
                ["", "", "", "", "", "", "", ""],
                ["player", "", "", "", "", "", "", ""],
                ["", "", "", "", "", "", "pawn", ""],
                ["", "", "", "", "", "", "", ""],
                ["", "", "queen", "", "", "", "", ""],
                ]

#Put pieces on board
def decorate_board(n, canvas):
    for i in range(0, 8):
        for j in range(0, 8):
            if level_array[n-1][j][i] == "pawn":
                pieces.append(Piece(i, j, n, "pawn", ImageTk.PhotoImage(Image.open("Images/pawn_white.png")), ImageTk.PhotoImage(Image.open("Images/pawn_white_animate.png"))))
                piecesImage.append(canvas.create_image((((2*i)+1)/16)*600, (((2*j)+1)/16)*600, anchor=CENTER, image=pieces[-1].image))
                animate(boards[n-1], piecesImage[-1], pieces[-1].image, pieces[-1].animation, 400)
            elif level_array[n-1][j][i] == "bishop":
                pieces.append(Piece(i, j, n, "bishop", ImageTk.PhotoImage(Image.open("Images/bishop_white.png")), ImageTk.PhotoImage(Image.open("Images/bishop_white_animate.png"))))
                piecesImage.append(canvas.create_image((((2*i)+1)/16)*600, (((2*j)+1)/16)*600, anchor=CENTER, image=pieces[-1].image))
                animate(boards[n-1], piecesImage[-1], pieces[-1].image, pieces[-1].animation, 400)
            elif level_array[n-1][j][i] == "king":
                pieces.append(Piece(i, j, n, "king", ImageTk.PhotoImage(Image.open("Images/king_white.png")), ImageTk.PhotoImage(Image.open("Images/king_white.png"))))
                piecesImage.append(canvas.create_image((((2*i)+1)/16)*600, (((2*j)+1)/16)*600, anchor=CENTER, image=pieces[-1].image))
                animate(boards[n-1], piecesImage[-1], pieces[-1].image, pieces[-1].animation, 400)
            elif level_array[n-1][j][i] == "knight":
                pieces.append(Piece(i, j, n, "knight", ImageTk.PhotoImage(Image.open("Images/knight_white.png")), ImageTk.PhotoImage(Image.open("Images/knight_white_animate.png"))))
                piecesImage.append(canvas.create_image((((2*i)+1)/16)*600, (((2*j)+1)/16)*600, anchor=CENTER, image=pieces[-1].image))
                animate(boards[n-1], piecesImage[-1], pieces[-1].image, pieces[-1].animation, 400)
            elif level_array[n-1][j][i] == "queen":
                pieces.append(Piece(i, j, n, "queen", ImageTk.PhotoImage(Image.open("Images/queen_white.png")), ImageTk.PhotoImage(Image.open("Images/queen_white_animate.png"))))
                piecesImage.append(canvas.create_image((((2*i)+1)/16)*600, (((2*j)+1)/16)*600, anchor=CENTER, image=pieces[-1].image))
                animate(boards[n-1], piecesImage[-1], pieces[-1].image, pieces[-1].animation, 400)
            elif level_array[n-1][j][i] == "rook":
                pieces.append(Piece(i, j, n, "rook", ImageTk.PhotoImage(Image.open("Images/rook_white.png")), ImageTk.PhotoImage(Image.open("Images/rook_white_animate.png"))))
                piecesImage.append(canvas.create_image((((2*i)+1)/16)*600, (((2*j)+1)/16)*600, anchor=CENTER, image=pieces[-1].image))
                animate(boards[n-1], piecesImage[-1], pieces[-1].image, pieces[-1].animation, 400)

#Convert board position to canvas position
def board_to_canvas(n):
    return (((2*n)+1)/16)*600

#Set spawn point
def set_spawn(n):
    for i in range (0, 8):
        for j in range(0, 8):
            if level_array[n][j][i] == "player":
                player.x = i
                player.spawn[0] = i
                player.y = j
                player.spawn[1] = j
                
#Save
def save():
    with open('Data/saveState.txt', 'w') as file:
        file.writelines(str(player.level) + "\n")
        file.writelines(str(player.score))

#Load
global quitButton
def load(frame):
    global levelButtons
    global quitButton
    with open('Data/saveState.txt', 'r') as file:
        player.level = int(file.readline().strip())
        player.score = int(file.readline().strip())
        frame.place_forget()
        for i in range(0, player.level-1):
            player.currentLevel = i+1
            levelButtons[i].invoke()
            player.x = 7
            check_win()
            win_screen.destroy()
            level[i].place_forget(), level[i+1].place(relx=0.5, rely=0.2, anchor=CENTER)
            draw_board(i+1)
            set_spawn(i+1)
            increment_level()
            open_level(i+2, boards[i+1])
            calculate_move(boards[i+1])
    levelButtons[player.level-1].invoke()
    level[player.level-1].place_forget()
    reset_level()
    level_select()
    restart(boards[player.level-1], moveableSquaresButtons)

#Save menu
def save_menu(frame):
    save_screen = Frame(frame, width=500, height=400, bg='#C4C4C4', highlightthickness=3, highlightbackground="#252525")

    saveText = Label(save_screen, text="Save/Load", bg='#C4C4C4', font=30)
    saveText.place(relx=0.5, rely=0.15, anchor=CENTER)

    saveButton = Button(save_screen, text="Save", width=25, height=8, command=lambda:[save()])
    saveButton.place(relx=0.26, rely=0.6, anchor=CENTER)

    loadButton = Button(save_screen, text="Load", width=25, height=8, command=lambda:[load(frame)])
    loadButton.place(relx=0.74, rely=0.6, anchor=CENTER)

    closeButton = Button(save_screen, text="×", width=2, height=1, command=lambda:[save_screen.destroy()])
    closeButton.place(relx=0.99, rely=0.01, anchor=NE)

    save_screen.place(relx=0.5, rely=0.55, anchor=CENTER)

#Level Select Screen
def level_select():
    global levelButtons
    level_selection = Frame(root, width=1920, height=1080)
    level_selection["bg"] = '#C4C4C4'

    ls_text = PhotoImage(file = 'Images/levelSelect.png')
    ls = Label(level_selection, image=ls_text)
    ls["bg"] = '#C4C4C4'
    ls.place(relx=0.5, rely=0.3, anchor=CENTER)

    #Buttons
    level1_button = Button(level_selection, text="1", width=10, height=5, command=lambda:[level_selection.place_forget(), set_level(1), draw_board(0), open_level(1, boards[0]), restart(boards[0], moveableSquaresButtons), set_spawn(0)])
    level1_button.place(relx=0.36, rely=0.45, anchor=CENTER)
    level2_button = Button(level_selection, text="2", width=10, height=5, command=lambda:[level_selection.place_forget(), set_level(2), restart(boards[1], moveableSquaresButtons), set_spawn(1), draw_board(1), open_level(2, boards[1]), calculate_move(boards[1])])
    level2_button.place(relx=0.43, rely=0.45, anchor=CENTER)
    level3_button = Button(level_selection, text="3", width=10, height=5, command=lambda:[level_selection.place_forget(), set_level(3), set_spawn(2), restart(boards[2], moveableSquaresButtons), draw_board(2), open_level(3, boards[2]), calculate_move(boards[2])])
    level3_button.place(relx=0.5, rely=0.45, anchor=CENTER)
    level4_button = Button(level_selection, text="4", width=10, height=5, command=lambda:[level_selection.place_forget(), set_level(4), set_spawn(3), restart(boards[3], moveableSquaresButtons), draw_board(3), open_level(4, boards[3]), calculate_move(boards[3])])
    level4_button.place(relx=0.57, rely=0.45, anchor=CENTER)
    level5_button = Button(level_selection, text="5", width=10, height=5, command=lambda:[level_selection.place_forget(), set_level(5), set_spawn(4), restart(boards[4], moveableSquaresButtons), draw_board(4), open_level(5, boards[4]), calculate_move(boards[4])])
    level5_button.place(relx=0.64, rely=0.45, anchor=CENTER)
    level6_button = Button(level_selection, text="6", width=10, height=5, command=lambda:[level_selection.place_forget(), set_level(6), set_spawn(5), restart(boards[5], moveableSquaresButtons), draw_board(5), open_level(6, boards[5]), calculate_move(boards[5])])
    level6_button.place(relx=0.36, rely=0.58, anchor=CENTER)
    level7_button = Button(level_selection, text="7", width=10, height=5, command=lambda:[level_selection.place_forget(), set_level(7), set_spawn(6), restart(boards[6], moveableSquaresButtons), draw_board(6), open_level(7, boards[6]), calculate_move(boards[6])])
    level7_button.place(relx=0.43, rely=0.58, anchor=CENTER)
    level8_button = Button(level_selection, text="8", width=10, height=5, command=lambda:[level_selection.place_forget(), set_level(8), set_spawn(7), restart(boards[7], moveableSquaresButtons), draw_board(7), open_level(8, boards[7]), calculate_move(boards[7])])
    level8_button.place(relx=0.5, rely=0.58, anchor=CENTER)
    level9_button = Button(level_selection, text="9", width=10, height=5, command=lambda:[level_selection.place_forget(), set_level(9), set_spawn(8), restart(boards[8], moveableSquaresButtons), draw_board(8), open_level(9, boards[8]), calculate_move(boards[8])])
    level9_button.place(relx=0.57, rely=0.58, anchor=CENTER)
    level10_button = Button(level_selection, text="10", width=10, height=5, command=lambda:[level_selection.place_forget(), set_level(10), set_spawn(9), restart(boards[9], moveableSquaresButtons), draw_board(9), open_level(10, boards[9]), calculate_move(boards[9])])
    level10_button.place(relx=0.64, rely=0.58, anchor=CENTER)

    levelButtons = [level1_button, level2_button, level3_button, level4_button, level5_button, level6_button, level7_button, level8_button, level9_button, level10_button]

    saveButton = Button(level_selection, text="Save/Load", command=lambda:[save_menu(level_selection)])
    saveButton.place(relx=1-0.18, rely=0.25, anchor=NE)

    backButton = Button(level_selection, text="Back", command=lambda:[main_menu.place(relx=0.5, rely=0.5, anchor=CENTER), level_selection.place_forget()])
    backButton.place(relx=0.18, rely=0.25, anchor=NW)

    cover_image = PhotoImage(file = 'Images/cover.png')
    cover = Label(level_selection, image = cover_image)
    cover["bg"] = '#C4C4C4'
    cover.place(relx=0.5, rely=0.92, anchor=CENTER)

    disable_levels()

    level_selection.place(relx=0.5, rely=0.5, anchor=CENTER)
    level_selection.mainloop()

#Leaderboard Menu
def leaderboard():
    global existingNames
    global existingScores

    leaderboard_menu = Frame(root, width=1920, height=1080)
    leaderboard_menu["bg"] = '#C4C4C4'

    leaderboard_text = PhotoImage(file = 'Images/leaderboard.png')
    ld = Label(leaderboard_menu, image=leaderboard_text)
    ld["bg"] = '#C4C4C4'
    ld.place(relx=0.5, rely=0.3, anchor=CENTER)

    nameTitle = Label(leaderboard_menu, text="Name", bg='#C4C4C4', font=30)
    nameTitle.place(relx=0.42, rely=0.37, anchor=W)

    scoreTitle = Label(leaderboard_menu, text="Score", bg='#C4C4C4', font=30)
    scoreTitle.place(relx=1-0.42, rely=0.37, anchor=E)

    for i in range(1, 11):
        number = Label(leaderboard_menu, text=str(i)+".", bg='#C4C4C4', font=30)
        number.place(relx=0.4, rely=0.4+(i/25), anchor=CENTER)

    for j in range(0, len(existingNames)):
        name = Label(leaderboard_menu, text=existingNames[j], bg='#C4C4C4', font=30)
        name.place(relx=0.42, rely=0.4+((j+1)/25), anchor=W)

    for k in range(0, len(existingScores)):
        name = Label(leaderboard_menu, text=str(existingScores[k]), bg='#C4C4C4', font=30)
        name.place(relx=1-0.42, rely=0.4+((k+1)/25), anchor=E)

    backButton = Button(leaderboard_menu, text="Back", command=lambda:[main_menu.place(relx=0.5, rely=0.5, anchor=CENTER), leaderboard_menu.place_forget()])
    backButton.place(relx=0.18, rely=0.25, anchor=NW)

    cover_image = PhotoImage(file = 'Images/cover.png')
    cover = Label(leaderboard_menu, image = cover_image)
    cover["bg"] = '#C4C4C4'
    cover.place(relx=0.5, rely=0.92, anchor=CENTER)

    leaderboard_menu.place(relx=0.5, rely=0.5, anchor=CENTER)
    leaderboard_menu.mainloop()

#Load leaderboard
def load_leaderboard():
    global existingNames
    global existingScores
    existingNames = []
    existingScores = []
    with open('Data/leaderboard.txt', 'r') as file1:
        lines = file1.readlines()
        for i in range(0, len(lines)):
            lines[i] = lines[i].strip()
            existingName, existingScore = lines[i].split(", ")
            existingScore = int(existingScore)
            existingNames.append(existingName)
            existingScores.append(existingScore)

#Add to leaderboard
def add_to_leaderboard(name, score):
    global existingNames
    global existingScores
    added = False
    load_leaderboard()
    for j in range(0, len(existingScores)):
        if score < existingScores[j]:
            existingNames.insert(j, name)
            existingScores.insert(j, score)
            added = True
            break
        elif score >= existingScores[j]:
            try:
                if score < existingScores[j+1]:
                    existingNames.insert(j+1, name)
                    existingScores.insert(j+1, score)
                    added = True
                    break
            except:
                pass
    if added == False:
        existingNames.append(name)
        existingScores.append(score)
        added = True

    with open('Data/leaderboard.txt', 'w') as file2:
        for k in range(0, len(existingNames)):
            file2.writelines(existingNames[k] + ", " + str(existingScores[k]) + "\n")

#Finished game
def finished():
    finish = Frame(root, width=500, height=400, bg='#C4C4C4', highlightthickness=3, highlightbackground="#252525")

    enterNameText = Label(finish, text="Enter name:", bg='#C4C4C4', font=30)
    enterNameText.place(relx=0.5, rely=0.15, anchor=CENTER)

    enterNameBox = Entry(finish, width=50)
    enterNameBox.place(relx=0.5, rely=0.4, anchor=CENTER)

    enterNameSubmit = Button(finish, text="Submit", width=30, height=2, command=lambda:[level[player.currentLevel-1].place_forget(), add_to_leaderboard(enterNameBox.get(), player.score), finish.place_forget(), leaderboard()])
    enterNameSubmit.place(relx=0.5, rely=0.8, anchor=CENTER)

    finish.place(relx=0.5, rely=0.5, anchor=CENTER)

#Pause game
def pause(n, buttons, pauseButton):
    global quitButton
    for i in range(0, len(buttons)):
        buttons[i].destroy()

    pause_screen = Frame(level[n], width=400, height=300, bg='#C4C4C4', highlightthickness=3, highlightbackground="#252525")

    pauseTitle = Label(pause_screen, text="Paused", bg='#C4C4C4')
    pauseTitle.place(relx=0.5, rely=0.15, anchor=CENTER)

    resumeButton = Button(pause_screen, text="Resume", width=30, height=2, command=lambda:[pause_screen.destroy(), calculate_move(boards[n]), pauseButton.config(state='normal')])
    resumeButton.place(relx=0.5, rely=0.35, anchor=CENTER)

    restartButton = Button(pause_screen, text="Restart", width=30, height=2, command=lambda:[pause_screen.destroy(), restart(boards[player.currentLevel-1], moveableSquaresButtons), pauseButton.config(state='normal')])
    restartButton.place(relx=0.5, rely=0.55, anchor=CENTER)

    quitButton = Button(pause_screen, text="Quit", width=30, height=2, command=lambda:[pause_screen.destroy(), level[n].place_forget(), reset_level(), level_select(), pause_screen.destroy(), restart(boards[player.currentLevel-1], moveableSquaresButtons)])
    quitButton.place(relx=0.5, rely=0.75, anchor=CENTER)

    pause_screen.place(relx=0.5, rely=0.65, anchor=CENTER)

#Help
def help(n, buttons, helpButton):
    for i in range(0, len(buttons)):
        buttons[i].destroy()
    
    help_screen = Frame(level[n], width=500, height=400, bg='#C4C4C4', highlightthickness=3, highlightbackground="#252525")

    helpText1 = Label(help_screen, text="This is NOT traditional chess", bg='#C4C4C4', font=30)
    helpText1.place(relx=0.5, rely=0.15, anchor=CENTER)

    helpText2 = Label(help_screen, text="-Complete levels by making it to the opposite end of the board\n\n-Enemy pieces will only move if they are able to capture you\n\n-You are unable to capture enemy pieces\n\n-Landing on a square under threat by an enemy piece will always result\n in a loss, even if the square is at the end of the board!", bg='#C4C4C4')
    helpText2.place(relx=0.5, rely=0.45, anchor=CENTER)

    pawn = PhotoImage(file = 'Images/pawn_white.png')
    pawnHelp = Label(help_screen, image=pawn)
    pawnHelp["bg"] = '#C4C4C4'
    pawnHelp.place(relx=0.1, rely=0.75, anchor=CENTER)
    pawnText = Label(help_screen, text="Pawn", bg='#C4C4C4', font=30)
    pawnText.place(relx=0.1, rely=0.88, anchor=CENTER)

    knight = PhotoImage(file = 'Images/knight_white.png')
    knightHelp = Label(help_screen, image=knight)
    knightHelp["bg"] = '#C4C4C4'
    knightHelp.place(relx=0.3, rely=0.75, anchor=CENTER)
    knightText = Label(help_screen, text="Knight", bg='#C4C4C4', font=30)
    knightText.place(relx=0.3, rely=0.88, anchor=CENTER)

    rook = PhotoImage(file = 'Images/rook_white.png')
    rookHelp = Label(help_screen, image=rook)
    rookHelp["bg"] = '#C4C4C4'
    rookHelp.place(relx=0.5, rely=0.75, anchor=CENTER)
    rookText = Label(help_screen, text="Rook", bg='#C4C4C4', font=30)
    rookText.place(relx=0.5, rely=0.88, anchor=CENTER)

    bishop = PhotoImage(file = 'Images/bishop_white.png')
    bishopHelp = Label(help_screen, image=bishop)
    bishopHelp["bg"] = '#C4C4C4'
    bishopHelp.place(relx=0.7, rely=0.75, anchor=CENTER)
    bishopText = Label(help_screen, text="Bishop", bg='#C4C4C4', font=30)
    bishopText.place(relx=0.7, rely=0.88, anchor=CENTER)

    queen = PhotoImage(file = 'Images/queen_white.png')
    queenHelp = Label(help_screen, image=queen)
    queenHelp["bg"] = '#C4C4C4'
    queenHelp.place(relx=0.9, rely=0.75, anchor=CENTER)
    queenText = Label(help_screen, text="Queen", bg='#C4C4C4', font=30)
    queenText.place(relx=0.9, rely=0.88, anchor=CENTER)

    closeButton = Button(help_screen, text="×", width=2, height=1, command=lambda:[help_screen.destroy(), calculate_move(boards[n]), helpButton.config(state='normal')])
    closeButton.place(relx=0.99, rely=0.01, anchor=NE)

    help_screen.place(relx=0.5, rely=0.65, anchor=CENTER)
    help_screen.mainloop()

#Open Level
def open_level(n, canvas):
    global playerImage
    global scoreText
    if player.currentLevel == 6 or player.currentLevel == 8 or player.currentLevel == 9:
        player.type = "knight"
        player.image = ImageTk.PhotoImage(Image.open("Images/knight_black_animate.png"))
        player.animation = ImageTk.PhotoImage(Image.open("Images/knight_black.png"))
    else:
        player.type = "king"
        player.image = ImageTk.PhotoImage(Image.open("Images/king_black.png"))
        player.animation = ImageTk.PhotoImage(Image.open("Images/king_black_animate.png"))
    playerImage = canvas.create_image((((2*player.spawn[0])+1)/16)*600, (((2*player.spawn[1])+1)/16)*600, anchor=CENTER, image=player.image)
    animate(boards[n-1], playerImage, player.image, player.animation, 400)

    scoreText = Label(level[n-1], text="Moves:  " + str(player.score), bg='#C4C4C4', font=30)
    scoreText.place(relx=0.25, rely=0.68, anchor=CENTER)

    pauseButton = Button(level[n-1], text="| |", width=4, height=2, command=lambda:[pause(n-1, moveableSquaresButtons, pauseButton), pauseButton.config(state='disabled')])
    pauseButton.place(relx=0.82, rely=0.4, anchor=NE)

    helpButton = Button(level[n-1], text="?", width=4, height=2, command=lambda:[help(n-1, moveableSquaresButtons, helpButton), helpButton.config(state='disabled')])
    helpButton.place(relx=0.82, rely=0.45, anchor=NE)

    level[n-1].place(relx=0.5, rely=0.2, anchor=CENTER)
    

#Animate player
def animate(canvas, image_item, photo1, photo2, delay):
    def toggle():
        current_image = canvas.itemcget(image_item, "image")
        if current_image == str(photo1):
            canvas.itemconfig(image_item, image=photo2)
        else:
            canvas.itemconfig(image_item, image=photo1)
        canvas.after(delay, toggle)

    toggle()

#Change colour
def change_colour(colour):
    global boardColour
    boardColour = colour

#Settings
def settings():
    settings_menu = Frame(root, width=1920, height=1080, bg='#C4C4C4')
    green_button = Button(settings_menu, image=green_board, width = 250, height = 250, command=lambda:[change_colour("#779556")])
    green_button.place(relx=0.41, rely=0.4, anchor=CENTER)
    orange_button = Button(settings_menu, image=orange_board, width = 250, height = 250, command=lambda:[change_colour("#a1662a")])
    orange_button.place(relx=0.59, rely=0.4, anchor=CENTER)
    blue_button = Button(settings_menu, image=blue_board, width = 250, height = 250, command=lambda:[change_colour("#3f61b0")])
    blue_button.place(relx=0.41, rely=0.71, anchor=CENTER)
    yellow_button = Button(settings_menu, image=yellow_board, width = 250, height = 250, command=lambda:[change_colour("#c2a930")])
    yellow_button.place(relx=0.59, rely=0.71, anchor=CENTER)
    settings_menu.place(relx=0.5, rely=0.5, anchor=CENTER)

    backButton = Button(settings_menu, text="Back", command=lambda:[main_menu.place(relx=0.5, rely=0.5, anchor=CENTER), settings_menu.place_forget()])
    backButton.place(relx=0.18, rely=0.25, anchor=NW)

#Make chess board on level n
global boards
boards = []
def draw_board(n):
    border = Frame(level[n], width=610, height=610, background="#252525")
    border.place(relx=0.4999, rely=0.67999, anchor=CENTER)
    boards.insert(n, Canvas(level[n], width=600, height=600, highlightthickness=0, bg="#DED6C4"))
    for j in range(0, 8, 2):
        for k in range(1, 9, 2):
            boards[n].create_rectangle(75 * k, 75 * j, 75 * (k + 1), 75 * (j + 1), outline=boardColour, fill=boardColour)
    for j in range(1, 9, 2):
        for k in range(1, 9, 2):
            boards[n].create_rectangle(75 * k, 75 * j, 75 * (k - 1), 75 * (j + 1), outline=boardColour, fill=boardColour)
    boards[n].place(relx=0.5, rely=0.68, anchor=CENTER)
    decorate_board(n+1, boards[n])

#Increment current level
def increment_level():
    player.currentLevel += 1

def set_level(n):
    player.currentLevel = n

#Win screen
def win(n, buttons):
    for i in range(0, len(buttons)):
        buttons[i].destroy()
    global win_screen
    global pieces
    global piecesImage
    pieces = []
    piecesImage = []

    reset_level()

    win_screen = Frame(level[n], width=400, height=300, bg='#C4C4C4', highlightthickness=3, highlightbackground="#252525")

    winTitle = Label(win_screen, text="Level Complete!", bg='#C4C4C4')
    winTitle.place(relx=0.5, rely=0.15, anchor=CENTER)

    if player.currentLevel != 10:
        nextButton = Button(win_screen, text="Next Level", width=30, height=5, command=lambda:[win_screen.destroy(), level[n].place_forget(), level[n+1].place(relx=0.5, rely=0.2, anchor=CENTER), draw_board(n+1), set_spawn(n+1), increment_level(), open_level(n+2, boards[n+1]), calculate_move(boards[n+1])])
        nextButton.place(relx=0.5, rely=0.4, anchor=CENTER)
    else:
        leaderboardButton = Button(win_screen, text="Leaderboard", width=30, height=5, command=lambda:[win_screen.destroy(), finished()])
        leaderboardButton.place(relx=0.5, rely=0.4, anchor=CENTER)

    quitButton = Button(win_screen, text="Quit", width=30, height=5, command=lambda:[win_screen.destroy(), level[n].place_forget(), draw_board(n+1), level_select(), restart(boards[player.currentLevel-1], moveableSquaresButtons)])
    quitButton.place(relx=0.5, rely=0.75, anchor=CENTER)

    win_screen.place(relx=0.5, rely=0.65, anchor=CENTER)

#Restart level
def restart(canvas, buttons):
    global dead
    global pieces
    global piecesImage
    global messageShown
    messageShown = False
    try:
        for i in range(0, len(piecesImage)):
            canvas.delete(piecesImage[i])
    except:
        pass
    pieces = []
    piecesImage = []
    decorate_board(player.currentLevel, boards[player.currentLevel-1])
    dead = False
    reset_level()
    player.x = player.spawn[0]
    player.y = player.spawn[1]
    canvas.coords(playerImage, (((2*player.spawn[0])+1)/16)*600, (((2*player.spawn[1])+1)/16)*600)
    canvas.update()
    for i in range(0, len(buttons)):
        buttons[i].destroy()
    calculate_move(canvas)

#Death screen
def death(n):
    global dead
    global messageShown
    if messageShown == False:
        messageShown = True
        dead = True

        death_screen = Frame(level[n], width=400, height=300, bg='#C4C4C4', highlightthickness=3, highlightbackground="#252525")

        deathTitle = Label(death_screen, text="Captured!", bg='#C4C4C4')
        deathTitle.place(relx=0.5, rely=0.15, anchor=CENTER)

        restartButton = Button(death_screen, text="Restart", width=30, height=5, command=lambda:[death_screen.destroy(), restart(boards[player.currentLevel-1], moveableSquaresButtons)])
        restartButton.place(relx=0.5, rely=0.4, anchor=CENTER)

        quitButton = Button(death_screen, text="Quit", width=30, height=5, command=lambda:[death_screen.destroy(), level[n].place_forget(), reset_level(), level_select(), death_screen.destroy(), restart(boards[player.currentLevel-1], moveableSquaresButtons)])
        quitButton.place(relx=0.5, rely=0.75, anchor=CENTER)

        death_screen.after(800)
        death_screen.place(relx=0.5, rely=0.65, anchor=CENTER)

#Check win
def check_win():
    global dead
    if dead == False:
        if player.x == 7:
            print("You win")
            win(player.currentLevel - 1, moveableSquaresButtons)
            if player.level == player.currentLevel:
                player.level += 1

#Translate enemy
def translate_enemy(canvas, piece, startx, starty, finalx, finaly):
    canvas.move(piece, (finalx-startx)/10, (finaly-starty)/10)
    canvas.after(10)
    canvas.update()

#Check death - Collision detection
def check_death(canvas):
    for m in range(0, len(piecesImage)):
        canvas.tag_raise(piecesImage[m])
    for i in range(0, len(pieces)):
        if pieces[i].type == "pawn":
            if (pieces[i].x - player.x == 1) and (abs(pieces[i].y - player.y) == 1):
                print("You died")
                for l in range(0, 10):
                    translate_enemy(canvas, piecesImage[i], (((2*pieces[i].x)+1)/16)*600, (((2*pieces[i].y)+1)/16)*600, (((2*player.x)+1)/16)*600, (((2*player.y)+1)/16)*600)
                death(player.currentLevel - 1)
        elif pieces[i].type == "bishop":
            exposed = True
            if (abs(pieces[i].x - player.x) == abs(pieces[i].y - player.y)): 
                for j in range(1, abs(pieces[i].x - player.x)):
                    if (pieces[i].x - player.x) == (pieces[i].y - player.y):
                        if pieces[i].x - player.x > 0:
                            if level_array[player.currentLevel - 1][player.y + j][player.x + j] != "":
                                exposed = False
                        elif pieces[i].x - player.x < 0:
                            if level_array[player.currentLevel - 1][player.y - j][player.x - j] != "":
                                exposed = False
                    elif (pieces[i].x - player.x) == -(pieces[i].y - player.y):
                        if pieces[i].x - player.x > 0:
                            if level_array[player.currentLevel - 1][player.y - j][player.x + j] != "":
                                exposed = False
                        elif pieces[i].x - player.x < 0:
                            if level_array[player.currentLevel - 1][player.y + j][player.x - j] != "":
                                exposed = False
                if exposed == True:
                    print("You died")
                    for l in range(0, 10):
                        translate_enemy(canvas, piecesImage[i], (((2*pieces[i].x)+1)/16)*600, (((2*pieces[i].y)+1)/16)*600, (((2*player.x)+1)/16)*600, (((2*player.y)+1)/16)*600)
                    death(player.currentLevel - 1)
        elif pieces[i].type == "king": #Remove as king can't capture king
            if (abs(pieces[i].x - player.x) == 1 or abs(pieces[i].x - player.x) == 0) and ((abs(pieces[i].y - player.y) == 1 or abs(pieces[i].y - player.y) == 0)):
                print("You died")
                for l in range(0, 10):
                    translate_enemy(canvas, piecesImage[i], (((2*pieces[i].x)+1)/16)*600, (((2*pieces[i].y)+1)/16)*600, (((2*player.x)+1)/16)*600, (((2*player.y)+1)/16)*600)
                death(player.currentLevel - 1)
        elif pieces[i].type == "knight":
            if (abs(pieces[i].x - player.x) == 1) and (abs(pieces[i].y - player.y) == 2) or (abs(pieces[i].x - player.x )== 2) and (abs(pieces[i].y - player.y) == 1):
                print("You died")
                for l in range(0, 10):
                    translate_enemy(canvas, piecesImage[i], (((2*pieces[i].x)+1)/16)*600, (((2*pieces[i].y)+1)/16)*600, (((2*player.x)+1)/16)*600, (((2*player.y)+1)/16)*600)
                death(player.currentLevel - 1)
        elif pieces[i].type == "rook":
            exposed = True
            if (pieces[i].x == player.x):
                for j in range(0, 8):
                    if level_array[player.currentLevel-1][j][player.x] != "":
                        if (j < player.y and j > pieces[i].y) or (j > player.y and j < pieces[i].y):
                            exposed = False
            elif (pieces[i].y == player.y):
                for j in range(0, 8):
                    if level_array[player.currentLevel-1][player.y][j] != "":
                        if (j < player.x and j > pieces[i].x) or (j > player.x and j < pieces[i].x):
                            exposed = False
            else:
                exposed = False
            if exposed == True:
                print("You died")
                for l in range(0, 10):
                    translate_enemy(canvas, piecesImage[i], (((2*pieces[i].x)+1)/16)*600, (((2*pieces[i].y)+1)/16)*600, (((2*player.x)+1)/16)*600, (((2*player.y)+1)/16)*600)
                death(player.currentLevel - 1)
        elif pieces[i].type == "queen":
            exposed = True
            if (pieces[i].x == player.x) or (pieces[i].y == player.y) or (abs(pieces[i].x - player.x) == abs(pieces[i].y - player.y)):
                if (pieces[i].x == player.x):
                    for j in range(0, 8):
                        if level_array[player.currentLevel-1][j][player.x] != "":
                            if (j < player.y and j > pieces[i].y) or (j > player.y and j < pieces[i].y):
                                exposed = False
                elif (pieces[i].y == player.y):
                    for j in range(0, 8):
                        if level_array[player.currentLevel-1][player.y][j] != "":
                            if (j < player.x and j > pieces[i].x) or (j > player.x and j < pieces[i].x):
                                exposed = False
                elif (abs(pieces[i].x - player.x) == abs(pieces[i].y - player.y)): 
                    for j in range(1, abs(pieces[i].x - player.x)):
                        if (pieces[i].x - player.x) == (pieces[i].y - player.y):
                            if pieces[i].x - player.x > 0:
                                if level_array[player.currentLevel - 1][player.y + j][player.x + j] != "":
                                    exposed = False
                            elif pieces[i].x - player.x < 0:
                                if level_array[player.currentLevel - 1][player.y - j][player.x - j] != "":
                                    exposed = False
                        elif (pieces[i].x - player.x) == -(pieces[i].y - player.y):
                            if pieces[i].x - player.x > 0:
                                if level_array[player.currentLevel - 1][player.y - j][player.x + j] != "":
                                    exposed = False
                            elif pieces[i].x - player.x < 0:
                                if level_array[player.currentLevel - 1][player.y + j][player.x - j] != "":
                                    exposed = False
                if exposed == True:
                    print("You died")
                    for l in range(0, 10):
                        translate_enemy(canvas, piecesImage[i], (((2*pieces[i].x)+1)/16)*600, (((2*pieces[i].y)+1)/16)*600, (((2*player.x)+1)/16)*600, (((2*player.y)+1)/16)*600)
                    death(player.currentLevel - 1)

#Translate player
def translate_player(canvas, startx, starty, finalx, finaly):
    canvas.move(playerImage, (finalx-startx)/10, (finaly-starty)/10)
    canvas.after(10)
    canvas.update()

#Move player
def move_player(x, y, canvas, buttons):
    global scoreText
    level_array[player.currentLevel - 1][player.y][player.x] = ""
    level_array[player.currentLevel - 1][y][x] = "player"
    for i in range(0, len(buttons)):
        buttons[i].destroy()
    startx = (((2*player.x)+1)/16)*600
    starty = (((2*player.y)+1)/16)*600
    finalx = (((2*x)+1)/16)*600
    finaly = (((2*y)+1)/16)*600
    for i in range(0, 10):
        translate_player(canvas, startx, starty, finalx, finaly)
    player.x = x
    player.y = y
    player.score += 1
    scoreText.config(text="Moves:  " + str(player.score))
    print(player.score)
    check_death(canvas)
    check_win()

#Place buttons in moveable squares
def calculate_move(canvas):
    global cheatMode
    if player.x != 7:
        moveableSquares = []
        global moveableSquaresButtons
        moveableSquaresButtons = []
        currentPosition = [player.x, player.y]
        for i in range(0, 8):
            for j in range(0, 8):
                if level_array[player.currentLevel - 1][j][i] == "":
                    if cheatMode == False:
                        if player.type == "king":
                            if abs(player.x - i) <= 1 and abs(player.y - j) <= 1 and [i, j] != currentPosition:
                                moveableSquares.append([i, j])
                        elif player.type == "knight":
                            if (abs(player.x - i) == 1 and abs(player.y - j) == 2) or (abs(player.x - i) == 2 and abs(player.y - j) == 1):
                                moveableSquares.append([i, j])
                    else:
                        moveableSquares.append([i, j])

        if dead == False:
            for k in range(0, len(moveableSquares)):
                buttonx = (((2*moveableSquares[k][0])+1)/16)*600
                buttony = (((2*moveableSquares[k][1])+1)/16)*600
                moveableSquaresButtons.append(Button(canvas, width=32, height=32, image=move, bd=0, highlightthickness=0, command=lambda k=k:[move_player(moveableSquares[k][0], moveableSquares[k][1], canvas, moveableSquaresButtons), calculate_move(canvas)]))
                moveableSquaresButtons[-1].place(x=buttonx, y=buttony, anchor=CENTER)

#Reset level_array
def reset_level():
    level_array[player.currentLevel - 1][player.y][player.x] = ""
    level_array[player.currentLevel - 1][player.spawn[1]][player.spawn[0]] = "player"

#Disable levels
def disable_levels():
    for i in range(9, player.level-1, -1):
        levelButtons[i].config(state='disabled')

# #Reopen level
# def reopen_level(n):
#     player.x = player.spawn[0]
#     player.y = player.spawn[]

#Main Menu
main_menu = Frame(root, width=1920, height=1080, bg='#C4C4C4')

title_text = PhotoImage(file = 'Images/title.png')
title = Label(main_menu, image = title_text)
title["bg"] = '#C4C4C4'
title.place(relx=0.5, rely=0.3, anchor=CENTER)

play_button = Button(main_menu, text = "Play", width = 25, height = 2, command=lambda:[main_menu.place_forget(), level_select()])
play_button.place(relx=0.5, rely=0.42, anchor=CENTER)

leaderboard_button = Button(main_menu, text = "Leaderboard", width = 25, height = 2, command=lambda:[leaderboard()])
leaderboard_button.place(relx=0.5, rely=0.5, anchor=CENTER)

settings_button = Button(main_menu, text = "Settings", width = 25, height = 2, command=lambda:[settings()])
settings_button.place(relx=0.5, rely=0.58, anchor=CENTER)

exit_Button = Button(main_menu, text= "Exit", command = root.destroy, width = 20, height = 2)
exit_Button.place(relx=0.5, rely=0.66, anchor=CENTER)

cover_image = PhotoImage(file = 'Images/cover.png')
cover = Label(main_menu, image = cover_image)
cover["bg"] = '#C4C4C4'
cover.place(relx=0.5, rely=0.92, anchor=CENTER)

main_menu.place(relx=0.5, rely=0.5, anchor=CENTER)

def toggle_cheat(event):
    global cheatMode
    if cheatMode == False:
        cheatMode = True
    else:
        cheatMode = False

global boss_screen
def boss(event):   
    global bossScreen
    global boss_screen
    if bossScreen == False:
        boss_screen = Frame(root, width=1920, height=1080, bg='#00FF00')
        disguiseImage = Label(boss_screen, image=disguise)
        disguiseImage.place(relx=0, rely=0, anchor=NW)
        boss_screen.pack()
        print("Shown")
        bossScreen = True
    else:
        boss_screen.destroy()
        print("Hidden")
        bossScreen = False

root.bind('<KeyPress-bracketright>', toggle_cheat)
root.bind('<KeyPress-Escape>', boss)
load_leaderboard()
root.mainloop()