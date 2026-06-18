def is_valid_triangle(sides):

    if len(sides) == 3:
        a, b, c = sides
        if a > 0 and b > 0 and c > 0:
            if (a + b > c) and (a + c > b) and (b + c > a):
                return True
        return False
    else:
        raise ValueError("Sides must be greater than 0 and have 3 elements")

def equilateral(sides):
    
    if is_valid_triangle(sides):
        a, b, c = sides

        if a == b == c:
            return True
        
    return False

def isosceles(sides):

    if is_valid_triangle(sides):
        a, b, c = sides

        if (a == b and b == a) or (a == c and c == a) or (b == c and c == b):
            return True
    
    return False


def scalene(sides):

    if is_valid_triangle(sides):
        a, b, c = sides

        if a != b and a != c and b != c:
            return True
    
    return False
