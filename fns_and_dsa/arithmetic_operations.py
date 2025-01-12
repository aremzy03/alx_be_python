def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num1 == 0 or num2 == 0:
                return "cannot divide by zero (0)."
            return num1 / num2
