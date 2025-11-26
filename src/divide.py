def divide(a, b):
     """Divide two numbers and return the result.
    
    Args:
        a: The first number.
        b: The second number.
        
    Returns:
        The divison of a and b WHEN b!=0 
    """
    # Issue #7: Fix divide() behavior for b = 0
     if b!=0:
         return a / b
     else:
            return None  # Return None when division by zero is attempted
