from hello import hello

def test_argument():
    assert hello("David") == "Hello, David"

def test_default():
    for name in ["Yan Naing", "Wai Yan", "Ngwe Thant"]:
        assert hello(name) == f"Hello, {name}"