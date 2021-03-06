import os
import csv

class CarBase():
    def __init__(self, brand, photo_file_name, carrying):
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying,
                 passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying,
                 body_whl="0.0x0.0x0.0"):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "truck"
        
        try:
            self.body_length, \
            self.body_width, \
            self.body_height = map(float, body_whl.split("x"))
        except ValueError:
            self.body_length, \
            self.body_width, \
            self.body_height = 0.0, 0.0, 0.0

    def get_body_volume(self):
        return self.body_length*self.body_width* \
               self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying,
                 extra):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra


def check(lst):
	if lst[-4:] in set(['.png', '.jpg', '.gif']) or \
           lst[-5:] == '.jpeg':
		return True
	return False


def get_car(row):
    if row[0] == 'car' and all((row[1], row[3])) and check(row[3]):
        try:
            return Car(row[1], row[3], float(row[5]), int(row[2]))
        except ValueError:
            pass

    elif row[0] == 'truck' and all((row[1], row[3])) and check(row[3]):
        try:
            return Truck(row[1], row[3], float(row[5]), row[4])
        except ValueError:
            pass

    elif row[0] == 'spec_machine' and all((row[1], row[3], row[6])) and check(row[3]):
        try:
            return SpecMachine(row[1], row[3], float(row[5]), row[6])
        except ValueError:
            pass

        
def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # skip titles
        for row in reader:
            if len(row) == 7:
                next_car = get_car(row)
                if(next_car):
                    car_list.append(next_car)

    return car_list
