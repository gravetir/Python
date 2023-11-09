class Matrix:
    
    def __init__(self, matrix):
        self.matrix = matrix
        
    def __len__(self):
        return len(self.matrix)
    
    def __repr__(self):
        return str(self.matrix)
    


    def __add__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = []
            for i in range(len(self.matrix)):
                s = []
                for j in range(len(self.matrix[0])):
                    try:  
                        s.append(self.matrix[i][j] + other)
                    except(AttributeError) as e:
                        print('Ошибка при сложении')
                result.append(s)
            pass
        else:
            result = []
            for i in range(len(self.matrix)):
                s = []
                for j in range(len(self.matrix[0])):
                    try:
                        s.append(self.matrix[i][j] + other.matrix[i][j])
                    except(AttributeError) as e:
                        print('Ошибка при сложении')
                result.append(s)

        return Matrix(result)



    def __sub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = []
            for i in range(len(self.matrix)):
                s = []
                for j in range(len(self.matrix[0])):
                    try:  
                        s.append(self.matrix[i][j] - other)
                    except(AttributeError) as e:
                        print('Ошибка при вычитание')
                result.append(s)
            pass
        else:
            result = []
            for i in range(len(self.matrix)):
                s = []
                for j in range(len(self.matrix[0])):
                    try:
                        s.append(self.matrix[i][j] - other.matrix[i][j])
                    except(AttributeError) as e:
                        print('Ошибка при вычитание')
                result.append(s)

        return Matrix(result)



    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = []
            for i in range(len(self.matrix)):
                s = []
                for j in range(len(self.matrix[0])):
                    try:  
                        s.append(self.matrix[i][j] * other)
                    except(AttributeError) as e:
                        print('Ошибка при умножении')
                result.append(s)
            pass
        else:
            result = []
            for i in range(len(self.matrix)):
                s = []
                for j in range(len(self.matrix[0])):
                    try:  
                        s.append(self.matrix[i][j] * other.matrix[i][j])
                    except(AttributeError) as e:
                        print('Ошибка при умножении')
                result.append(s)

        return Matrix(result)




    def __truediv__(self, other):
        result = []
        if isinstance(other, int) or isinstance(other, float):
            result = []
            for i in range(len(self.matrix)):
                s = []
                for j in range(len(self.matrix[0])):
                    try:  
                        s.append(self.matrix[i][j] / other)
                    except(AttributeError) as e:
                        print('Ошибка при делении')
                result.append(s)
            pass
        else:
            for i in range(len(self.matrix)):
                s = []
                for j in range(len(self.matrix[0])):
                    try:
                        s.append(self.matrix[i][j] / other.matrix[i][j])
                    except(ZeroDivisionError) as e:
                        print('Ошибочка')
                result.append(s)

        return Matrix(result)
    
    
    
    
    def T(self):
        transpose_matrix = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        
        return Matrix(transpose_matrix)
    
    
    
    def __matmul__(self,other):
        # result=[]
        # for i in range(len(self.matrix)):
        #     for j in range(len(other.matrix[0])):
        #         sum=[]
        #         for k in range(len(self.matrix[0])):
        #             sum=self.matrix[i][k]*other.matrix[k][j]
        #             result.append(sum)
        result = [[sum(self.matrix[i][k] * other.matrix[k][j] for k in range(len(self.matrix[0])))
                   for j in range(len(other.matrix[0]))]
                  for i in range(len(self.matrix))]

                    
                
            
        return Matrix(result)
        # (self.matrix[i][j]*other.matrix[i][j])*(1/self.matrix[i][j]*other.matrix[i][j]*matrix.T()[i][j])



    def __str__(self):
        return "\n".join([" ".join([str(val) for val in row]) for row in self.matrix])
    
    
    


    def vector_scalyr(v1, v2):
        r = 0
        for i in range(len(v2[0])):
            r += v1[0][i] * v2[0][i]
        return r
    def basic(self):
        v1,v2,v3,v4=self.T().matrix

        f1 = v1

        f2 = (Matrix(v2) - (Matrix(f1)*(Matrix.vector_scalyr(v2,f1) / Matrix.vector_scalyr(f1,f1)))).matrix

        f3 = (Matrix(v3) - (Matrix(f1)*(Matrix.vector_scalyr(v3,f1) / Matrix.vector_scalyr(f1,f1))) -
                            (Matrix(f2)*(Matrix.vector_scalyr(v3,f2) / Matrix.vector_scalyr(f2,f2)))).matrix
        
        f4 = (Matrix(v4) - (Matrix(f1)*(Matrix.vector_scalyr(v4,f1) / Matrix.vector_scalyr(f1,f1))) -
                            (Matrix(f2)*(Matrix.vector_scalyr(v4,f2) / Matrix.vector_scalyr(f2,f2))) -
                            (Matrix(f3)*(Matrix.vector_scalyr(v4,f3) / Matrix.vector_scalyr(f3,f3)))).matrix
        return Matrix(f1), Matrix(f2), Matrix(f3), Matrix(f4)



    def norm(f1,f2,f3,f4):
        a=(f1.matrix[0][0]**2+f1.matrix[0][1]**2+f1.matrix[0][2]**2+f1.matrix[0][3]**2)**0.5
        b=(f2.matrix[0][0]**2+f2.matrix[0][1]**2+f2.matrix[0][2]**2+f2.matrix[0][3]**2)**0.5
        c=(f3.matrix[0][0]**2+f3.matrix[0][1]**2+f3.matrix[0][2]**2+f3.matrix[0][3]**2)**0.5
        d=(f4.matrix[0][0]**2+f4.matrix[0][1]**2+f4.matrix[0][2]**2+f4.matrix[0][3]**2)**0.5
    def ortognalization(a,b,c,d,f1,f2,f3,f4):
        res_1=f1/a
        res_2=f2/b
        res_3=f3/c
        res_4=f4/d
        return res_1,res_2,res_3,res_4
    
    
test_matrix = Matrix([[1, -1, 2, 0],
                    [0, -1, 1, 2],
                    [1,  0, 3, 1],
                    [0,  1, 1, 3]])
test_matrix.basic()
test_matrix.ortognalization()
        