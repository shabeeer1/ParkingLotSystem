from app.models.parkingmodel import ParkingModel

class ParkingService:
    def __init__(self, big, medium, small):
        self.parking_model = ParkingModel(big, medium, small)

    def add_car(self, car):
        return self.parking_model.add_car(car)

    def get_car_count(self, car):
        print("Car Count:", self.parking_model.ParkingSpace)
        return self.parking_model.get_car_count(car)