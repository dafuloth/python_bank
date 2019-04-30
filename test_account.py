import pytest
import account

def test_account():
  my_account = account.Account()
  assert my_account.balance == 0

def test_open_account_with_balance():
  my_account = account.Account(1000)
  assert my_account.balance == 1000

def test_deposit():
  my_account = account.Account()
  my_account.deposit("29-04-2019", 425)
  assert my_account.balance == 425

def test_withdraw():
  my_account = account.Account(1000)
  my_account.withdraw("30-04-2019", 350)
  assert my_account.balance == 650

