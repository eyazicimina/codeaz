
def ortalama( sayilar: list ) -> float:
    topla = 0
    for s in sayilar:
        topla += s
    return topla / len(sayilar)

def alanHesapla( r: float ) -> float:
    return 3.14 * r * r
