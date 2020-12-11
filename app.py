
class Calculator:

    def add(self, num1, num2):

        if type(num1) is not int or type(num2) is not int:
            raise ValueError("Values must be integers")

        return num1 + num2
    
    def multiply(self, num1, num2):

        if type(num1) is not int or type(num2) is not int:
            raise ValueError("Values must be integers")

        return num1 * num2
    
    def subtract(self, num1, num2):

        if type(num1) is not int or type(num2) is not int:
            raise ValueError("Values must be integers")
        
        return num1 - num2
        