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

# Change your initial guess, do you find different solutions?

|Iteration       |	      |Function            |      |X values| <br>
|:---------------|        |:----------------   |      |:--------------------------------------------------------------------|  
|__-1,-1,-1,-1,-1|	      |1.488372093"98987"  |      |-0.0697'4738',0.02324913,1.51162303,1.46512478,-0.02324913__ <br>
|-10,-9,-8,-7,-6 |        |1.4883720958972313  |      |-0.0697679,0.02325597,1.51166589,1.46515395,-0.02325597 <br>
|__10,9,8,7,6	 |        |1.488372093"0250495"|      |-0.0697'6684', 0.02325561,  1.51162849,  1.46511726, -0.02325561__ <br>
|10,10,10,10,10	 |        |1.4883720940959808  |      |-0.06977049,0.02325683,1.5116055,1.46509184,-0.02325683 <br>
|-10,-10,-10,-10,-10|	  |1.488372098254787   |      |-0.06976901,  0.02325634,  1.51167928,  1.46516661, -0.02325634 <br>
|0,0,0,0,0	     |        |1.4883720930232558  |      |-0.06976744,0.02325581,1.5116279 ,  1.46511628, -0.02325581 <br>

- Based on above iterations, I observed that with change in initial conditions there is very minimum change in the solution.
For example, when we consider the 2 scenarios(1st and 3rd), we can see that value of function changes at 10th decimal point and value of x1 changes from 5th decimal point, which can be considered as very minimum. 
