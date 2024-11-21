class atm:
    def _init_(self): #constructor for python
        self.pin=" "
        self.balance=0
        self.menu()
    def menu(self): #self is like this but for each specific object which is calling the class, it uses the address of the object
        user_input=input('''
        choose from below:
        1. to create pin
        2. to deposit
        3. To withdraw
        4. check balance
        5. exit

        ''')
        if user_input==1:
            print("creating pin")
        elif user_input==2:
            print("deposit")
        elif user_input==3:
            print("withdraw")
        elif user_input==4:
            print("check balance")
        else:
            print("exit")