import pytest
import account
from account import Account


class TestAccount:
    self = account
    a1 = Account('John')
    def test___init__(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == pytest.approx(0)

    def test_deposit(self):

        assert self.a1.deposit(-2) is False #negative
        assert self.a1.get_balance() == pytest.approx(0)

        assert self.a1.deposit(0) is False  # 0
        assert self.a1.get_balance() == pytest.approx(0)

        assert self.a1.deposit(2) is True  # positive
        assert self.a1.get_balance() == pytest.approx(2)


    def test_withdraw(self):

        assert self.a1.withdraw(-4) is False  # negative
        assert self.a1.get_balance() == pytest.approx(2)

        assert self.a1.withdraw(0) is False  # 0
        assert self.a1.get_balance() == pytest.approx(2)

        assert self.a1.withdraw(4) is False  # 0
        assert self.a1.get_balance() == pytest.approx(2)

        assert self.a1.withdraw(2) is True  # positive
        assert self.a1.get_balance() == pytest.approx(0)


if __name__ == '__main__':
    pytest.main()