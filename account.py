from datetime import datetime

class Account(object):
  balance = 0
  transaction_log = []
  def __init__(self, opening_balance = 0):
    self.balance += opening_balance

  def deposit(self, date, amount):
    date_object = datetime.strptime(date, "%d-%m-%Y")
    self.balance += amount
    self.transaction_log.append((date_object.day, date_object.month, date_object.year, amount, "", self.balance))

  def withdraw(self, date, amount):
    date_object = datetime.strptime(date, "%d-%m-%Y")
    self.balance -= amount
    self.transaction_log.append((date_object.day, date_object.month, date_object.year, "", amount, self.balance))

  
  def print_statement(self):
    statement = "date       || credit  || debit   || balance\n"
    for transaction in reversed(self.transaction_log):
      date = str(transaction[0]) + "/" + str(transaction[1]).rjust(2,'0') + "/" + str(transaction[2])
      
      statement += date.ljust(11) + "|| "

      if transaction[3]=="":
        statement += transaction[3].ljust(8) + "|| "
      else:
        statement += ("%.2f" % transaction[3]).ljust(8) + "|| "
    
      if transaction[4]=="":
        statement += transaction[4].ljust(8) + "|| "
      else:
        statement += ("%.2f" % transaction[4]).ljust(8) + "|| "  
    
      statement += ("%.2f" % transaction[5]) + "\n"

    print(statement)
  