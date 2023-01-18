import numpy as np
import database

class Topsis():
  def __init__(self):
    self.sqlite = database.SQLite3()