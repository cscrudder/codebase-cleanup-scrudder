from app.utils import to_usd

def test_to_usd():
    assert to_usd(123456789.98) == "$123456,789.98" 

