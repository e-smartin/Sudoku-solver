import numpy as np
board = [[8, 1, 0, 0, 3, 0, 0, 2, 7], 
            [0, 6, 2, 0, 5, 0, 0, 9, 0], 
            [0, 7, 0, 0, 0, 0, 0, 0, 0], 
            [0, 9, 0, 6, 0, 0, 1, 0, 0], 
            [1, 0, 0, 0, 2, 0, 0, 0, 4], 
            [0, 0, 8, 0, 0, 5, 0, 7, 0], 
            [0, 0, 0, 0, 0, 0, 0, 8, 0], 
            [0, 2, 0, 0, 1, 0, 7, 5, 0], 
            [3, 8, 0, 0, 7, 0, 0, 4, 2]]
"""
board = [[0,4,3,0,8,0,2,5,0]
           ,[ 6,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,1,0,9,4],
            [9,0,0,0,0,4,0,7,0],
            [0,0,0,6,0,8,0,0,0],
            [0,1,0,2,0,0,0,0,3],
            [8,2,0,5,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,5],
            [0,3,4,0,9,0,7,1,0]] 
"""

board = np.array(board)
def print_sudoku(b):
    if b is None:
        print("There's no board 2 print")
        return
    line = "-"*25
    rows, cols = b.shape
    for i in range(rows):
        #separate matrix every 3 rows
        if not i % 3 :
            print(line)
        sudoku_row = ""
        for j in range(cols):
            #separate matrix every 3 cols
            if not j % 3 :
                sudoku_row += "| "
            sudoku_row += str(b[i,j])+" " if b[i,j] else "  "
        print(sudoku_row + "|")
    print(line)

#def getMatrixPos(i,j):
#    def retPos(a):
#        if a %3 ==0:
#            pos1 = a+1
#            pos2 = a+2
#        if a %3 ==1:
#            pos1 = a-1 
#            pos2 = a+1
#        if a % 3 == 2:
#            pos1 = a-2 
#            pos2 = a-1
#
#        return [pos1,pos2]
#    row1,row2 = retPos(i)
#    col1,col2 = retPos(j)
#    return [row1,row2,col1,col2]

def solve_sudoku(b):
    solvable = True 
    #do while there r values 2 find
    while(solvable):
        onzeros = b.size - np.count_nonzero(b) 
        rows,cols = b.shape
        
        #check each elment
        for i in range(rows):
            for j in range(cols):
                #skip not 0 boxes
                if (b[i,j]):
                    continue
                def getMatrix(aa,bb):
                    rmin = aa // 3 * 3
                    cmin = bb // 3 * 3 
                    return [rmin,cmin]
                rmin, cmin = getMatrix(i,j)
                matrix_3p3 = b[rmin:rmin+3, cmin:cmin+3]
                matrix = np.concatenate((matrix_3p3[0],matrix_3p3[1],matrix_3p3[2]), axis = None)
                #r1,r2,c1,c2 = getMatrixPos(i,j)
                #rs = np.array([r1,r2,i]) #rows
                #cs = np.array([c1,c2,j]) #cols
                ##getMatrix
                #matrix = np.empty([rs.size,cs.size], dtype = int)
                #for s in range(rs.size):
                #    for m in range(cs.size):
                #        matrix[s,m] = b[rs[s],cs[m]]
                #matrix = np.concatenate((matrix[0],matrix[1],matrix[2]), axis = None)

                for num in range(1,10):
                    #num already in row,col or matrix
                    if num in b[i,:] or num in b[:,j] or num in matrix:
                        continue

                    #check if num is in the rest of rows and columns that have empty values | MATRIX
                    c = True
                    c2 = True
                    for ss in range (3):
                        #check elements of other rows rn't empty or num is already in that row, also check same condition 4 elements in the same row.
                        c = c and ((num in b[ss + rmin,:] or np.count_nonzero(matrix_3p3[ss,:]) == 3 ) if rmin + ss != i else True)#row 
                        c = c and ((num in b[:,ss + cmin] or matrix_3p3[i-rmin,ss] != 0 ) if cmin + ss != j else True)#element of same row

                        c2 = c2 and ((num in b[:,ss + cmin] or np.count_nonzero(matrix_3p3[:,ss]) == 3 ) if cmin + ss != j else True)#col 
                        c2 = c2 and ((num in b[ss + rmin,:] or matrix_3p3[ss,j-cmin] != 0 ) if rmin + ss != i else True)#element of same col
                    if (c or c2):
                        #num must be in this pos
                        b[i,j] = num
                        break

                    c = True
                    c2 = True
                    for ss in range (9):
                    #check if num can fit in the rest of elements of the row | ROW
                        if ss == j :
                            continue
                        
                        brmin, bcmin = getMatrix(i,ss)
                        bmatrix_3p3 = b[brmin:brmin+3, bcmin:bcmin+3]
                        bmatrix = np.concatenate((bmatrix_3p3[0],bmatrix_3p3[1],bmatrix_3p3[2]), axis = None)
                        c2 = c2 and (num in b[:,ss] or b[i,ss]!=0 or num in bmatrix)

                    for ss in range (9):
                    #check if num can fit in the rest of elements of the col | COLUMN
                        if ss == i :
                            continue
                        
                        brmin, bcmin = getMatrix(ss,j)
                        bmatrix_3p3 = b[brmin:brmin+3, bcmin:bcmin+3]
                        bmatrix = np.concatenate((bmatrix_3p3[0],bmatrix_3p3[1],bmatrix_3p3[2]), axis = None)
                        c = c and (num in b[ss, :] or b[ss,j]!=0 or num in bmatrix)
                       
                    if (c or c2):
                        #num must be in this pos
                        b[i,j] = num
                        break

                    if num not in b[i,:] and np.count_nonzero(b[i,:]) == 8 or num not in b[:,j] and np.count_nonzero(b[:,j]) == 8 or num not in matrix and np.count_nonzero(matrix) == 8:
                        b[i,j] = num
                    #print(num in b[i,:])
                    #print(b[:,j])
                #print(b[i,j])
                 
        enzeros = b.size - np.count_nonzero(b) 
        if not enzeros:
            print("Correctly solved")
            solvable = False
            print_sudoku(b)
        if not ( enzeros - onzeros ) :
            solvable = False
            print("Not solvable")
            return
#show sudoku before solving it
print_sudoku(board)
#solve sudoku n show solution
solve_sudoku(board)

