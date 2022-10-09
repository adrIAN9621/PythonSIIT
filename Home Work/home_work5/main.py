import json

import uuid

if __name__ == '__main__':
    with open('cars.json') as json_file:
        data = json.load(json_file)
    # print(data)
    new_car_list = []

    for car in data:
        dic_car = dict(car)
        dic_car["ID"] = uuid.uuid4().hex
        # print(dic_car)
        new_car_list.append(dic_car)

    slow_cars = [dic_car for dic_car in new_car_list if dic_car.get("HP") < 120]
    # print("slow_cars", slow_cars)

    fast_cars = [car for car in new_car_list if 120 <= car.get("HP") < 180]
    # print("fast_cars", fast_cars)

    sport_cars = [car for car in new_car_list if car.get("HP") >= 180]
    # print("sport_cars", sport_cars)

    cheap_price = [car for car in new_car_list if car.get("Price") < 1000]
    # print("cheap_price:)", cheap_price)

    medium_price = [car for car in new_car_list if 1000 <= car.get("Price") < 5000]
    # print("medium_price:)", medium_price)

    expensive_price = [car for car in new_car_list if car.get("Price") >= 5000]
    # print("expensive_price:)", expensive_price)

    peugeot = [car for car in new_car_list if car.get("Brand") == "Peugeot"]
    # print(peugeot)
    dacia = [car for car in new_car_list if car.get("Brand") == "Dacia"]

    volkswagen = [car for car in new_car_list if car.get("Brand") == "Volkswagen"]

    audi = [car for car in new_car_list if car.get("Brand") == "Audi"]

    mercedes = [car for car in new_car_list if car.get("Brand") == "Mercedes"]

    with open('output.data/slow_cars.json', 'w') as json_file:
        json.dump(slow_cars, json_file, indent=2)

    with open('output.data/fast_cars.json', 'w') as json_file:
        json.dump(fast_cars, json_file, indent=2)

    with open('output.data/sport_cars.json', 'w') as json_file:
        json.dump(sport_cars, json_file, indent=2)

    with open('output.data/cheap_cars.json', 'w') as json_file:
        json.dump(cheap_price, json_file, indent=2)

    with open('output.data/medium_cars.json', 'w') as json_file:
        json.dump(medium_price, json_file, indent=2)

    with open('output.data/expensive_cars.json', 'w') as json_file:
        json.dump(expensive_price, json_file, indent=2)

    with open('output.data/peugeot_cars.json', 'w') as json_file:
        json.dump(peugeot, json_file, indent=2)

    with open('output.data/dacia_cars.json', 'w') as json_file:
        json.dump(dacia, json_file, indent=2)

    with open('output.data/volkswagen_cars.json', 'w') as json_file:
        json.dump(volkswagen, json_file, indent=2)

    with open('output.data/audi_cars.json', 'w') as json_file:
        json.dump(audi, json_file, indent=2)

    with open('output.data/mercedes_cars.json', 'w') as json_file:
        json.dump(mercedes, json_file, indent=2)
