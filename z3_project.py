from z3 import *

# Boolean variables
Music = Bool('Music')
Sports = Bool('Sports')
Gmail = Bool('Gmail')

# Logical condition:
# Active student = (Music OR Sports) AND Gmail
Active = And(Or(Music, Sports), Gmail)

s = Solver()
s.add(Active)

print(s.check())  # Checks if condition is satisfiable