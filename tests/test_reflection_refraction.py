from rr_light.reflection_refraction import *
import pytest

def test_check_invalid_alfa_passes():
    check_invalid_alfa(1)
    check_invalid_alfa(89)

def test_check_invalid_alfa_fails():
    with pytest.raises(ValueError):
        check_invalid_alfa(0)
    with pytest.raises(ValueError):
        check_invalid_alfa(90)

def test_check_invalid_index_of_refr_passes():
    check_invalid_index_of_refr(0.0000001,000000.11)
    check_invalid_index_of_refr(9999999998,9999999999)

def test_check_invalid_index_of_refr_fails():
    check_invalid_index_of_refr(0.000001,0.000001)
    check_invalid_index_of_refr(9999999999,9999999999)
    
def test_tot_intern_refl_passes():
    theta = 45
    n1 = 1.0001
    n2 = 1.0000
    bool = tot_intern_refl(theta, n1, n2)
    assert bool == True

def test_tot_intern_refl_fails():
    theta = 44
    n1 = 1.0000
    n2 = 1.0001
    bool = tot_intern_refl(theta, n1, n2)
    assert bool == True

def test_calculate_refr_angl_passes():
    alfa = 60
    n1 = 1.5
    n2 = 2
    alfa_new, alfa_prim, beta = calculate_refr_angl(alfa, n1, n2)
    assert (alfa_new, alfa_prim, beta) == (alfa, alfa, 40.5053503274186)

def test_calculate_refr_angl_fais():
    alfa = 35
    n1 = 1.5
    n2 = 2
    alfa_new, alfa_prim, beta = calculate_refr_angl(alfa, n1, n2)
    assert (alfa_new, alfa_prim, beta) == (alfa, alfa, 26)
