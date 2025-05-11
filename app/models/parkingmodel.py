from app.enums.vehicletype import VehicleType

class ParkingModel:
    def __init__(self, big: int, medium: int, small: int):
        self.ParkingSpace = {
            VehicleType.BIG: big,
            VehicleType.MEDIUM: medium,
            VehicleType.SMALL: small
        }
    def add_car(self, car):
        car_type = self._get_vehicle_type(car)
        print("Car Type:", car_type, self.get_car_count(car_type))
        if self.get_car_count(car_type) > 0:
            self.ParkingSpace[car_type] -= 1
            return True

        return False
    def get_car_count(self, car):
        # print("Car Count:", self.ParkingSpace)
        return self.ParkingSpace[car] if car in self.ParkingSpace else 0
    
    def _get_vehicle_type(self, car):
        # Helper method to convert integer to VehicleType
        if isinstance(car, int):
            return VehicleType(car)
        return car