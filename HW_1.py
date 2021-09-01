"""
Problem Statement: Solve the problem using Python SciPy.optimize

Minimize: (x1-x2)^2+(x2+x3-2)^2+(x4-1)^2+(x5-1)^2
Subject to:
             x1+3x2 = 0
             x3+x4-2x5 = 0
             x2-x5 = 0
Boundary Conditions :
-10<= xi <= 10, i = 1,2,3,4,5

"""
# Code
# First Iteration with boundary conditions [-1 -1 -1 -1 -1]

import pandas as pd

data = {'fun': ['1.48837209398987','1.4883720958972313']}

df = pd.DataFrame(data, columns= ['fun'])

df.to_csv (r'C:\Users\divya\PycharmProjects\MAE598-Design-Optimization\hw_1 output.csv', index = False, header=True)

print (df)