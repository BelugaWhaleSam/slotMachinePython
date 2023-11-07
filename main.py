import random 

MAX_LINES = 3 # constant in all caps
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

#dictionary 
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append[symbol]

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] # copying to current_symbols
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column) 

    return columns

# print the transpose

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!= len(columns) - 1:
                print(column[row],"|")
            else:
                print(column[row])



def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount) # converts string to integer
            if amount>0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")
    
    return amount

def get_number_of_lines():
    while True:
        number_of_lines = input("How many lines would you like to bet on (1-" +str(MAX_LINES)+ ")? ")
        if number_of_lines.isdigit():
            number_of_lines = int(number_of_lines) # converts string to integer
            if 1<=number_of_lines<=MAX_LINES:
                break
            else:
                print("Number of lines must be between 1 and", MAX_LINES)
        else:
            print("Please enter a number")
    
    return number_of_lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount) # converts string to integer
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}")
        else:
            print("Please enter a number")
    
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet>balance:
            print(f"You don't have enough money to bet ${total_bet}, your balance is ${balance}")
        else:
            break

    print(f"You are betting ${bet} on ${lines} lines. Total bet is equal to ${total_bet}")
    print(balance, lines)
  
main()