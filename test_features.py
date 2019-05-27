import pytest
import account

def test_deposit_money_into_account():
  my_account = account.Account()
  my_account.deposit("26-04-2019", 500)
  assert my_account.balance == 500

def test_withdraw_money_from_account():
  my_account = account.Account()
  my_account.deposit("26-04-2019", 500)
  my_account.withdraw("29-04-2019", 225)
  assert my_account.balance == 275

def test_print_statement(capsys):

  print_account = account.Account()
  print_account.deposit("26-04-2019", 1500)
  print_account.withdraw("29-04-2019", 225)

  expected = """date       || credit  || debit   || balance
29/04/2019 ||         || 225.00  || 1275.00
26/04/2019 || 1500.00 ||         || 1500.00"""
# 29/04/2019 ||         || 225.00  || 1275.00
# 26/04/2019 || 1500.00 ||         || 1500.00

  print_account.print_statement()

  actual = capsys.readouterr()

  actual_output = actual.out

  assert actual_output.startswith(expected)