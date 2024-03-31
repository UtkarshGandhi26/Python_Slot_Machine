import random

#Global Values
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

#Rows and columns in slot machine
ROWS = 3
COLS = 3

#Dictionary to hold symbols and their occurrence for each line
symbols_count = {
    "🔆": 2,
    "💥": 4,
    "🔰": 6,
    "➰": 8
}

#Dictionary to hold symbols and their value for each calculating winnings
symbols_value = {
    "🔆": 5,
    "💥": 4,
    "🔰": 3,
    "➰": 2
}

#Getting symbols for a slot machine spin
def get_slot_machine_spin(rows, cols, symbols):

    #all_symbols hold all the symbols ar per their respective count. Ex: 🔆,🔆,💥,💥,💥,💥 ...........
    all_symbols = []
    #From dictionary.items we can get key and value both
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    #Columms stores the random symbols to be dispalyed for every spin
    columns=[]

    #For every column, generate row number of symbols
    for _ in range(cols):
        
        column = []
        #We use a copy of all_symbols as we need to remove the symbol once it is picked
        current_symbols = all_symbols[:]
       
        for _ in range(rows):
           
            #Random value from current_symbols
            value = random.choice(current_symbols)
            #Removing that value from current_symbols
            current_symbols.remove(value)
            #Adding to the column
            column.append(value)
        
        #Adding column to the columns
        columns.append(column)
    
    return columns

#Prinitng the slow machine spin
def print_slot_machine(columns):
    
    #Transposing the slotmachine columns and printing
    for row in range(len(columns[0])): 

        #Printing 0th element of every column
        for i, column in enumerate(columns):
            if i != len(column)-1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        
        print()
    return

#Check Winnings based on if symbol on a line is same throughout
#User can bet on a specifc number of lines 1-Top 2-Top, Middle 3-Top, Middle, Bottom
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    #Iterating over number of lines that were bet on
    for line in range(lines):
        #Getting symbol at 0th index for every row that is bet on
        symbol = columns[0][line]

        #Looping over every symbol of that row
        for column in columns:

            #That is why we created columns as [[a,b,c][b,c,a][a,d,c] and then print the transpose]
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

#Deposit Function
def deposit():
    while True:
        amount = input("What would you like to deposit? ₹")
        #Checking whether amount enetered is a +ve number
        if amount.isdigit():
            amount = int(amount)
            #Checking whether amount is greater than zero
            if amount > 0:
                break
            else:
                print("Please enter amount greater than ₹0.")
        else:
            print("Please enter a valid Deposit Amount")
    return amount

#Get number of lines that user wants to play
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        #Checking whether lines enetered is a +ve number
        if lines.isdigit():
            lines = int(lines)
            #Checking whether lines is greater than zero
            if 1 <= lines <=MAX_LINES:
                break
            else:
                print("Number of Lines must be within the limit (1-" + str(MAX_LINES) + ")? ")
        else:
            print("Please enter a valid Line Number")
    return lines

#Bet that user want to play
def get_bet():
    while True:
        bet = input("What would you like to bet on each line (Min: ₹" +str(MIN_BET)+ " - Max: ₹" + str(MAX_BET) + ")? ₹")
        #Checking whether bet enetered is a +ve number
        if bet.isdigit():
            bet = int(bet)
            #Checking whether lines is greater than zero
            if MIN_BET <= bet <=MAX_BET:
                break
            else:
                # print("Bet must be within the limit (Min: " +str(MIN_BET)+ "- Max: " + str(MAX_BET) + ")? ")
                #Another way to print variables within string
                print(f"Bet must be within the limit (Min: ₹{MIN_BET} - Max: ₹{MAX_BET})")
        else:
            print("Please enter a valid Bet Amount")
    return bet

#One Game Spin
def spin(balance):

    print()
    print()
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if(total_bet > balance):
            print(f"You do not have enough balance to bet that amount, your current balance is: ₹{balance}")
        else:
            break
   
    print("Balance: ₹",balance)
    print("Lines: ",lines)
    print("Bet: ₹",bet)
    print("Total bet: ₹",total_bet)

    #Getting the slots
    slots = get_slot_machine_spin(ROWS, COLS, symbols_count)
    #Printing the slots
    print_slot_machine(slots)

    #Get winnings
    winnings, winning_lines = check_winnings(slots, lines, bet, symbols_value)
    print("You won ₹", winnings)
    # * splits the array and prints values separated by space
    print("You won on: ", *winning_lines)

    return winnings - total_bet

def main():

    balance = deposit()
    
    while balance > 0:
        print(f"Current balance is ₹{balance}")
        print()
        print()
        each_spin = input("Press enter to Play or q to Quit. ")

        if each_spin == "q":
            break
        else:
            balance += spin(balance)

    print (f"You left with ₹{balance}")
    
main()