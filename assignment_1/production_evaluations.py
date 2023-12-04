from production_functions import cobb_douglas, leontief, ces, general_ces


print("The value the Cobb Douglas production function returns is {}, the correct value is {}." .format(cobb_douglas(x1=25, x2=36, gamma1=0.5, gamma2=0.5, a=10), 300.0))

print("The value the Leontief production function returns is {}, the correct value is {}." .format(leontief(x1=10, x2=15, a=2), 10))

print("The value the CES function returns is {}, the correct value is {}." .format(ces(x1=4, x2=9, gamma1=0.4, gamma2=0.6, rho=1, a=1), 2.0 ))


 # for README.md file
 # By splitting up the code into two files "production_evaluations" and "production_functions",
 # we separate the files that have different functionalities. We know that production_functions
 # file contains the functions we can reuse in the project while production_evaluations 
 # file serves the purpose of evaluating and testing the functions we wrote. Separate files
 # enhance the readability of the code, make it easier to use our functions again in other files
 # by importing.


print("The generalized CES function returns {}, the correct value is: {}".format(general_ces([1/2,1/2],[1,1], 1/2, 2),2))
