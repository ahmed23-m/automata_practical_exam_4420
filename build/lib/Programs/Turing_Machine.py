class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape)    # Input tape 
        self.head = 0             # Current position of the tape head
        self.state = "start"      # Current state (start/compare/accept/reject)
        self.middle = None        # Middle index of the tape

    def step(self):
        if self.state == "start":
            if not self.tape:  # Empty string
                self.state = "accept"
                return
            self.middle = len(self.tape) // 2
            if len(self.tape) % 2 != 0:
                self.state = "reject"
            else:
                self.state = "compare"

        elif self.state == "compare":
            if self.head >= self.middle:
                self.state = "accept"
                return
            # Compare current symbol with its mirror
            mirror_idx = self.head + self.middle
            if mirror_idx >= len(self.tape):
                self.state = "reject"
                return
            if self.tape[self.head] != self.tape[mirror_idx]:
                self.state = "reject"
            else:
                self.head += 1

    def run(self):
        while self.state not in ["accept", "reject"]:
            self.step()
        return "Accepted" if (self.state == "accept") else "Rejected"

# Getting the User Input 
# input_Str = input("Please Enter the TM Input String: ")

# Print Result
# print(f"TM Result for '{input_str}':", TuringMachine(input_str).run())