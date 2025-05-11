from app.services.parkingservice import ParkingService

class ParkingController:
    def __init__(self, big, medium, small):
        self.car_service = ParkingService(big, medium, small)

    def get_all_cars(self):
        return self.car_service.get_all_cars()

    def get_car_by_id(self, car_id):
        return self.car_service.get_car_by_id(car_id)

    def addCar(self, car_data):
        return self.car_service.add_car(car_data)

    def get_car_count(self, car_type):
        return self.car_service.get_car_count(car_type)