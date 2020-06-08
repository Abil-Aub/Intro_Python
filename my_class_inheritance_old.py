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
    try:
        if (float(row[5]) <= 0) or (not check(row[3])) or \
           row[1]:
            raise ValueError
        if(row[0]=='car'):
            if not (int(row[2]) <=0 ):
                raise ValueError
            return Car(row[1], row[3], row[5], row[2])
        elif(row[0]=='truck'):
            return Truck(row[1], row[3], row[5], row[4])
        elif(row[0]=='spec_machine'):
            if not row[6]:
                raise ValueError
            return SpecMachine(row[1], row[3], row[5], row[6])
    except:
        pass

        
def get_car_list(csv_filename):
    car_list = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # skip titles
        for row in reader:
            next_car = get_car(row)
            if(next_car):
                car_list.append(next_car)

    return car_list
