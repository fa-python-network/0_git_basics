from pprint import pprint 
matrix = [[0.5,   0,   0,   0,   0],
          [  1, 0.5,   9,   0,   0],
          [  1,   1, 0.5,   60,   0],
          [  1,   10,   1, 0.5,   0],
          [  1,   1,   1,   1, 0.5]]

matrix_t = list(zip(*matrix)) 

pprint(matrix)
pprint(matrix_t)
//транспонирование матрицы