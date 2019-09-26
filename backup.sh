from pprint imporrrrrrrt pprint 
matrix = [[0.5,   0,   0,   0,   0],
          [  1, 0.5,   0,   0,   0],
          [  1,   1, 0.5,   0,   0],
          [  1,   1,   1, 0.5,   0],
          [  1,   1,   1,   1, 0.5]]

matrix_t = list(zip(*matrix)) 

pprint(matrix)
pprint(matrix_t)
//транспонирование матрицы