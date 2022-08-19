import numpy as np
import matplotlib.pyplot as plt


def f(x):
    y = (5*x**4) + (3*x**3) + (10*x) + 3
    return y


def f_i(x):
    y = (20*x**3) + (9*x**2) + 10
    return y


def f_ii(x):
    y = (60*x**2) + (18*x)
    return y


def misma_grafica():
    x_axis = np.arange(-50, 50, 2)
    plt.figure()
    plt.axhline(y=0, color="grey", linestyle="--")
    plt.axvline(color="grey", linestyle="--")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.ylim(-100000, 100000)
    plt.legend(fontsize=14)
    plt.plot(x_axis, f(x_axis), '--', label="f(x)")
    plt.plot(x_axis, f_i(x_axis), ':', label="f(x)'")
    plt.plot(x_axis, f_ii(x_axis), label="f(x)''")
    plt.suptitle("Tarea 1: Graficas")
    plt.legend()
    plt.savefig('misma_grafica.jpg')
    plt.savefig('misma_grafica.eps')
    plt.savefig('misma_grafica.svg')


def diferente_grafica():
    x_axis = np.arange(-50, 50, 2)
    plt.figure()
    fig, ax = plt.subplots(3, 1)
    ax[0].set_title("Tarea 1: Graficas")
    ax[0].axvline(color="grey", linestyle="--")
    ax[0].tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    ax[0].plot(x_axis, f(x_axis), color="#781C68", linestyle='--', label="f(x)")
    ax[0].legend()
    ax[1].axhline(y=0, color="grey", linestyle="--")
    ax[1].axvline(color="grey", linestyle="--")
    ax[1].tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    ax[1].set_ylabel("Y")
    ax[1].plot(x_axis, f_i(x_axis), color="#319DA0", linestyle=':', label="f(x)'")
    ax[1].legend()
    ax[2].axvline(color="grey", linestyle="--")
    ax[2].set_xlabel("X")
    ax[2].plot(x_axis, f_ii(x_axis), color="#FF7F3F", label="f(x)''")
    ax[2].legend()
    plt.savefig('difetente_grafica.jpg')
    plt.savefig('difetente_grafica.eps')
    plt.savefig('difetente_grafica.svg')


