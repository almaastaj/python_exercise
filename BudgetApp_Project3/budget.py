class Category:
  """instantiate objects based on different budget categories like food, clothing, and entertainment. When objects are created, they are passed in the name of the category.The class should have an instance variable called ledger that is a list."""
  def __init__(self,name):
    self.name = name
    self.ledger= list()
    self.total_withdrawal = 0
    
  """A title line of 30 characters where the name of the category is centered in a line of * characters.
A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
A line displaying the category total. """ 
  def __repr__(self):
    title = self.name.center(30,'*') 
    desc = ""
    final_total =0
    for item in self.ledger:
      desc += item["description"][:23].ljust(23) + f"{item['amount']:>7.2f}" +'\n'
      final_total += item['amount']
    output = title + '\n' + desc + "Total: " + f"{final_total:.2f}"
    return output
    
  """A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}."""   
  def deposit(self,amount,description =""):
    self.ledger.append({"amount": amount, "description": description})
    
  """A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise."""
  def withdraw (self,amount,description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      self.total_withdrawal += amount
      return True
    return False

  """A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred."""
  def get_balance(self):
    total =0
    for item in self.ledger:
      total += item["amount"]
    return total

  """A transfer method that accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise."""  
  def transfer (self,amount,category):
    if self.check_funds(amount):
      self.withdraw(amount, "Transfer to " + category.name)
      category.deposit(amount,"Transfer from " + self.name)
      return True
    return False

  """A check_funds method that accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method."""
  def check_funds(self,amount):
    if self.get_balance() >= amount:
      return True
    return False
"""Besides the Category class, create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument. It should return a string that is a bar chart.

The chart should show the percentage spent in each category passed in to the function. The percentage spent should be calculated only with withdrawals and not with deposits. Down the left side of the chart should be labels 0 - 100. The "bars" in the bar chart should be made out of the "o" character. The height of each bar should be rounded down to the nearest 10. The horizontal line below the bars should go two spaces past the final bar. Each category name should be written vertically below the bar. There should be a title at the top that says "Percentage spent by category"."""    
def create_spend_chart(categories):
  line =''
  total_with =0
  longest = 0
  head = 'Percentage spent by category\n'
  # for looping the categories and getting total withdrawal of the given categories and longest category name
  for cat in categories:
    total_with += cat.total_withdrawal
    if len(cat.name) > longest:
      longest = len(cat.name)
  # loop through 100 - 0 and right indent to 4 spaces    
  for n in range(100,-10,-10):
    line += f"{str(n) +'|':>4}"
    # calculate each percentage by looping the categories
    for cat in categories:
      percent = ((cat.total_withdrawal/total_with*100))
     # if percent > number then " o " else "   "
      if percent >= n:
        line += f" {'o'} "
      else:
        line += "   "
    line += ' \n'
    # for number of dashes = no. of terms in categories list * 3 +1 
  length = len(categories)
  dash = f"    {'-'*(3*length +1)}"
  i=0
  let ='    '
  #looping categories to get each char of categories.name and cap it at longest length of the name and in case of no char use "   "
  while i< longest:
    for cat in categories:
      try:
        let += f" {cat.name[i]} "
      except:
        let += "   "
    i = i +1
    let += ' '
    # for proper arrangement with test case
    if i != longest:
      let += '\n    '
   # final bar graph 
  graph = head + line + dash +'\n' + let
  return graph


  
      
      



    
  
