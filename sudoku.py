# Sudoku
import random
import tkinter as tk
from tkinter import ttk
import time
# board[row][column]
GIVEN_NUMBER = 20

def createCanvas(board):
    root = tk.Tk()
    root.title("Sudoku")
    entries = [[tk.Entry(root, width=5, justify='center') for row in range(9)] for col in range(9)]

    for rowIndex in range(9):
        for colIndex in range(9):
            value = board[rowIndex][colIndex]
            if (value != 0):
                entries[rowIndex][colIndex] = tk.Label(root, justify='center', borderwidth=2,font=('Helvetica', 16, 'bold'), text=value)
                #ttk.Separator(root, orient="horizontal").grid(row=rowIndex, column=colIndex)
                #entries[rowIndex][colIndex].insert(0, value)
            entries[rowIndex][colIndex].grid(row=rowIndex, column=colIndex, ipady=10)

    #Decoration
    ttk.Separator(root, orient="horizontal").grid(row=2, columnspan=9, sticky="SEW")
    ttk.Separator(root, orient="horizontal").grid(row=5, columnspan=9, sticky="SEW")
    ttk.Separator(root, orient="vertical").grid(rowspan=9, column=2, row=0, sticky="NSE")
    ttk.Separator(root, orient="vertical").grid(rowspan=9, column=5, row=0, sticky="NSE")

    spaceList = findAllSpace(board)
    button = tk.Button(root, text='Solve',command= lambda: sodukuSolver(board, spaceList, 0, entries))
    button.grid(row=10, column=4)

    root.mainloop()
    return entries


def randomGenerator():
    return random.randrange(9)


def isValidNumber(board, assigned_row, assigned_column, number):
    #check for repeated number in row
    for row_counter in range(9):
        if (board[row_counter][assigned_column] == number):
            return False

    #check for repeated number in column
    for column_counter in range(9):
        if (board[assigned_row][column_counter] == number):
            return False

    #check for repeated number in subNines
    (row, column) = assigned_row // 3, assigned_column // 3
    (subNineStartingRow, subNineStartingColumn) = row * 3, column * 3
    for row_counter in range(3):
        for column_counter in range(3):
            if (board[subNineStartingRow+row_counter][subNineStartingColumn+column_counter] == number):
                return False
    # return true if it is a valid numnber
    return True

def displayBoard(board):
    for row in range(9):
        print()
        if ((row) % 3 == 0):
            print("""-----------------------""")
        for column in range(9):
            #print("column is", column)
            if ((column) % 3 == 0):
                print("|", end=" ")
            print(board[row][column], end=" ")

def findAllSpace(board):
    list = []
    for row in range(9):
        for col in range(9):
            if (board[row][col] == 0):
                list.append((row, col))
    return list

def boardInitialize(board):
    counter = 0
    while (counter < GIVEN_NUMBER ):
        assigned_row, assigned_column = randomGenerator(), randomGenerator()
        while (board[assigned_row][assigned_column] != 0):
            assigned_row, assigned_column = randomGenerator(), randomGenerator()
        number = random.randrange(1, 10)
        if (isValidNumber(board, assigned_row, assigned_column, number)):
            board[assigned_row][assigned_column] = number
            counter += 1

def isDone(board):
    for row in range(9):
        for col in range(9):
            if (board[row][col] == 0):
                return False
    return True

def sodukuSolver(board, spaceList, index, entries):

    if (len(spaceList) == index):
        return True

    (row, col) = spaceList[index]

    for solution in range(1, 10):
        if (isValidNumber(board, row, col, solution)):
            board[row][col] = solution
            entries[row][col].delete(0)
            entries[row][col].insert(0, solution)
            entries[row][col].update()
            if (sodukuSolver(board, spaceList, index+1, entries)):
                return True

            board[row][col] = 0
            entries[row][col].delete(0)

    #Backtrack
    return False



def main():
    board = [[0 for row in range(9)] for column in range(9)]
    boardInitialize(board)
    print("Soduku Puzzle")
    displayBoard(board)
    entries = createCanvas(board)

    print("\nSoduku Solution")
    spaceList = findAllSpace(board)
    if (sodukuSolver(board, spaceList, 0, entries)):
        displayBoard(board)
    else:
        print("Has no Solution")



if __name__ == '__main__':
    main()
