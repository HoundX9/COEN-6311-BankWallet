# COEN-6311-BankWallet
A mini-project on a family bank wallet for COEN 6311.
### Introduction
The repository contains the source code and related UML Diagrams for the mini-project for COEN 6311 - Software Engineering. The main.py file is to be run to start the program whose interactions will be done via the console/terminal/shell. The source code also contains a pcbw.py file that is a module which contains the necessary classes and related operations of the three different users who will be able to interact with the bank wallet - Dad, Mom, and Child.

### Types of User Interactions
The operations of the three users are fairly straightforward. Both Dad and Mom and deposit and withdraw money and read all the transactions made with the bank wallet, but the Dad has special access to block or unblock a member (Mom or Child) from accessing the wallet. 

A Child on the other hand, although only has the option to withdraw money, they would have to get their access request granted by a Parent (Dad or Mom) before being able to proceed. A Child may choose to request a withdrawal of upto $50 or more than $50, in which case they would have to get their access granted by Mom who can decide to either accept, reject or transfer the request to Dad. In case there isn't enough money for withdrawal, a Child may request a Parent to deposit some money into the bank wallet.

A Child, whose access was denied twice will not be able to access the wallet until the current execution in terminated (the program has to start again before they may be able to access the wallet).

### UML Diagrams
Four diagram types have been used to depict the various types of interactions involved created using StarUML2.0 - Use Case Diagram, Flowchart Diagram, Class Diagram and Sequence Diagram all of which havee been uploaded to the repository for viewing.

#### Activity Plan and Report
A detailed table showing the activity report followed has been uploaded to the repository as well.
