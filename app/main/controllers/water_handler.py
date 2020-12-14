import os
import csv
import math

basedir = os.path.abspath(os.path.dirname(__file__))


def get_pipes(load, fluid, pipe_type, temperature, temp_difference):
    """Returns list of recommended pipe diameters [mm] using D'Arcy equation.
    https://en.wikipedia.org/wiki/Darcy%E2%80%93Weisbach_equation
    Arguments:
    load - heating or cooling load [kW]
    fluid - type of fluid (water or water-glycol)
    diameter - internal pipe diameter [mm]
    roughness - pipe's equivalent roughness [mm]
    temperature - mean fluid temperature [degC]
    temp_difference - supply/return temperature difference [degC/K]
    """
    pipe_dict = get_diameters()

    diameters = []

    for pipe in pipe_dict:
        if pipe["type"] == pipe_type:
            diameters.append([int(pipe["dn"]), float(pipe["di"]), pipe["k"]])
    roughness = float(diameters[0][2])

    pressure_losses = []

    for diameter in diameters:
        fluid_table = get_fluid_data(fluid)
        density = float(fluid_table[int(temperature)]["Density[kg/m3]"])
        heat_capacity = float(fluid_table[int(temperature)]["Specific heat[kJ/kg*K]"])
        kinematic_viscosity = float(
            fluid_table[int(temperature)]["Kinematic viscosity[m2/s]"]
        )

        volume_flow = get_volume_flow(load, density, heat_capacity, temp_difference)
        velocity = get_velocity(volume_flow, diameter[1])
        reynolds_number = get_reynolds_number(
            velocity, diameter[1], kinematic_viscosity
        )
        friction_coefficient = get_friction_coefficient(
            reynolds_number, roughness, diameter[1]
        )
        pressure_losses.append(
            [
                diameter[0],
                int(
                    get_pressure_loss(
                        friction_coefficient, diameter[1], density, velocity
                    )
                ),
            ]
        )

    return pressure_losses


def get_diameters():
    """Returns dictionary of available pipes."""

    pipe_dict = []

    with open(os.path.join(basedir, "pipes.csv"), encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=";")
        for row in csv_reader:
            pipe_dict.append(row)
    return pipe_dict


def get_velocity(volume_flow, diameter):
    """Returns fluid velocity inside a piape [m/s].
    volume_flow - fluid volume flow [m3/s]
    diameter - internal pipe diameter [mm]
    """
    return volume_flow / ((math.pi * (diameter / 1000) ** 2) / 4)


def get_volume_flow(load, density, heat_capacity, temp_difference):
    """Returns volume flow of fluid [m^3/s].
    load - heating or cooling load [kW]
    density - fluid density [kg/m3]
    heat_capacity - fluid specific heat capacity [kJ/kg*K]
    temp_difference - supply/return temperature difference [degC/K]
    """
    return load / (density * heat_capacity * temp_difference)


def get_reynolds_number(velocity, diameter, kinematic_viscosity):
    """Returns Reynolds number.
    velocity - fluid velocity [m/s]
    diameter - internal pipe diameter [mm]
    kinematic_viscosity - fluid kinematic viscosity [m^2/s]
    """
    return velocity * (diameter / 1000) / kinematic_viscosity


def get_friction_coefficient(reynolds_number, roughness, diameter):
    """Returns friction coefficient using Haaland's equation.
    https://en.wikipedia.org/wiki/Darcy_friction_factor_formulae
    reynolds_number = Reynolds Number
    roughness - pipe's equivalent roughness [mm]
    diameter - internal pipe diameter [mm]
    """
    if reynolds_number < 2000:
        return 64 / reynolds_number
    else:
        value = 6.9 / reynolds_number + ((roughness / diameter) / 3.71) ** 1.11
        friction_coefficient = (1 / (-1.8 * math.log10(value))) ** 2
        return friction_coefficient


def get_pressure_loss(friction_coefficient, diameter, density, velocity):
    """Returns pressure loss for given diameter [Pa/m].
    friction_coefficient - Friction coefficient [-]
    diameter - internal pipe diameter [mm]
    density - fluid density [kg/m3]
    velocity - fluid velocity [m/s]
    """
    pressure_loss = (
        friction_coefficient
        * (1 / (diameter / 1000))
        * ((density * (velocity ** 2)) / 2)
    )
    return pressure_loss


def get_fluid_data(fluid):
    """Returns dictionary with chosen fluid data."""

    fluid_dict = []

    if fluid == "water":
        with open(
            os.path.join(basedir, "water_table.csv"), encoding="utf-8"
        ) as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=";")
            for row in csv_reader:
                fluid_dict.append(row)
        return fluid_dict
