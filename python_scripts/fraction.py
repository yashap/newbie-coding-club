class Fraction:
  def __init__(self, num, denom):
    def gcd():
      x = 1
      for n in range(1, min(num, denom)+1):
        if num % n == 0 and denom % n == 0:
          x = n
      return x

    this_gcd = gcd()
    self.num = num/this_gcd
    self.denom = denom/this_gcd

  def __mul__(self, other):
    return Fraction(self.num*other.num, self.denom*other.denom)

  def __div__(self, other):
    return Fraction(self.num*other.denom, self.denom*other.num)

  def __str__(self):
    return "%s/%s" % (self.num, self.denom)

# Next step: try to make this work!
# print Fraction(2,Fraction(1, 6))
