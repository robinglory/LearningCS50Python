from numb3rs import validate

def test_valid_ips():
    assert validate("192.168.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_invalid_ips():
    assert validate("275.3.6.28") == False  # 275 out of range
    assert validate("192.168.1") == False  # Missing one number
    assert validate("192.168.1.256") == False  # 256 out of range
    assert validate("abc.def.ghi.jkl") == False  # Not numbers
    assert validate("1.1.1.1.1") == False  # Too many parts
