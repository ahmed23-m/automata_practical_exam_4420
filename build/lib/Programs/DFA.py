def DFA_Divisible_By_Three(input_Str: str) -> str:
    # Starting State
    state = 0
    for c in input_Str:
        if c == '1':
            # Match Each [divisible_By] Ones 
            state = (state + 1) % 3
        elif c != '0':
            return "Invalid Character Is Inserted"  # Invalid Character
    # Check If the Input String is Divisable (Reachs a Final State)
    return "Accepted" if state == 0 else "Rejected"

# Getting the User Input 
# input_Str = input("Please Enter the DFA Input String: ")

# Print Result
# print(f"DFA Result for '{input_Str}':", DFA_Divisible_By_Three(input_Str))