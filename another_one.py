import csv
class BankAccount:

    def __init__(self, bank_name, atm_name):
        self.balance = 0
        self.bank_name = bank_name
        self.atm_name = atm_name

    def withdraw(self, amount_i_want_to_withdraw):
        if self.balance < amount_i_want_to_withdraw:
            self.balance = 0
        else:
            self.balance = self.balance - amount_i_want_to_withdraw

    def deposit(self, amount_i_want_to_deposit):
        self.balance = self.balance + amount_i_want_to_deposit

    def __repr__(self):
        return f"Balance in {self.bank_name} / {self.atm_name}: {self.balance}"


# account_name = input("Account Name: ")
# atm_name = input("ATM Name: ")
# b1 = BankAccount(account_name, atm_name)
# b1.deposit(5000)
# b1.withdraw(100)

# try:
# except:
#     print("Cannot divide by 0")

data = [
    {"water": 10, "fire": 20, "air": 70, "dirt": 10},
    {"water": 10, "fire": 20, "air": 70, "dirt": 10},
    {"water": 10, "fire": 20, "air": 70, "dirt": 10},
    {"water": 10, "fire": 20, "air": 70, "dirt": 10},
    {"water": 10, "fire": 20, "air": 70, "dirt": 10},
    {"water": 10, "fire": 20, "air": 70, "dirt": 10},
]

# keys = data[0].keys()
# with open("test.csv", "w", newline="") as output_file:
#     dict_writer = csv.DictWriter(output_file, keys)
#     dict_writer.writeheader()
#     dict_writer.writerows(data)

input_file = csv.DictReader(open("test.csv"))
print(input_file)
for i in input_file:
    print(i)
# with open("test.csv") as fp:
#     reader = csv.reader(fp, delimiter=",", quotechar='"')
#     # data_read = [row  for row in reader]
#     for row in reader:
#         l.append(row)
# print(l)