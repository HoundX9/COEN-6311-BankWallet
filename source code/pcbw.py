"""
======
Module 
======
This module contains the BankWallet, Parent(Dad,Mom) and Child classes

"""
import pandas as pd # import pandas to display ledger as dataframe


class BankWallet:
    """
    This class encompasess attributes and behaviours of a Bank Wallet. The attributes of the class
    include 'bank_acc', 'wallet_balance' and 'ledger' that represent the available balance in joint 
    bank account, the available balance in the bank wallet, and the record of all transactions made
    with the bank wallet respectively.

    The class also defines important methods to update the ledger, display the balances, and notify
    parents when the avaialable balance falls below a certain threshold.

    The 'ledger' attribute is a dictionary with member names as keys and their transactions as a list.
    The first value for every list is the access value of the respective member.
    """
    bank_acc = 5000 # Amount in main bank account
    ledger = {"Dad":[3],"Mom":[2],"Child1":[1],"Child2":[1],"Child3":[1],"Child4":[1],"Child5":[1],"Child6":[1],"Child7":[1],"Child8":[1]} # Initial dictionary that will hold future transactions
    wallet_balance = 1000 # Amount in the wallet

    def updateLedger(mode,amount,member_name, message = ""):
        """
        Function that takes 3 parameters and 1 optional parameters, used for updating the ledger 
        attribute of any new changes (withdrawals or deposits).

        mode (string) - Parameter that has 2 possible values : 'd' or 'w', based on the action of user
        d - deposit action
        w - withdrawal action

        amount (int) - Parameter that holds the amount involved a transaction

        member_name (string - Parameter that holds the name of the user involved in a transaction

        message (optional) - Parameter that holds the details of a transaction input by a user; default value is an empty string ""
        """

        #Access corresponding member by indexing the corresponding key in the ledger dictionary
        if mode == 'd':
            BankWallet.ledger[member_name].append("Deposited $"+str(amount))
        elif mode == 'w':
            BankWallet.ledger[member_name].append("Withdrew $"+str(amount)+" for the following reason: "+message)

    def showBalance():
        """
        Function that displays the available balance in the bank wallet and the connected bank account.
        """
        print(f"Amount in balance: {BankWallet.wallet_balance}\nAmount in connected bank account: {BankWallet.bank_acc}\n")
        return


    def notifyParents():
        """
        Function that displays a warning message whenever money in the wallet falls below $100.
        """
        if BankWallet.wallet_balance < 100:
            print("----BALANCE BELOW $100----ACTION REQUIRED!!----")

    def __str__(self):
        return f"The Bank Wallet has ${BankWallet.wallet_balance} available in the balance and is conntected to a bank account which holds ${BankWallet.bank_acc}"

class Parent:
    """
    The Parent class establishes the attributes and behaviour of the Parent instances including those
    that inherit from this class, namely the Mom and Dad classes. The operations available to this class
    involve depositing money, withdrawing money, checking available balance in wallet, and reading the
    statements or transactions stored in the wallet ledger.
    """
    instance_count = 0
    def __init__(self):
        if Parent.instance_count >= 2: # No more than 2 intances of Parent can be created
            del self
            print("Error : No more parent instances can be created.")
            return
    
    def deposit(user,deposit_input):
        """
        Function to deposit money into the wallet.

        user (obj) - Parameter that refers to the object accessing the Parent.deposit() function

        deposit_input (int) - Parameter that holds the value of the money to be deposited
        """
        BankWallet.wallet_balance += deposit_input # Increase the money in wallet by deposit_input
        print(f"${deposit_input} deposited.")
        print(f"Current Balance in Wallet : ${BankWallet.wallet_balance}.")
        BankWallet.bank_acc -= deposit_input # Decrease the money in bank account by deposit_input
        print(f"Remaining Balance in connected bank account : ${BankWallet.bank_acc}.")
        BankWallet.updateLedger('d',deposit_input,user.name) # Update the ledger after any deposit operation
        print("Thank You.")
    
    def withdraw(user,withdraw_input):
        """
        Function to withdraw money from the bank wallet.

        user (obj) - Parameter that refers to the object accessing the Parent.withdraw() function

        withdraw_input (int) - Parameter that holds the value of the money to be withdrawn
        """
        if Parent.balanceCheck(withdraw_input): # Firstly, check if there is enough balance in wallet to withdraw withdraw_input amount of money
            BankWallet.wallet_balance -= withdraw_input # Decrease the money in the bank wallet by withdraw_input
            print(f"${withdraw_input} withdrawn.")
            message = input("Please enter the purpose of your withdrawal:")
            print(f"Remaining Balance in Wallet : ${BankWallet.wallet_balance}.")
            print(f"Current Balance in connected bank account : ${BankWallet.bank_acc}.")
            BankWallet.updateLedger('w',withdraw_input,user.name,message) # Update ledger after any withdraw operation
            BankWallet.notifyParents() # Notify the parents by displaying a warning message to the console
            print("Thank You.")
        else:
            # Fail message if not enough balance in wallet to withdraw input amount
            print(f"Not enough balance in wallet to withdraw ${withdraw_input}. Available balance is ${BankWallet.wallet_balance}")
        

    def balanceCheck(amt):
        """
        Function that checks if the wallet has enough balance to withdraw given amount.
        Returns True if remaining balance will be positive
        Returns False if remaining balance will be negative

        amt (int) - Paramenter that holds the amount to be withdrawn, which will be checked with the remaining balance in the wallet
        """
        if BankWallet.wallet_balance - amt >= 0:
            return True
        else:
            return False

    def getStatement(self):
        """
        Function that will display all the transactions made in current program lifecycle. Only a 
        Parent instance has access (dad and mom). Can be used to show the entire ledger or only the
        transactions of a particular member.
        """
        print("You can choose to :\n1. View the entire list of transactions ordered by member\n2. View the transactions of a particular member.")
        parent_choice = int(input("Enter your choice here:"))
        if parent_choice == 1:
            # print a dataframe of he ledger for better viewing
            print(pd.DataFrame.from_dict(BankWallet.ledger, orient='index'))
        elif parent_choice == 2:
            # Select particular member id
            member_select = int(input("Which member transactions do you want to see?\n[1] for Dad\n[2] for Mom\n[3-10] for a Child\nEnter here: "))
            if member_select == 1:
                print(BankWallet.ledger["Dad"])
            elif member_select == 2:
                print(BankWallet.ledger["Mom"])
            elif member_select > 2:
                # As the children ids are expected to start from 1 to 8, any input greater than 2 has 2 subtracted before indexing the child instance
                print(BankWallet.ledger["Child"+str(member_select-2)])
            else:
                return "Invalid input."

    def processRequest(child_name, message, child_req_amt):
        """
        Function that processes a request from a child if they choose to spend/withdraw an amount
        less than fifty dollars. Returns one of two possible characters : 

        Return 'y' if a Parent accepts the request
        Return 'n' if a Parent denies the request

        child_name (string) - Parameter that holds the name of the child

        message (string) - Parament that holds the message request from child

        child_req_amt (int) - Paramenter that hold the amount that a child is requesting to withdraw
        """
        print(f"Hello Parent, {child_name} is requesting access to the wallet to spend {child_req_amt} for the following reason: {message}")
        parent_choice = input("1. Press 'y' to grant access\n2. Press 'n' to deny request\nEnter here: ")
        return parent_choice

    def depositRequest(child_name):
        """
        Funtion that processes a child's request for a parent to deposit money into the bank wallet if
        there isn't enough money to withdraw the amount the child wants.

        child_name (string) - Parameter that holds the name of the child requesting a deposit
        """
        print(f"Hello Parent, {child_name} has requested you to make a deposit in the wallet.")
        BankWallet.showBalance() # Display balance to the console
        parent_depost_decision = input("Press 'd' to deposit or 'c' to cancel: ") # choose to deposit or cancel request
        if parent_depost_decision == 'd':
            deposit_amt = int(input("OK. Please enter amount you want to deposit: "))
            # Asks for the parent identity to input as the user of the deposit transaction into the ledger
            parent_identity = input("Should I enter the creditor as Mom or Dad?\nSelect 'm' for Mom or 'd' for Dad: ")
            if parent_identity == 'm':
                mom.deposit(deposit_amt)
            elif parent_identity == 'd':
                dad.deposit(deposit_amt)
            return f"${deposit_amt} has been deposited into the wallet. You may withdraw now."
        else:
            return "Sorry, your parents have refused to deposit money."


class Dad(Parent):
    """
    A child class of the Parent Superclass. The Dad instance can choose to block or unblock a member, 
    or process a request of a child transferred by the Mom.
    """
    dad_instance_count = 0
    def __init__(self,name):
        Parent.__init__(self)
        if Dad.dad_instance_count >= 1: # Only one Dad instance can exist
            del self
            print("Error : There is already a Dad in the Family.")
            return
        self.name = name
        self.access_value = 3 # Determines the access level of User (Dad) - 3 being the highest level see documentation for further detail
        # Increase dad_count and total Parent_count by 1
        Dad.dad_instance_count += 1
        Parent.instance_count += 1

    def __str__(self):
        return f"{self.name} has access value {self.access_value} and can freely use the wallet."

    def blockMember(self,other_member):
        """
        Function which allows the Dad instance to block a member from accessing the wallet by setting
        their access_value attribute to 0.

        other_member (obj) - Parameter that refers to the object (member instance) which will be blocked
        """
        # Block a member from accessing the wallet
        other_member.access_value = 0 # Set access value to 0 meaning = No Access
        print(f"{other_member.name} has been blocked from further access to the wallet.")

    def unblockMember(self,other_member):
        """
        Function which allows the Dad instance to unblock a member from accessing the wallet by setting
        their access_value attribute to 0.

        other_member (obj) - Parameter that refers to the object (member instance) which will be unblocked
        """
        # Unblock a member from accessing the wallet
        if other_member.access_value > 0:
            return f"{other_member.name} already has access."
        elif isinstance(other_member,Mom): # Check if the member is an instance of Mom class
            other_member.access_value = 2
        else:
            other_member.access_value = 1
        print(f"{other_member.name} has been unblocked, and can now access the wallet."    )
    
    def processRequestMom(child_name, child_message, more_than_fifty):
        """
        Function that processes a request from Mom originally requested by a child who wants to spend/
        withdraw more than fifty dollars from the wallet. 

        Returns True if Dad accepts
        Returns False if Dad rejects

        child_name (string) - Parameter that holds the name of the child requesting access

        child_message (string) - Parameter that holds the message of the child requesting access

        more_than_fifty (int) - Parameter that holds the amount requested by the child whose value should be greater than 50
        """
        print(f"Hello Dad, you have been transferred a request from Mom regarding {child_name} who wants to withdraw ${more_than_fifty} for the following reason:\n{child_message}")
        dad_choice = int(input("You can choose one of the following:\n1. Accept\n2. Reject\nEnter your choice here: "))
        if dad_choice == 1:
            return True
        elif dad_choice == 2:
            return False
        else:
            return "Invalid choice"

class Mom(Parent):
    """
    A child class of the Parent Superclass. The Mom instance has only one operation attached which is 
    processing the request of a child who wants to spend more than fifty dollars.
    """
    mom_instance_count = 0
    def __init__(self,name):
        Parent.__init__(self)
        if Mom.mom_instance_count >= 1: # Only one Mom instance can exist
            del self
            print("Error : There is already a Mom in the Family.")
            return
        self.name = name
        self.access_value = 2
        # Increase mom_count and total Parent_count by 1
        Mom.mom_instance_count += 1
        Parent.instance_count += 1

    def __str__(self):
        return f"{self.name} has access value {self.access_value} and has full access except blocking functionality."

    def childRequestAccess(child_name, child_message, more_than_fifty):
        """
        Function that process a request from a child instance who wants to withdraw more than fifty
        dollars from the wallet.Returns an integer which indicates the Mom's decision.

        Returns 1 if Mom accepts
        Returns 2 if Mom rejects
        Returns 3 if Mom wants to transfer/forward the request to Dad

        child_name (string) - Parameter that holds the name of the child requesting access

        child_message (string) - Parameter that holds the message of the child requesting access

        more_than_fifty (int) - Parameter that holds the amount requested by the child whose value should be greater than 50
        """
        print(f"Hello Mom, you have a request from {child_name} to withdraw ${more_than_fifty} for the following reason:\n{child_message}")
        mom_choice = int(input("You can choose one of the following:\n1. Accept\n2. Reject\n3. Transfer Request to Dad\nEnter your choice here: "))
        if mom_choice == 1:
            return 1
        elif mom_choice == 2:
            return 2
        elif mom_choice == 3:
            return 3
        else:
            return "Invalid choice"
        

class Child:
    """
    The Child class involves all operations and attributed related to the behaviour of a child instance.
    An instance of the Child class can spend money less than fifty dollars or more than fifty dollars.
    Every time an instance triggers an operation for withdrawal, access to the wallet is requested from
    a Parent.
    """
    child_instance_count = 0
    def __init__(self,name):
        if Child.child_instance_count >= 9: # Only eight children instances can exist
            del self
            print("Error : There is already a Mom in the Family.")
            return
        self.name = name
        self.access_value = 1 # Attribute to catergorise member based on level of access available
        self.access_deny_count = 0 # Attribute to keep track of number of requests denied
        # Increase child_count by 1
        Child.child_instance_count += 1


    def spendFifty(self,less_than_fifty):
        """
        Function for a child instance to spend an amount less than fifty dollars. First checks with
        a Parent for access then verifies if there is enough balance before proceeding. If a child
        is denied access, the access_deny_count variable is incremented by 1

        less_than_fifty (int) - Parameter that holds the amount the child wants to withdraw
        """
        child_message = input("Please enter the details of your purchase: ")
        # First request access from the Parent
        parent_response = Parent.processRequest(self.name, child_message, less_than_fifty)
        if parent_response == 'y':
            print(f"${less_than_fifty} withdrawn.")
            BankWallet.wallet_balance -= less_than_fifty
            BankWallet.updateLedger('w',less_than_fifty,self.name,child_message)
            BankWallet.notifyParents()
        elif parent_response == 'n':
            print(f"Sorry {self.name}, your request has been denied by a Parent.")
            self.access_deny_count += 1

        

    def spendMFifty(self,more_than_fifty):
        """
        Function for a child instance to spend an amount less than fifty dollars. First checks with
        Mom for access then verifies if there is enough balance before proceeding. If a child
        is denied access, the access_deny_count variable is incremented by 1

        more_than_fifty (int) - Parameter that holds the amount the child wants to withdraw
        """
        child_message = input("Please enter the details of your purchase: ")
        # Request access from Mom for withdrawing more than $50
        mom_repsonse = Mom.childRequestAccess(self.name, child_message, more_than_fifty)
        if mom_repsonse == 1:
            print(f"Hello {self.name}, you have been granted access. Withdrawing ${more_than_fifty}")
            print(f"Remaining Balance in Wallet : ${BankWallet.wallet_balance}.")
            BankWallet.wallet_balance -= more_than_fifty
            BankWallet.updateLedger('w',more_than_fifty,self.name,child_message)
            BankWallet.notifyParents()
        elif mom_repsonse == 2:
            print("Sorry access was denied by Mom.")
            self.access_deny_count += 1
        elif mom_repsonse == 3: # Mom can choose to transfer request to Dad
            dad_response = Dad.processRequestMom(self.name, child_message, more_than_fifty)
            if dad_response :
                BankWallet.wallet_balance -= more_than_fifty
                print(f"Hello {self.name}, you have been granted access. Withdrawing {more_than_fifty}")
                print(f"Remaining Balance in Wallet : ${BankWallet.wallet_balance}.")
                BankWallet.updateLedger('w',more_than_fifty,self.name,child_message)
                BankWallet.notifyParents()
            elif dad_response == False:
                print("Sorry access was denied by Dad.")
                self.access_deny_count += 1

# Creating instances of all users for the bank wallet
dad = Dad("Dad")
mom = Mom("Mom")
c1 = Child("Child1")
c2 = Child("Child2")
c3 = Child("Child3")
c4 = Child("Child4")
c5 = Child("Child5")
c6 = Child("Child6")
c7 = Child("Child7")
c8 = Child("Child8")