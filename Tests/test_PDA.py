from src.Programs.PDA import PDA_an_bn

def test_pda():
    assert PDA_an_bn("") == "Accepted"
    assert PDA_an_bn("ab") == "Accepted"
    assert PDA_an_bn("aabb") == "Accepted"
    assert PDA_an_bn("aaabbb") == "Accepted"
    assert PDA_an_bn("aab") == "Rejected"
    assert PDA_an_bn("abb") == "Rejected"
    assert PDA_an_bn("aabba") == "Rejected"
    assert PDA_an_bn("aabbc") == "Invalid Input The Language is [a,b]"