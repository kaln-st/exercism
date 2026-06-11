def is_armstrong_number(number):
    
    """
    
    Write some code to determine whether a number is an Armstrong number.

    Parameter:
        number (int): positive number to check
    
    Returns:
        bool: is armstrong number or not   
    
    """

    # 1. Check number is int or not
    if type(number) != int: raise ValueError("Input should be a number!")

    # 2. Check number < 0
    if number < 0: raise ValueError("Number should be a positive number!")

    # 3. Find the exponent
    numbers = str(number) # Convert number (int) to number (string). And assign to numbers
    exponent = len(numbers)

    # 4. Calculate opposite of armstrong number
    temp_number = 0
    for num in numbers:
        temp_number += int(num) ** exponent

    # 5. Check if number is armstrong number or not
    return number == temp_number
