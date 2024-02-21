def calculate_emi(principal, interest_rate, tenure):
    # Convert annual interest rate to monthly and calculate EMI
    monthly_interest_rate = interest_rate / (12 * 100)
    emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure) / ((1 + monthly_interest_rate) ** tenure - 1)
    return emi

def main():
    try:
        # Get user input for loan details
        principal = float(input("Enter loan amount (principal): "))
        interest_rate = float(input("Enter annual interest rate (%): "))
        tenure = int(input("Enter loan tenure in months: "))

        # Calculate EMI
        emi = calculate_emi(principal, interest_rate, tenure)

        # Display the result
        print(f"\nEMI: {emi:.2f} INR per month")
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")

if __name__ == "__main__":
    main()
