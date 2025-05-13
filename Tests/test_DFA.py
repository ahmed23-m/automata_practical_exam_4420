from src.Programs.DFA import DFA_Divisible_By_Three

def test_DFA():
    assert DFA_Divisible_By_Three("")       == "Accepted" # 0 1s
    assert DFA_Divisible_By_Three("000")    == "Accepted" # 0 1s
    assert DFA_Divisible_By_Three("111")    == "Accepted" # 3 1s
    assert DFA_Divisible_By_Three("110110") == "Rejected" # 4 1s
    assert DFA_Divisible_By_Three("101")    == "Rejected" # 2 1s
    assert DFA_Divisible_By_Three("12")     == "Invalid Character Is Inserted"    # Invalid Input