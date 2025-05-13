from src.Programs.Turing_Machine import TuringMachine

def test_TM():
    assert TuringMachine("").run() == "Accepted"  # Empty string is valid
    assert TuringMachine("0101").run() == "Accepted" # "01" + "01"
    assert TuringMachine("0100").run() == "Rejected" # "01" + "00"   
    assert TuringMachine("0").run() == "Rejected"# Length 1 (odd)