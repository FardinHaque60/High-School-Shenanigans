from random import randint

account_holders = {
    92047902 : "bob"
}

balances = {
    92047902 : 342
}

def account_holdername(account_number, name):
    account_holders[account_number] = name

def account_balances(account_number):
    balances[account_number] = 0.0

def make_account_prompt():
    name = input("Please enter your name: ")
    if name.isdigit():
        print ("Please enter a valid name!")
        run_atm()

    if name in account_holders.values():
        print ("That name is taken please try another one!")
        run_atm()

    account_number = []
    for x in range(8):
        random_number = randint(0,9)
        account_number.append(random_number)
    for x in account_number:
        index = account_number.index(x)
        account_number[index] = str(x)
    final_account_number = "".join(account_number)
    print ("Your account number is: %s" % final_account_number)

    account_holdername(int(final_account_number), name)
    account_balances(int(final_account_number))
    return final_account_number

def ask_first_question():
    
    first_question = input("Would you like to make a transaction or make a new account?: ")

    if not (first_question == "make transaction" or first_question == "make new account"):
        print ("Please enter 'make transaction' or 'make new account'!")
        run_atm()

    if (first_question == "make transaction"):
        return str(first_question)
    
    if (first_question == "make new account"):
        return str(first_question)

def ask_second_question():
    second_question = input("What is your account number?: ")
    try:
        second_question = int(second_question)
    except ValueError:
        print ("Please enter a valid account number!")
        run_atm()

    if int(second_question) in balances:
        new_balance = 0.0
        new_balance += balances[int(second_question)]
        print ("Entering %s's account..." % (account_holders[int(second_question)]))
        print ("Your balance is $%s" % (new_balance))
        return int(second_question)
    else: 
        print ("Sorry that account number is not in the data base!")
        run_atm()
    

def ask_third_question(second_question_use):
    third_question = input("Would you like to make a deposit or withdraw?: ")

    balance_output = balances[second_question_use]
    if not (third_question == "deposit" or third_question == "withdraw"):
        print ("Please enter 'deposit' or 'withdraw'!")
        run_atm()

    if (third_question == "deposit"):
        deposit = input("How much would you like to deposit?: ")
        try:
            deposit = float(deposit)
        except ValueError:
            print ("pleae enter a valid deposit amount!")
            run_atm()

        balance_output += deposit
        print ("Your new balance is: $%.2f" % (balance_output))
        balances[second_question_use] = balance_output
        return balance_output

    if (third_question == "withdraw"):
        withdraw = input("How much would you like to withdraw?: ")
        try:
            wihtdraw = float(withdraw)
        except ValueError:
            print ("Please enter a valid withdraw amount!")
            run_atm()

        if (float(withdraw) > float(balance_output)):
            print ("You do not have enough in your account!")
        else:
            balance_output -= withdraw
            print ("Your new balance is: $%.2f" % (balance_output))
            balances[second_question_use] = balance_output
            return balance_output

def run_atm():
    if (ask_first_question() == "make transaction"):
        ask_third_question(int(ask_second_question()))
        print ("Thank You for using atm")
        print ("----------")
        run_atm()
    else:
        make_account_prompt()
        run_atm()
        
run_atm()