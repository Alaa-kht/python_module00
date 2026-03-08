def ft_count_harvest_iterative():
    """counts days until harvest iteratively based on user input."""
    days = int(input("Days until havest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")
