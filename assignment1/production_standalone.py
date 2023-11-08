def cobb_douglas(x1, x2, gamma1, gamma2, a):
    """Calculate the Cobb-Douglas output of a single good with two factors.
    
    Args: 
        x1 (float): First input factor
        x2 (float): Second input factor
        gamma1 (float): First exponent
        gamma2 (float): Second exponent
        a (float): Total factor productivity
    
    Returns: 
        float: The output of the Cobb-Douglas production function
    """
    return a*x1**gamma1*x2**gamma2

def leontief(x1,x2,a):
    """Calculate the Leontief output of a single good with two inputs.

    Args: 
        x1 (float): First input quantity
        x2 (float): Second input quantity
        a (float): Total factor productivity

    Returns:
        float: The output of the Leontief production function
    """
    return a*min(x1,x2)

def ces(x1,x2, gamma1, gamma2, rho, a):
    """Calculate the output of CES production function

    Args: 
        x1 (float): First input factor
        x2 (float): Second input factor
        gamma1 (float): Share parameter of the first input
        gamma2 (float): Share parameter of the first input
        rho (float): Substitution parameter
        a (float): Total factor productivity

    Returns: 
        float: The output of CES production function       

    """
    return a*(gamma1*x1**(-rho)+gamma2*x2**(-rho))**(-1/rho)


print("The value the Cobb Douglas production function returns is {}, the correct value is {}." .format(cobb_douglas(x1=25, x2=36, gamma1=0.5, gamma2=0.5, a=10), 300.0))

print("The value the Leontief production function returns is {}, the correct value is {}." .format(leontief(x1=10, x2=15, a=2), 20))

print("The value the CES function returns is {}, the correct value is {}." .format(round(ces(x1=4, x2=9, gamma1=0.4, gamma2=0.6, rho=1, a=1)), 6 ))

