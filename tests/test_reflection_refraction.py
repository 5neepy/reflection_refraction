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
    with pytest.raises(ValueError):
        check_invalid_index_of_refr(0.000001,0.000001)
    with pytest.raises(ValueError):        
        check_invalid_index_of_refr(9999999999,9999999999)
    
def test_is_tot_intern_refl_passes():
    theta = 45
    n1 = 1.0001
    n2 = 1.0000
    tot_int_refl = is_tot_intern_refl(theta, n1, n2)
    assert tot_int_refl == True

def test_tot_intern_refl_fails():
    theta = 44
    n1 = 1.0000
    n2 = 1.0001
    tot_int_refl = is_tot_intern_refl(theta, n1, n2)
    assert tot_int_refl == False

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
    assert (alfa_new, alfa_prim, beta) != (alfa, alfa, 26)

def test_calc_ref_plot():
    alfa = 60
    beta = 40

    p1, p2, p3 = calc_ref_plot(alfa, beta)
    assert pytest.approx(p1, rel= 1e-3) == [-4.33, 2.5]
    assert pytest.approx(p2, rel= 1e-3) ==  [4.33, 2.5]
    assert pytest.approx(p3, rel= 1e-3) == [3.21, -3.83]
