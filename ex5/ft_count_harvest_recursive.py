def ft_count_harvest_recursive():
    """counts days until harvest recursively based on user input."""
    days = int(input("Days until harvest: "))

    def _recursive_count(current_day):
        if current_day <= days:
            print(f"Day {current_day}")
            _recursive_count(current_day + 1)
        else:
            print("Harvest time!")
    _recursive_count(1)
