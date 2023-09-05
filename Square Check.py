import math
def Check_Square(n):
    root = math.sqrt(n)
    root = int(root)
    if root * root == n:
        return True
    else:
        return False

print(Check_Square(32))