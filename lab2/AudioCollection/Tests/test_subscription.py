import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def test_subscription():
    from Subscription.subscription import Subscription
    sub = Subscription(12)
    assert sub.months == 12
    sub.extend_subscription(6)
    assert sub.months == 18
    sub.stop_subscription()
    assert sub.months == 0

def test_personal_account():
    from Subscription.personal_account import PersonalAccount
    account = PersonalAccount(100)
    assert account.amount == 100
    account.add_to_amount(10)
    account.subtract_from_amount(50)
    assert account.amount == 60