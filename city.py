from math import hypot
import sys

def read_cities():
  """Reads in cities from the standard input,
  and returns a list of these cities"""

  cities = []

  for line in sys.stdin:
    x, y = line.split()
    cities += [city((int(x), int(y)))]

  return cities

def total_distance(route):
  """Calculates the total distance taken by the route"""
  d = 0
  for i in range(len(route) - 1):
    d += distance(route[i], route[i + 1])

  return d

def route_cmp(route_a, route_b):
  """Returns -1 if route_a < route_b, 0 if they are equal, and 1 if
  route_a > route_b"""
  if (route_a < route_b): return -1
  elif(route_a == route_b): return 0
  else: return 1

def distance(a, b):
  """Returns the distance between two cities, a and b"""
  return hypot(a.x - b.x, a.y - b.y)

class city:
  def __init__(self, (x, y)):
    """Initializes the city"""
    self.x = x
    self.y = y
  def __repr__(self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'
