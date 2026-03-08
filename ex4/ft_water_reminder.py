def ft_water_reminder():
    """precise if the plant need water or nobased on the days last watering."""
    NbOfDaysBeforWatering = int(input("Days since last watering: "))
    if NbOfDaysBeforWatering > 2:
        print("Watter the plants!")
    else:
        print("Plants are fine")
