def PDA_an_bn(input_str: str) -> str:
    stack = []
    # Loop on Characters in the Input String
    for char in input_str:
        if char == 'a':
            # Push 'a' Into Stack
            stack.append('a')
        elif char == 'b':
            if stack:
            # Pop 'a' From Stack (Match Each a with b)
                stack.pop()
            else:
                return "Rejected"
        else:
            return "Invalid Input The Language is [a,b]"
    return "Accepted" if (len(stack) == 0) else "Rejected"

# Getting the User Input 
# print("PDA Checker For The input Accepted By The Language aⁿbⁿ")
# input_str = input("Enter The Input String: ")

# Print Result
# print(f"PDA Result for '{input_str}':", PDA_an_bn(input_str))