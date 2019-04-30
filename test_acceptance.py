import pytest
import account

def test_acceptance_criteria(capsys):
  test_account = account.Account()
  test_account.deposit("10-01-2012", 1000)
  test_account.deposit("13-01-2012", 2000)
  test_account.withdraw("14-01-2012", 500)


  expected = "date".ljust(11) + "|| credit".ljust(11) + "|| debit".ljust(11)
  expected += "|| balance\n"

  expected += "14/01/2012".ljust(11) + "||".ljust(11) + "|| 500.00".ljust(11) + "|| 2500.00\n"
  expected += "13/01/2012".ljust(11) + "|| 2000.00".ljust(11) + "||".ljust(11) + "|| 3000.00\n"
  expected += "10/01/2012".ljust(11) + "|| 1000.00".ljust(11) + "||".ljust(11) + "|| 1000.00\n"

  test_account.print_statement()
  actual = capsys.readouterr()

  print(expected)
  expected_output = capsys.readouterr()

  assert actual.out == expected_output.out