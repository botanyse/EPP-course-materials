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


def general_ces(gammas, factors, rho, a):
    """Calculate the output of the generalized CES production function

    Args:
        gammas (list): List of share parameters of inputs
        factos (list): List of input factors
        rho (float): Substitution parameter
        a (float): Total factor productivity
    """
    output = a * sum(gamma * factor**(-rho) for gamma, factor in zip(gammas, factors))**(-1/rho)
    return output
