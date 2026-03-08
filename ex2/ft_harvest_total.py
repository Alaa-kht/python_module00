def ft_harvest_total():
    """Calculatr the totl harvest vegetables on 3 different days."""
    Day1Hav = int(input("Day 1 harvest: "))
    Day2Hav = int(input("Day 2 harvest: "))
    Day3Hav = int(input("Day 3 harvest: "))
    total = Day1Hav + Day2Hav + Day3Hav
    print(f"Total harvst: {total}")
