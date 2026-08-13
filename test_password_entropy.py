from engines.password_gen import PasswordSecurityEngine


def test_entropy_empty():
    assert PasswordSecurityEngine.calculate_entropy("") == 0.0


def test_entropy_variety():
    p = "Ab3$"
    entropy = PasswordSecurityEngine.calculate_entropy(p)
    assert entropy > 0.0
