def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    
    Formula: SI = (P × R × T) / 100
    
    Args:
        principal: Initial amount (P)
        rate: Annual interest rate as percentage (R)
        time: Time period in years (T)
    
    Returns:
        Simple interest amount
    """
    simple_interest = (principal * rate * time) / 100
    return simple_interest

def calculate_amount(principal, rate, time):
    """
    Calculate total amount (Principal + Simple Interest).
    
    Args:
        principal: Initial amount
        rate: Annual interest rate as percentage
        time: Time period in years
    
    Returns:
        Total amount
    """
    si = calculate_simple_interest(principal, rate, time)
    total_amount = principal + si
    return total_amount

# Interactive mode
if __name__ == "__main__":
    print("=" * 50)
    print("Simple Interest Calculator")
    print("=" * 50)
    
    try:
        principal = float(input("\nEnter Principal Amount ($): "))
        rate = float(input("Enter Rate of Interest (% per annum): "))
        time = float(input("Enter Time Period (years): "))
        
        if principal < 0 or rate < 0 or time < 0:
            print("\nError: All values must be positive!")
        else:
            si = calculate_simple_interest(principal, rate, time)
            amount = calculate_amount(principal, rate, time)
            
            print("\n" + "=" * 50)
            print("CALCULATION RESULTS")
            print("=" * 50)
            print(f"Principal Amount: ${principal:,.2f}")
            print(f"Rate of Interest: {rate}% per annum")
            print(f"Time Period: {time} years")
            print("-" * 50)
            print(f"Simple Interest: ${si:,.2f}")
            print(f"Total Amount: ${amount:,.2f}")
            print("=" * 50)
    
    except ValueError:
        print("\nError: Please enter valid numeric values!")
