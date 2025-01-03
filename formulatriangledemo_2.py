import formulatriangle as ft


def main():

    """

    """

    print("---------------------")
    print("| codedrome.com     |")
    print("| Formula Triangles |")
    print("---------------------\n")

    # distance_speed_time()

    # volts_amps_ohms()

    # mass_density_volume()

    # force_mass_acceleration()

    # speed_wavelength_frequency()

    energy_power_time()


def distance_speed_time():

    distance = ft.Quantity("Distance", "s", "metre", "m")
    speed = ft.Quantity("Speed", "v", "metre per second", "m/s")
    time = ft.Quantity("Time", "t", "second", "s")

    ft.output(distance, speed, time)

    # set v & t, and calculate s
    v = 16.0
    t = 5400.0
    s = ft.evaluate(float('nan'), v, t)

    print()
    print(f"v = {v}m/s") 
    print(f"t = {t}s") 
    print(f"s = {s}m")

    # set s & t, and calculate v
    s = 86400.0
    t = 5400.0
    v = ft.evaluate(s, float('nan'), t)

    print()
    print(f"t = {t}s") 
    print(f"s = {s}m")
    print(f"v = {v}m/s") 

    # set s & v, and calculate t
    s = 86400.0
    v = 16.0
    t = ft.evaluate(s, v, float('nan'))

    print()
    print(f"s = {s}m")
    print(f"v = {v}m/s") 
    print(f"t = {t}s")


def volts_amps_ohms():

    '''
    Ohm's Law
    '''

    voltage = ft.Quantity("Voltage", "V", "Volt", "V")
    current = ft.Quantity("Current", "I", "Amp", "A")
    resistance = ft.Quantity("Resistance", "R", "Ohm", "Ω")

    ft.output(voltage, current, resistance)

    # set I & R, and calculate V
    I = 1.5
    R = 6.0
    V = ft.evaluate(float('nan'), I, R)

    print()
    print(f"I = {I}A") 
    print(f"R = {R}Ω") 
    print(f"V = {V}V")

    # set V & R, and calculate I
    V = 9.0
    R = 6.0
    I = ft.evaluate(V, float('nan'), R)

    print()
    print(f"V = {V}V")
    print(f"R = {R}Ω") 
    print(f"I = {I}A") 

    # set V & I, and calculate R
    V = 9.0
    I = 1.5
    R = ft.evaluate(V, I, float('nan'))

    print()
    print(f"V = {V}V")
    print(f"I = {I}A") 
    print(f"R = {R}Ω") 


def mass_density_volume():

    mass = ft.Quantity("Mass", "m", "Kilogram", "kg")
    density = ft.Quantity("Density", "ρ", "Kilograms per cubic metre", "kg/m³")
    volume = ft.Quantity("Volume", "V", "Cubic metre", "m³")

    ft.output(mass, density, volume)

    # set ρ and V, and calculate m
    ρ = 19300.0
    V = 0.000001
    m = ft.evaluate(float('nan'), ρ, V)

    print()
    print(f"ρ = {ρ:0.0f}kg/m³")
    print(f"V = {V:0.6f}m³") 
    print(f"m = {m:0.4f}kg")

    # set m and V, and calculate ρ
    m = 0.0193
    V = 0.000001
    ρ = ft.evaluate(m, float('nan'), V)

    print()
    print(f"m = {m:0.4f}kg")
    print(f"V = {V:0.6f}m³") 
    print(f"ρ = {ρ:0.0f}kg/m³")

    # set m and ρ, and calculate V
    m = 0.0193
    ρ = 19300.0
    V = ft.evaluate(m, ρ, float('nan'))

    print()
    print(f"m = {m:0.4f}kg") 
    print(f"ρ = {ρ:0.0f}kg/m³")
    print(f"V = {V:0.6f}m³")


def force_mass_acceleration():

    '''
    Newton's Second Law of Motion
    '''

    force = ft.Quantity("Force", "F", "Newton", "N")
    mass = ft.Quantity("Mass", "m", "Kilogram", "kg")
    acceleration = ft.Quantity("Acceleration", "a", "Metre per second squared", "m/s²")

    ft.output(force, mass, acceleration)

    # set m and a, calculate F
    m = 1600.0
    a = 3.0
    F = ft.evaluate(float('nan'), m, a)

    print()
    print(f"m = {m}kg") 
    print(f"a = {a}m/s²")
    print(f"F = {F}N")

    # set F and a, calculate m
    F = 4800.0
    a = 3.0
    m = ft.evaluate(F, float('nan'), a)

    print()
    print(f"F = {F}N")
    print(f"a = {a}m/s²")
    print(f"m = {m}kg")

    # set F and m, calculate a
    F = 4800.0
    m = 1600.0
    a = ft.evaluate(F, m, float('nan'))

    print()
    print(f"F = {F}N")
    print(f"m = {m}kg")
    print(f"a = {a}m/s²")


def speed_wavelength_frequency():

    speed = ft.Quantity("Speed", "v", "Metres per second", "m/s")
    frequency = ft.Quantity("Frequency", "f", "Hertz", "Hz")
    wavelength = ft.Quantity("Wavelength", "λ", "Metre", "m")

    ft.output(speed, frequency, wavelength)

    # set f and λ, calculate V
    f = 261.63
    λ = 1.261323243
    v = ft.evaluate(float('nan'), f, λ)

    print()
    print(f"f = {f}Hz")
    print(f"λ = {λ}m")
    print(f"v = {v:0.0f}m/s")

    # set v and λ, calculate f
    v = 330
    λ = 1.261323243
    f = ft.evaluate(v, float('nan'), λ)

    print()
    print(f"v = {v:0.0f}m/s")
    print(f"λ = {λ}m")
    print(f"f = {f}Hz")

    # set v and f, calculate λ
    v = 330
    f = 261.63
    λ = ft.evaluate(v, f, float('nan'))

    print()
    print(f"v = {v:0.0f}m/s")
    print(f"f = {f}Hz")
    print(f"λ = {λ}m")


def energy_power_time():

    energy = ft.Quantity("Energy", "E", "Joule", "J")
    power = ft.Quantity("Power", "P", "Watt", "W")
    time = ft.Quantity("Time", "t", "Second", "s")

    ft.output(energy, power, time)

    # set P and t, calculate E
    P = 2450.0
    t = 30.0
    E = ft.evaluate(float('nan'), P, t)

    print()
    print(f"P = {P}W")
    print(f"t = {t}s")
    print(f"E = {E}J")

    # set E and t, calculate P
    E = 73500
    t = 30
    P = ft.evaluate(E, float('nan'), t)

    print()
    print(f"E = {E}J")
    print(f"t = {t}s")
    print(f"P = {P}W")

    # set E and P, calculate t
    E = 73500
    P = 2450.0
    T = ft.evaluate(E, P, float('nan'))

    print()
    print(f"E = {E}J")
    print(f"P = {P}W")
    print(f"t = {t}s")


if __name__ == "__main__":

    main()
