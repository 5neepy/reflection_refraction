from distutils.util import strtobool
import math
from matplotlib import pyplot as plt
import typing

DISTANCE = 5

def intro() -> None:
    '''Introduction to the project.
    '''
    
    print("\nReflection and refraction of light Calculator")
    print("By Martin Lambov")
    print("GitHub: https://github.com/5neepy")

def check_alfa(alfa: float) -> None:
    '''Check if the equation is possible by giving alfa certain range.

    :param alfa: Angle of incidence.
    '''
    
    if alfa >= 90 or alfa <= 0:
        print("\nAlfa can't be equal or more than 90 and can't be equal or less than 0.\n")
        exit()

def check_index_of_refr(n1: float, n2: float) -> None:
    '''Check if the refraction indices are equal.
    
    :param n1: Index of refraction of the first medium
    :param n2: Index of refraction of the second medium
    '''
    
    if n1 == n2:
        print("\nIf n_1 = n_2 we don't have Reflection/Refraction of light.\n")
        exit()

def get_vars() -> tuple[float,float,float]:
    '''Getting the variables from the user.
    
    :return: Angle of incidence.
    :return: Index of refraction of the first medium
    :return: Index of refraction of the second medium
    '''
    
    alfa = float(input("\nEnter the degrees of alfa: "))
    check_alfa(alfa)

    print("\nEnter the indexes of refraction of usual objects: \n air = 1 \n water = 1.33 \n glass = 1.5")

    n1 = float(input("\nn1: "))
    n2 = float(input("n2: "))

    check_index_of_refr(n1, n2)

    return alfa, n1, n2

def tot_intern_refl(theta, n1, n2):
    '''Check if we have total internal reflection.

    :param theta: Angle of incidence
    :param n1: Index of refraction of the first medium
    :param n2: Index of refraction of the second medium
    :return: True or False
    '''
    if theta >= 45 and n1 > n2:
        return True
    else:
        return False

def calculate_refr_angl(alfa: float, n1: float, n2: float) -> tuple[float,float,float]:
    '''Calculate the refraction angle.
    
    :param alfa: Angle of incidence
    :param n1: Index of refraction of the first medium
    :param n2: Index of refraction of the second medium
    :return: Angle of incidence
    :return: Angle of reflection
    :return: Angle of refraction
    '''
    
    alfa_prim = alfa
    
    if tot_intern_refl(alfa, n1, n2):
        beta = 90
    else:
        try:
            beta = math.degrees(math.asin(n1*math.sin(math.radians(alfa))/n2))  # n1*sin(θ1) = n2*sin(θ2)
        except ValueError:
            beta = None

    return alfa, alfa_prim, beta
 
def calc_ref_plot(alfa: float, beta:float) -> tuple[float,float,float]:
    '''Calculate the positions of the points in the plot.
    :param alfa: Angle of incidence
    :param: beta: Angle of refraction
    :return: Start cordinates of the incident beam
    :return: Start cordinates of the reflected beam
    :return: Start cordinates of the refracted beam
    '''
    
    # Incident beam = a:
    alfa_2 = 90+alfa
    X_1 = (0+DISTANCE*math.cos(math.radians(alfa_2)))
    Y_1 = (0+DISTANCE*math.sin(math.radians(alfa_2)))

    # Reflected beam = a_1:
    X_2 = -X_1
    Y_2 = Y_1

    if beta is not None:
        # Refracted beam = b:
        beta_2 = 270+beta
        X_3 = (0+DISTANCE*math.cos(math.radians(beta_2)))
        Y_3 = (0+DISTANCE*math.sin(math.radians(beta_2)))
        p3 = [X_3, Y_3]
    else:
        p3 = None

    p1 = [X_1, Y_1]
    p2 = [X_2, Y_2]

    return (p1, p2, p3)

def matplotlib_graph(p1: float, p2: float, p3: float, n1: float, n2: float) -> str:
    '''Create a matplotlib graph.

    :param p1: Start cordinates of the incident beam
    :param p2: Start cordinates of the reflected beam
    :param p3: Start cordinates of the refracted beam
    :param n1: Index of refraction of the first medium
    :param n2: Index of refraction of the second medium
    :return: Show graph
    '''
    # Color codes cons
    COLOR_OF_INCIDENT_BEAM = '#ff0a0a'
    COLOR_OF_REFLECTED_AND_REFRACTED_BEAM = '#ff4141'

    # Cord. Sys.
    ax = plt.gca()
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')

    # Set Cord. sys. Range and making 1x=1y
    ax.set_xlim([-DISTANCE, DISTANCE])
    ax.set_ylim([-DISTANCE, DISTANCE])
    plt.axis('equal')

    # Hide numbers
    plt.gca().axes.get_xaxis().set_ticks([])
    plt.gca().axes.get_yaxis().set_ticks([])
    
    # Incident beam
    dc1 = [p1[0], p1[1]]
    plt.arrow(x=DISTANCE*p1[0], y=DISTANCE*p1[1], dx=DISTANCE*-dc1[0], dy=DISTANCE*-dc1[1], facecolor=COLOR_OF_INCIDENT_BEAM, width=0.4, head_width=1, head_length=1.5, length_includes_head=True)

    # Reflected beam
    c2, dc2 = [0, 0], [p2[0], p2[1]]
    plt.arrow(x=c2[0], y=c2[1], dx=DISTANCE*dc2[0], dy=DISTANCE*dc2[1], facecolor=COLOR_OF_REFLECTED_AND_REFRACTED_BEAM, width=0.4, head_width=1, head_length=1.5, length_includes_head=True)

    if p3 is not None:
        # Refracted beam
        c3, dc3 = [0, 0], [p3[0], p3[1]]
        plt.arrow(x=c3[0], y=c3[1], dx=DISTANCE*dc3[0], dy=DISTANCE*dc3[1] , facecolor=COLOR_OF_REFLECTED_AND_REFRACTED_BEAM, width=0.4, head_width=1, head_length=1.5, length_includes_head=True)

    # Legend
    plt.legend(["Incident beam", "Reflected beam", "Refracted beam"], loc='lower left')

    # Print the ns on the screan
    plt.text(0, 7/8, "$n_1 = {0}$\n$n_2 = {1}$".format(n1, n2), transform=plt.gca().transAxes)

    plt.show()

    return plt.show()

def main() -> None:
    intro()
    alfa, n1, n2 = get_vars()
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