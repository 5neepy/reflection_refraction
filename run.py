from rr_light.reflection_refraction import *

def main() -> None:
   
    print("\nReflection and refraction of light Calculator")
    print("By Martin Lambov")
    print("GitHub: https://github.com/5neepy")

    try:
        alfa, n1, n2 = get_vars()
    except ValueError as a:
        print(str(a))
        exit(1)
    
    alfa, alfa_prim, beta = calculate_refr_angl(alfa, n1, n2)
    p1, p2, p3 = calc_ref_plot(alfa, beta)
    
    print("\nalfa = " + str(alfa))
    print("alfa prim = " + str(alfa_prim))
    print("beta = " + str(beta))

    choice = input("\nDo you want to see the graphical solution [y/n]: ")
    proceed = bool(strtobool(choice))
    if not proceed:
        exit()

    matplotlib_graph(p1, p2, p3, n1, n2)
main()