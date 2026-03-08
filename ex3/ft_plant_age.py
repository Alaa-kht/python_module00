def ft_plant_age():
    """precise either if the plant are reday to harvest or no
    based on the age above 60 days."""
    PlantAge = int(input("Enter plant age in days: "))
    if PlantAge > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow")
