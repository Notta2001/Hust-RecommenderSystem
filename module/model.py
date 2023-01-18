import numpy as np
from module.database import SQLite3

class Topsis():
  def __init__(self, criteria_list):
    self.sqlite = SQLite3()
    self.evaluation_matrix = np.array([]) # M*N matrix
    self.normalized_decision = np.array([])
    self.weight = np.zeros(7) # N matrix weight
    self.row_size = 0
    self.column_size = 0
    self.criteria_list = np.array(criteria_list)

  def caculate_weight(self, preferential_list):
    i = 0
    for criteria in self.criteria_list:
      criteria_index = preferential_list.index(criteria)
      self.weight[i] = 7 - criteria_index
      i = i + 1
    self.weight = self.weight/sum(self.weight)
    # print(self.weight)
  
  def caculate_evaluation_matrix(self, student_infor):
    i = 0

  def normalized_score(self):
    self.normalized_decision = np.copy(self.evaluation_matrix)
    self.row_size = len(self.evaluation_matrix)
    self.column_size = len(self.evaluation_matrix[0])
    sqrd_sum = np.zeros(self.column_size)
    for i in range(self.row_size):
      for j in range(self.column_size):
        sqrd_sum[j] += self.evaluation_matrix[i, j]**2
    
    for i in range (self.row_size):
      for j in range(self.column_size):
        self.normalized_decision[i, j] = self.evaluation_matrix[i, j]/(sqrd_sum[j]**0.5)

  def weighted_normalized_score(self):
    for i in range(self.row_size):
      for j in range(self.column_size):
        self.normalized_decision[i, j] *= self.weight[j]

  def find_recommender_list(self):
    self.worst_decision = np.zeros(self.column_size)
    self.best_decision = np.zeros(self.column_size)
    for i in range(self.column_size):
      self.worst_decision[i] = min(self.normalized_decision[:, i])
      self.best_decision[i] = max(self.normalized_decision[:, i])

    #distances to worst and best decision
    self.worst_distance = np.zeros(self.row_size)
    self.best_distance = np.zeros(self.row_size)
    for i in range(self.row_size):
      for j in range(self.column_size):
        self.worst_distance[i] += (self.normalized_decision[i, j] - worst_decision[j])**2
        self.best_distance[i] += (self.normalized_decision[i, j] - best_decision[j])**2

    for i in range(self.row_size):
      self.worst_distance[i] = self.worst_distance[i]**0.5
      self.best_distance[i] = self.bets_distance[i]**0.5

    # caculate similarity
    # self.best_similarity = np.zeros(self.row_size)
    self.worst_similarity = np.zeros(self.row_size)
    for i in range(self.row_size):
      self.worst_similarity[i] = self.worst_distance[i]/(self.worst_distance[i] + self.best_distance[i])
      # self.best_similarity[i] = self.best_distance[i]/(self.worst_distance[i] + self.best_distance[i])

    # ranking
    self.ranking = [i+1 for i in self.worst_similarity.argsort()]
    return self.ranking
    
