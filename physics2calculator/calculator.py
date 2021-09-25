import calcupy
from physics2calculator.settings import constants
from physics2calculator.settings import units
from physics2calculator.settings import styling


def load_units(variables):
    variables["m"] = units.m
    variables["n"] = units.n
    variables["p"] = units.p
    variables["u"] = units.u


def load_constants(variables):
    variables["k"] = constants.COULOMB_CONSTANT
    variables["me"] = constants.ELECTRON_MASS
    variables["mp"] = constants.PROTON_MASS
    variables["e0"] = constants.VACUUM_PERMITTIVITY


def run():
    variables = {}
    load_units(variables)
    load_constants(variables)
    calculator = calcupy.Calculator(variables, None, styling.TITLE)
    calculator.start()


if __name__ == "__main__":
    run()
