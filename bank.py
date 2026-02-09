

from datetime import datetime, timedelta
import time

class BankAccount:
    def __init__(self, account_id, fullname_owner, balance):
        self.account_id = account_id
        self.fullname_owner = fullname_owner
        self.balance = balance
        self.created_at = datetime.now()

b1 = BankAccount(8676230, 'arya stark', 280000)
b2 = BankAccount(5979982, 'jon snow', 79011)
bg = BankAccount(6875533, 'golum', -28000)

print(b1)
print(b2)
print(b1 - b2)
print(b1 + b2)
print(b1 * b2)
print(b1 / b2)  # / (truediv) // (floordiv)
print(b1 // b2)  # / (truediv) // (floordiv)
print('min', min(b1, b2))
print('max', max(b1, b2))
print(b1 > b2)
print(b1 >= b2)
print(b1 <= b2)
print(b1 == b2)
print(b1 != b2)
print(abs(bg))

time.sleep(3)
print(len(b1))  #  **etgar: how long does this account exist in seconds