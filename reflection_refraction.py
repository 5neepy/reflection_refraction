from distutils.util import strtobool
import math
from matplotlib import pyplot as plt

distance = 5

# Introduction
def intro():
    print("\nReflection and refraction of light Calculator")
    print("By Martin Lambov")
    print("GitHub: https://github.com/5neepy")

# Check if the equetion is posible
def check_alfa(alfa):
    if alfa >= 90 or alfa <= 0:
        print("\nAlfa can't be equal or more than 90 and can't be equal or less than 0.\n")
        exit()

def check_index_of_refr(n1, n2):
    if n1 == n2:
        print("\nIf n_1 = n_2 we don't have Reflection/Refraction of light.\n")
        exit()

def get_vars():
    alfa = float(input("\nEnter the degrees of alfa: "))
    check_alfa(alfa)

    print("\nEnter the indexes of refraction of usual objects: \n air = 1 \n water = 1.33 \n glass = 1.5")

    n1 = float(input("\nn1: "))
    n2 = float(input("n2: "))

    check_index_of_refr(n1, n2)

    return alfa, n1, n2

def calculate_refl_angl(alfa, n1, n2):
    alfa_prim = alfa
    
    # Check if we have total internal reflection
    tot_intern_refl = lambda theta, n1, n2: theta >= 45 and n1 > n2
    
    if tot_intern_refl(alfa, n1, n2):
        beta = 90
    else:
        try:
            beta = math.degrees(math.asin(n1*math.sin(math.radians(alfa))/n2))  # n1*sin(θ1) = n2*sin(θ2)
        except ValueError:
            beta = None

    return alfa, alfa_prim, beta

# Defind function Reflection Plot 
def calc_ref_plot(alfa, beta):
    # Incident beam = a:
    alfa_2 = 90+alfa
    X_1 = (0+distance*math.cos(math.radians(alfa_2)))
    Y_1 = (0+distance*math.sin(math.radians(alfa_2)))

    # Reflected beam = a_1:
    X_2 = -X_1
    Y_2 = Y_1

    if beta is not None:
        # Refracted beam = b:
        beta_2 = 270+beta
        X_3 = (0+distance*math.cos(math.radians(beta_2)))
        Y_3 = (0+distance*math.sin(math.radians(beta_2)))
        p3 = [X_3, Y_3]
    else:
        p3 = None

    p1 = [X_1, Y_1]
    p2 = [X_2, Y_2]

    return (p1, p2, p3)

def matplotlib_graph(p1, p2, p3, n1, n2):
    # Color codes cons
    COLOR_OF_INCIDENT_BEAM = '#ff0a0a'
    COLOR_OF_REFLECTED_AND_REFRACTED_BEAM = '#ff4141'
    
    # plt.title("")

    # Cord. Sys.
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')

    # Set Cord. sys. Range and making 1x=1y
    ax.set_xlim([-distance, distance])
    ax.set_ylim([-distance, distance])
    plt.axis('equal')

    # Hide numbers
    plt.gca().axes.get_xaxis().set_ticks([])
    plt.gca().axes.get_yaxis().set_ticks([])

    # With Vectors
    
    # Incident beam
    dc1 = [p1[0], p1[1]]
    plt.arrow(x=distance*p1[0], y=distance*p1[1], dx=distance*-dc1[0], dy=distance*-dc1[1], facecolor=COLOR_OF_INCIDENT_BEAM, width=0.4, head_width=1, head_length=1.5, length_includes_head=True)

    # Reflected beam
    c2, dc2 = [0, 0], [p2[0], p2[1]]
    plt.arrow(x=c2[0], y=c2[1], dx=distance*dc2[0], dy=distance*dc2[1], facecolor=COLOR_OF_REFLECTED_AND_REFRACTED_BEAM, width=0.4, head_width=1, head_length=1.5, length_includes_head=True)

    if p3 is not None:
        # Refracted beam
        c3, dc3 = [0, 0], [p3[0], p3[1]]
        plt.arrow(x=c3[0], y=c3[1], dx=distance*dc3[0], dy=distance*dc3[1] , facecolor=COLOR_OF_REFLECTED_AND_REFRACTED_BEAM, width=0.4, head_width=1, head_length=1.5, length_includes_head=True)

    # Legend
    plt.legend(["Incident beam", "Reflected beam", "Refracted beam"], loc='lower left')

    # Print the ns on the screan
    
    plt.text(0, 7/8, "$n_1 = {0}$\n$n_2 = {1}$".format(n1, n2), transform=plt.gca().transAxes)

    plt.show()

    return plt.show()

def main():
    intro()
    alfa, n1, n2 = get_vars()
    alfa, alfa_prim, beta = calculate_refl_angl(alfa, n1, n2)
    p1, p2, p3 = calc_ref_plot(alfa, beta)
    
    print("\nalfa = " + str(alfa))
    print("alfa prim = " + str(alfa_prim))
    print("beta = " + str(beta))

    choice = input("\nDo you want to see the graphical solution [y/n]: ")
    proceed = bool(strtobool(choice))
    if not proceed:
        exit()

    matplotlib_graph(p1, p2, p3, n1, n2)

    # print("\nP1 = ( " + str(p1) + " )" "\nP2 = ( " + str(p2) + " )\nP3 = ( " + str(p3) + " )\n")

main()