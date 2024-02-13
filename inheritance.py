class Mpesa:
    def __init__(self,Account_balance,Phone_number):
        self.Account_balance = Account_balance
        self.Phone_number = Phone_number
    def send_money(self,amount,recipient):
        if self.Account_balance >=amount:
            self.Account_balance -= amount
            print(f"{amount} KES sent to the {recipient} successfully")
        else:
             print(f"Insufficient funds")

class personal_Mpesa(Mpesa):
    def __init__(self,Account_balance,Phone_number,id_number):
        super().__init__(Account_balance,Phone_number)
        self.id_number = id_number
    def buy_airtime(self,amount):
        if self.Account_balance >= amount:
            self.Account_balance -=amount
            print(f"{amount} KES airtime bought successfully")
        else:
            print(f"Insufficient funds")
class Business_Mpesa(Mpesa):
    def __init__(self,Account_balance,Phone_number,id_number):
        super().__init__(Account_balance,Phone_number)
        self.id_number =id_number
    #     self.lipa_na_mpesa =lipa_na_mpesa
    #     self.buy_goods=buy_goods
    #     self.pochi_la_biashara=pochi_la_biashara
    #
    # def lipa_na_mpesa(self,amount):
    #     if self.Account_balance >=amount:
    #         self.Account_balance -=amount
    #         print(f"{amount} KES sent to till")
    #     else:
    #         print(f"Insufficient funds")
    # def buy_goods(self,amount):
    #     if self.Account_balance >=amount:
    #         self.Account_balance -=amount
    #         print(f"{amount} KES sent to till")
    #     else:
    #         print(f"Insufficient funds")
    # def pochi_la_biashara(self,amount):
    #     if self.Account_balance >=amount:
    #         self.Account_balance -=amount
    #         print(f"{amount} KES sent to till")
    #     else:
    #         print(f"Insufficient funds")
# class Recieve_money(Mpesa):
    def Recieve_money(self,amount):
        self.account_balance =+amount
        print(f"{amount} KES recieved successfully")
    def account_balance(self,amount):
        self.account_balance ==amount
        print(f"Account balance is the remainder%{account_balance}")

personal=personal_Mpesa(500,7707835510,23743933)
personal.buy_airtime(25)
personal.send_money(512,5452747)
# personal.Recieve_money(1000)
busissnes=Business_Mpesa(23000,7474745,23743933)
busissnes.Recieve_money(36900)
busissnes.account_balance()






