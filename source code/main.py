from pcbw import BankWallet
from pcbw import Parent
from pcbw import Child
# from pcbw import Dad
# from pcbw import Mom

# Importing instances of all users for the bank wallet
from pcbw import dad,mom,c1,c2,c3,c4,c5,c6,c7,c8

# Tuple of all members connected to bank account    
member_tuple = ("Dad","Mom","Child1","Child2","Child3","Child4","Child5","Child6","Child7","Child8")


# Placed all instances of the child class in a tuple for easier selection by index
child_tuple = (c1,c2,c3,c4,c5,c6,c7,c8)

def welcome():
    """
    Function that starts the main program. The options displayed are placed in an infinite loop
    until the exit input is given. The user will be directed to a different set of operations based
    on the input they will give. The various operations are categories under 3 different groups :
    Dad, Mom, or Child.

    Takes no input parameters.
    """
    print("Welcome to your Bank Wallet!")
    print("The bank wallet has the following members :")
    # Loop to print all members of the bank wallet
    for member in member_tuple:
        print(member)

    # main event loop to determine user type and possible actions
    while True:
        print("What user are you ?")
        print("Child [Access Value : 1]")
        print("Mom [Access Value : 2]")
        print("Dad [Access Value : 3]")
        print("Press 0 to quit.")
        # Input selection based on access level of user - 3,2, or 1
        user_choice = int(input("Enter your selection here: "))
        if user_choice == 0:
            print("Quitting application...")
            exit()
        elif user_choice == 1:
            if Child.child_instance_count <=8:
                startChild()
        elif user_choice == 2:
            # If mom's access value is set to 0, then she is blocked from accessing
            if mom.access_value == 0:
                print("Sorry, but it seems you have been blocked fromm accessing the wallet.\n")
            else:
                startMom()
        elif user_choice == 3:
                startDad()
        else:
            print("Invalid input, please try again.")

def startChild():
    """
    Function that involves operations available to a Child instance. All children are numbered from 1
    to 8 in the program and each child will be referenced with the help of their respective ID.

    Takes no input parameters.
    """
    child_input_id = int(input("Hello Child. Please enter your ID (1 - 8):"))
    # If a child's access value is set to 0, they cannot access the wallet
    if child_tuple[child_input_id-1].access_value == 0:
        print(f"Sorry Child{child_input_id}, it seems you have been blocked from accessing the wallet.")
    elif child_tuple[child_input_id-1].access_deny_count == 2:
        print(f"Sorry Child{child_input_id}, you been rejected from access the wallet anymore.")
    else:
        child_options(child_input_id)
    

def startMom():
    """
    Function that involved operations availble to the Mom instance. The Mother can choose to deposit,
    withdraw, read transaction(s) or simply see the available balance in the wallet and connected bank
    account. The selection is based on integer inputs given by the user.

    Takes no input parameters.
    """
    print("Hello Mom. What do you need?")
    print("1. Deposit Money\n2. Withdraw Money\n3. Read Statment(s)\n4. See available balance")
    mom_input = int(input("Enter your choice: "))

    if mom_input == 1:
        deposit_input = int(input("User OK. Please enter amount to deposit."))
        mom.deposit(deposit_input)
        
    elif mom_input == 2:
        withdraw_input = int(input("Enter amount to withdraw."))  
        mom.withdraw(withdraw_input)

    elif mom_input == 3:
        mom.getStatement()

    elif mom_input == 4:
        BankWallet.showBalance() 



def startDad():
    """
    Function that involved operations availble to the Dad instance. The Dad can choose to deposit,
    withdraw, read transaction(s), simply see the available balance in the wallet and connected bank
    account or block a member from accesing the wallet. The selection is based on integer inputs 
    given by the user.

    Takes no input parameters.
    """
    print("Hello Dad. What do you need?")
    print("1. Deposit Money\n2. Withdraw Money\n3. Read Statment(s)\n4. See available balance\n5. Block a member\n6. Unblock a member")
    dad_input = int(input("Enter your choice: "))
    if dad_input == 1:
        deposit_input = int(input("User OK. Please enter amount to deposit."))
        dad.deposit(deposit_input)

    elif dad_input == 2:
        withdraw_input = int(input("Enter amount to withdraw: "))  
        dad.withdraw(withdraw_input)

    elif dad_input == 3:
        dad.getStatement()
        print("Thank you.")
         
    elif dad_input == 4:
        BankWallet.showBalance()   
        print("Thank you.")  

    elif dad_input == 5:
        # Blocking a member depends on the ID of that member.
        id_select = int(input("Enter ID of Member you want to select:[(0 for Mom) or (1-8) for a child]: "))
        if id_select == 0:
            dad.blockMember(mom)
        elif id_select == 1:
            dad.blockMember(c1)
        elif id_select == 2:
            dad.blockMember(c2)
        elif id_select == 3:
            dad.blockMember(c3)
        elif id_select == 4:
            dad.blockMember(c4)
        elif id_select == 5:
            dad.blockMember(c5)
        elif id_select == 6:
            dad.blockMember(c6)
        elif id_select == 7:
            dad.blockMember(c7)
        elif id_select == 8:
            dad.blockMember(c8)   
        else:
            print("Invalid Input...")

    elif dad_input == 6:
        # Blocking a member depends on the ID of that member.
        id_select = int(input("Enter ID of Member you want to select:[(0 for Mom) or (1-8) for a child]: "))
        if id_select == 0:
            dad.unblockMember(mom)
        elif id_select == 1:
            dad.unblockMember(c1)
        elif id_select == 2:
            dad.unblockMember(c2)
        elif id_select == 3:
            dad.unblockMember(c3)
        elif id_select == 4:
            dad.unblockMember(c4)
        elif id_select == 5:
            dad.unblockMember(c5)
        elif id_select == 6:
            dad.unblockMember(c6)
        elif id_select == 7:
            dad.unblockMember(c7)
        elif id_select == 8:
            dad.unblockMember(c8)   
        else:
            print("Invalid Input...")    

def child_options(child_id):
    """
    Function that is an extension of the startChild() function. This function included the operations
    a Child instance can perform. A Child can choose to either spend less than $50 or spend more than
    $50 by calling the corresponding functions. Any time a child wants to spend money, the amount
    required is always checked with the available balance in the wallet.

    In the special case a child wants to spend more than $50, the request is transferred to Mom, who
    can then decide to accept, reject, or transfer the request to Dad.

    child_id (int) - Parameter that hold the ID of a child instance. Can be any value from 1 to 8 denoting the position of child.
    """
    child_choice = int(input(f"Hello Child{child_id}, what do you need?:\n1. Spend upto $50\n2. Spend more than $50\nEnter here: "))
    if child_choice == 1: # Child can choose to withdraw less than $50
        less_than_fifty = int(input("Great! Please enter an amount upto $50: "))
        if Parent.balanceCheck(less_than_fifty): # Check if money is available
            if less_than_fifty <= 50:
                # Accessing Child'X' by indexing the tuple with the corresponding ID and subracting one because indexes start from 0 for tuples
                child_tuple[child_id-1].spendFifty(less_than_fifty)
            else:
                print("Sorry, you have an entered amount greater than $50. Please try again later.")
        else:
            print(f"Not enough balance in wallet to withdraw ${less_than_fifty}. Available balance is ${BankWallet.wallet_balance}")
            print("Do you want to request a Parent to deposit money?")
            child_deposit_request = input("1. Enter 'y' to send request\n2. Enter 'n' to cancel: ")
            if child_deposit_request == 'y':
                # Child can request Parent to deposit money to the wallet if there is not enough money to withdraw
                print(Parent.depositRequest(child_tuple[child_id-1].name))
            else:
                print("OK")
                return

    elif child_choice == 2: # Child can choose to withdraw more than $50
        more_than_fifty = int(input("OK. Please enter an amount more than $50: "))
        if Parent.balanceCheck(more_than_fifty):
            child_tuple[child_id-1].spendMFifty(more_than_fifty)
        else:
            print(f"Not enough balance in wallet to withdraw ${more_than_fifty}. Available balance is ${BankWallet.wallet_balance}")
            print("Do you want to request a Parent to deposit money?")
            child_deposit_request = input("1. Enter 'y' to send request\n2. Enter 'n' to cancel")
            if child_deposit_request == 'y':
                print(Parent.depositRequest(child_tuple[child_id-1].name))
            else:
                print("OK")
                return

# calling the welcome() function to start the program
welcome()
