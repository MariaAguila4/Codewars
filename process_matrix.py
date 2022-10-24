

matrix = [[4,5,3],[6,5,6],[7,8,9]]
def find_neighbours(matrix):

    neighbors = []
    #print(matrix)
    rows=len(matrix)
    cols=len(matrix[0])
    pepe = [[]] # initialize Matrix for

    for i in range(len(matrix)):
        for j, value in enumerate(matrix[i]):
            neighbors = []
            if (i == 0 or i == len(matrix) - 1 or j == 0 or j == len(matrix[i]) - 1): # corners of matrix weird cases
                if i != 0: # top neighbor 
                    neighbors.append(matrix[i - 1][j])
                if j != len(matrix[i]) - 1: # right neighbor
                    neighbors.append(matrix[i][j + 1])
                if i != len(matrix) - 1:# bottom neighbor
                    neighbors.append(matrix[i + 1][j])
                if j != 0:# left neighbor
                    neighbors.append(matrix[i][j - 1])

            else:
                # add neighbors arround value
                neighbors = [
                    matrix[i - 1][j],  # top 
                    matrix[i][j + 1],  # right 
                    matrix[i + 1][j],  # bottom 
                    matrix[i][j - 1]   # left 
                ]
            neighbors.append(value)  # add the value itself
            avg_value = sum(neighbors) / len(neighbors) # average of value
            #print("average",value,neighbors, avg_value)
            pepe[i].append((round(avg_value,3))) # add average of 3 decimals to list

        if (i < len(matrix)-1):
          pepe.append([]) # create a new list ("[]") inside of list

    return pepe
matrix = [[4,5,3,4],
          [6,2,0,1],
          [7,-1,7,8],
          [3,2,9,6],
          [3,4,2,6],
          [2,2,4,1]]
nei =(find_neighbours(matrix))
print(nei)
""""
for i in range(rows):
    for j in range(cols):
        #print("i i j",i,j)
        pepe = (i) , (j)
        coordi.append(pepe)
        if(i == 0 and j == 0):
          pass
          

print(coordi)"""