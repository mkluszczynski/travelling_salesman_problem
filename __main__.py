import os
from src.Path import Path
from src.AntService import AntService
from src.PathService import PathService
from src.City import City
from src.CityService import CityService

should_use_cache = False
if os.path.isfile("cache.txt"):
    should_use_cache = input("Do you want to use your last inserted data? (Y/N)").lower() == "y"

cities = []
if should_use_cache:
    cache_file = open("cache.txt", "r")
    for line in cache_file.readlines():
        raw = line.strip("\n")
        data = raw.split(";")
        if len(data) != 3: continue
        cities.append(City(data[0], {"x": int(data[1]), "y": int(data[2])}))
    cache_file.close()


if not(should_use_cache):
    no_points = int(input("How many points do you want to insert?: "))
    open("cache.txt", "w").close()

    for i in range(no_points):
        point_alias = input("Point alias: ")
        point_x = int(input("X: "))
        point_y = int(input("Y: "))
        cities.append(City(point_alias, {"x": point_x, "y": point_y}))
        os.system("cls" if os.name == "nt" else "clear")
        cache_file = open("cache.txt", "a")
        cache_file.write(f"{point_alias};{point_x};{point_y}\n")
        cache_file.close()


city_service = CityService(cities)
path_service = PathService(city_service)
ant_service = AntService(city_service, path_service)
ant_service.start()

final_paths: list[Path] = []

# Remove duplicates
for path in path_service.paths:
   if path.destination.alias not in map(lambda p: p.start.alias, final_paths):
       final_paths.append(path)

sorted_paths = sorted(final_paths, key=lambda p: p.feromon_strength, reverse=True)[:7]

if len(sorted_paths) != len(cities):
    print("Ants didn't find path... try again")
    exit()

sum = 0
for path in sorted_paths:
    if path.feromon_strength < 1: continue
    print(f"{path.start.alias} - {path.destination.alias}: {path.feromon_strength} ")
    sum += path.distance
print(f"SUM: {sum}")

#   F - D - B - A - G - E - C - F = 36.79327012304664
#   F - D - A - G - E - B - C - F = 35.22810183197734
#   F - D - G - A - E - B - C - F = 36.5998337815729
