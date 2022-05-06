## Create a Triangle class that accepts three side-lengths of the triangle a,b and c as parameters at the time of object creation. Class triangle should have the following methods:

<ul>
  <bold>
    <li>  is_valid() : To check validity of the triangle
      <li> Side_Classification() : To return the type of triangle - Isosceles, Equilateral or Scalene
        <li> Angle_Classification(): To return type of triangle - right, obtuse or acute
          <li> Area(): To return area of the triangle
  </bold>
</ul>

## Code:
<pre>
<p>
import math

class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def Is_valid(self):
        self.temp = False
        if self.a + self.b > self.c:
            if self.b + self.c > self.a:
                if self.c + self.a > self.b:
                    self.temp = True
        if self.temp:
            return('Valid')
        else:
            return('Invalid')
            
     def Side_Classification(self):
        if self.temp:
            if self.a == self.b == self.c:
                return ('Equilateral')
            elif self.a == self.b or self.b == self.c or self.c == self.a:
                return ('Isosceles')
            else:
                return ('Scalene')
        else:
            return (self.Is_valid())
  
    def Angle_Classification(self):
        if self.temp:
            ls = [self.a, self.b, self.c]
            max_angle = max(ls)
            min_angle = min(ls)
            ls.remove(max_angle)
            ls.remove(min_angle)
            mid_angle = ls[0]
                
            if min_angle**2 + mid_angle**2 == max_angle**2:
                return ('Right')
            elif  min_angle**2 + mid_angle**2 > max_angle**2:
                return ('Acute')
            elif  min_angle**2 + mid_angle**2 < max_angle**2:
                return ('Obtuse')
        else:
            return (self.Is_valid())
 
    def Area(self):
        if self.temp:
            t_sum = (self.a + self.b + self.c)/2
            triangle_area = math.sqrt(t_sum*(t_sum - self.a)*(t_sum-self.b)*(t_sum - self.c))
            return triangle_area
        
        else:
            return (self.Is_valid())   

a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())
</p>    
</pre>  
     
