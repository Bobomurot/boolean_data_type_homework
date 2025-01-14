def main(a):
    """
    "a" sonining mukammal kvadrat ekanligini tekshiring.
    Berilganlar:
        a: int
    Qaytaradi:
        bool
    """
    # Kodni shu yerga yozing
    if a < 0:
        return False
    b = int(a**0.5)
    
    return b * b == a 