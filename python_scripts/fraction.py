class Fraction:
  def __init__(self, num, denom=1):
    assert (type(num) is int and num != 0) or num.__class__.__name__ == "Fraction", "Wrong type for numerator"
    assert (type(denom) is int and denom != 0) or denom.__class__.__name__ == "Fraction", "Wrong type for denominator"

    if type(num) is int and type(denom) is int:
      pass
    elif type(num) is int and denom.__class__.__name__ == "Fraction":
      num = num * denom.denom
      denom = denom.num
    elif num.__class__.__name__ == "Fraction" and type(denom) is int:
      num = num.num
      denom = num.denom * denom
    else:
      num, denom = num.num * denom.denom, num.denom * denom.num

    def get_gcd():
      # Let's handle negative values here
      # Also, right now it won't reduce negative values!
      # because range(1,-10) == []
      x = 1
      for n in range(1, min(num, denom)+1):
        if num % n == 0 and denom % n == 0:
          x = n
      return x

    gcd = get_gcd()
    self.num = num/gcd
    self.denom = denom/gcd

  def __mul__(self, other):
    return Fraction(self.num * other.num, self.denom * other.denom)

  def __div__(self, other):
    return Fraction(self.num * other.denom, self.denom * other.num)

  def __add__(self, other):
    return Fraction(self.num * other.denom + self.denom * other.num, self.denom * other.denom)

  def __sub__(self, other):
    return self + -other

  def __neg__(self):
    return Fraction(-self.num, self.denom)

  def __eq__(self, other):
    return self.num == other.num and self.denom == other.denom

  def __str__(self):
    return "%s/%s" % (self.num, self.denom)

  def __repr__(self):
    return "Fraction(%s, %s)" % (self.num, self.denom)

# Next step: try to make this work!
# print Fraction(2,Fraction(1, 6))
# print Fraction(2,Fraction(1, 6))

print Fraction(Fraction(1,2),Fraction(3,Fraction(7,Fraction(20))))
print Fraction(1,2) - Fraction(1,8)
print Fraction(1,-2)  # This doesn't behave how we want yet
