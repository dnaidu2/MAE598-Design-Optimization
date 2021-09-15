# MAE598-Design-Optimization
Fall 2021 course
HW_1 : 
#Problem Statement: Solve the problem using Python SciPy.optimize
<br>
#Minimize: (x1-x2)^2+(x2+x3-2)^2+(x4-1)^2+(x5-1)^2
<br>
#Subject to:<br>
             x1+3x2 = 0 <br>
             x3+x4-2x5 = 0 <br>
             x2-x5 = 0 <br>
#Boundary Conditions : <br>
-10<= xi <= 10, i = 1,2,3,4,5 <br>
#Initial guesses of the solution <br>
[-1,-1,-1,-1,-1],[-10,-9,-8,-7,-6],[10,9,8,7,6],[10,10,10,10,10],[-10,-10,-10,-10,-10],[0,0,0,0,0]

# Code can be found in the below Jupyter Notebook
https://github.com/dnaidu2/MAE598-Design-Optimization/blob/1102664ac42fe87ac860cfadb32db1ce614028a3/HW_1.ipynb

# Change your initial guess, do you find different solutions?

|Iteration       |	      |Function            |      |X values| <br>
|:---------------|        |:----------------   |      |:--------------------------------------------------------------------|  
|__-1,-1,-1,-1,-1|	      |4.09302325"5824878" |      |-0.7674'4284',  0.25581428,  0.62790506, -0.1162765 ,  0.25581428__ <br>
|-10,-9,-8,-7,-6 |        |4.093023255813954   |      |-0.76744186,  0.25581395,  0.62790697, -0.11627907,  0.25581395 <br>
|10,9,8,7,6	     |        |4.093023255813954   |      |-0.76744185,  0.25581395,  0.62790697, -0.11627906,  0.25581395 <br>
|10,10,10,10,10	 |        |4.093023258012402   |      |-0.76745276,  0.25581759,  0.62787785, -0.11624268,  0.25581759 <br>
|__-10,-10,-10,-10,-10|	  |4.09302325"604787"  |      |-0.7674'3824',  0.25581275,  0.62791644, -0.11629094,  0.25581275__ <br>
|0,0,0,0,0	     |        |4.093023255813954   |      |-0.76744186,  0.25581395,  0.62790698, -0.11627907,  0.25581395 <br>

- Based on above iterations, I observed that with change in initial conditions there is very minimum change in the solution.
For example, when we consider the 2 scenarios(1st and 5th), we can see that value of function changes at 9th decimal point and value of x1 changes from 5th decimal point, which is very minimum.
- For some scenarios the function value is almost same and there is slight change in x values.
