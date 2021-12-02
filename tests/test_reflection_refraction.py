


from rr_light.reflection_refraction import calculate_refr_angl


def test_check_alfa():
    pass

def test_calculate_refr_angl():
    alfa = 60
    n1 = 2
    n2 = 1.5
    alfa_new, alfa_prim, beta = calculate_refr_angl(alfa, n1, n2)
    assert (alfa_new, alfa_prim, beta) == (alfa, alfa, 90)
    assert beta == 90