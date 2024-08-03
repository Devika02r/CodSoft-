class Calculator:
    
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y
    def main():
        print("Select option:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        for _ in range(5):
            choice = input("Enter your choice (1/2/3/4/5): ")
            if choice in ('1', '2', '3', '4', '5'):
                if choice == '5':
                    print("Exiting..")
                    break
                
                try:
                    n1 = float(input("Enter the first number: "))
                    n2 = float(input("Enter the second number: "))
                except ValueError:
                    print("Error,Invalid input.")
                    continue
                
                if choice == '1':
                    print("Result:", Calculator.add(n1, n2))
                elif choice == '2':
                    print("Result:", Calculator.subtract(n1, n2))
                elif choice == '3':
                    print("Result:", Calculator.multiply(n1, n2))
                elif choice == '4':
                    print("Result:", Calculator.divide(n1, n2))
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
                break

if __name__ == '__main__':
    Calculator.main()
