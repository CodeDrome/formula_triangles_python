import formulatriangle as ft


def main():

    print("---------------------")
    print("| codedrome.com     |")
    print("| Formula Triangles |")
    print("---------------------\n")

    distance_speed_time()


def distance_speed_time():

    '''
    Calculate the following individual values
    relating to a journey from the other two:
        * distance
        * speed
        * time
    '''

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


if __name__ == "__main__":

    main()
