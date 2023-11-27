#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items = []
    self.last_transaction = 0 
  
  
  def add_item(self, item_name, price, optional_quantity=1):
    self.last_transaction = self.total 
    self.total += price * optional_quantity
    for item in range(optional_quantity):
      self.items.append(item_name)

    
  def apply_discount(self):
    if (self.discount != 0):
      self.total -= int(self.total * (self.discount / 100))
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print("There is no discount to apply.")
  
  def void_last_transaction(self):
    self.total = self.last_transaction

  