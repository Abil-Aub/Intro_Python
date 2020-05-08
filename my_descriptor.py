## >> new_account = Account(0.1)
## >> new_account.amount = 100
## >>
## >> print(new_account.amount)
## 90
## TO-DO
## >> new_account.amount -= 50
## >> new_account.amount
## 35
## >> new_account.amount += 50
## >> new_account.amount
## 80

class Value:
    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        if hasattr(obj, 'commission'):
            self.value = value*(1.0 - obj.commission)
        else:
            self.value = value

class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission
