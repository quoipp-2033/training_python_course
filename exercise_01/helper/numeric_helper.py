class NumericChecker:
  def __init__(self):
    return
  def isfloat(self, value):
      try:
          float(value)
          return True
      except ValueError:
          return False
  def quantityCheck(self, value):
      try:
          int(value)
          if (value < 0):
            return False
          return True
      except ValueError:
          return False
