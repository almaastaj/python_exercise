class Rectangle:
  """initialized with width and height attributes."""
  def __init__(self,width,height):
    self.width = width
    self.height = height
  """Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10)"""
  def __repr__(self):
    line = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    return line
  
  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2*self.width + 2* self.height)

  def get_diagonal(self):
    return ((self.width ** 2 + self.height **2)**0.5)
  """Returns a string that represents the shape using lines of "*". The number of lines should be equal to the height and the number of "*" in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: "Too big for picture."."""
  def get_picture (self):
    line = ''
    for i in range(self.height):
      if (self.height <= 50 and self.width <= 50):
        line += "*"*self.width + '\n'
      else:
        line = "Too big for picture."
    return line
  """Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4."""
  def get_amount_inside(self,shape):
    amount = int(self.height / shape.height)* int(self.width/shape.width)
    return amount

"""The Square class should be a subclass of Rectangle. """    
class Square(Rectangle):
  """a single side length is passed in. The __init__ method should store the side length in both the width and height attributes from the Rectangle class."""
  def __init__(self,side):
    self.width = side
    self.height = side
  """If an instance of a Square is represented as a string, it should look like: Square(side=9)"""
  def __repr__(self):
    line = "Square(side=" + str(self.width)  + ")"
    return line

  def set_side(self,side):
    self.width = side
    self.height = side

  def set_width(self,side):
    self.width = side
    self.height = side

  def set_height(self,side):
    self.width = side
    self.height = side

  
