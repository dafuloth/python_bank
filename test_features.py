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

  expected = "date".ljust(11) + "|| credit".ljust(11) + "|| debit".ljust(11)
  expected += "|| balance\n"

  expected += "29/04/2019".ljust(11) + "||".ljust(11) + "|| 225.00".ljust(11) + "|| 1275.00\n"
  expected += "26/04/2019".ljust(11) + "|| 1500.00".ljust(11) + "||".ljust(11) + "|| 1500.00\n"

  print(expected)

  expected = capsys.readouterr()

  expected_output = expected.out

  print_account.print_statement()

  actual = capsys.readouterr()
  actual_output = actual.out

  assert expected_output == actual_output