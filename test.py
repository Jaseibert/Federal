import FRED

def test_state_name(state):
    FRED.Start_Date(1900,1,1)
    FRED.End_Date(2018,1,1)
    FRED.StateGDP(state)
    assert len(state) == 2, "State should be a string of length 2"

if __name__ == "__main__":
    test_state_name('TX')
    print("Everything passed")
