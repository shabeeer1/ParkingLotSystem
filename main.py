from app.controllers.parkingcontroller import ParkingController

def main():
    print("Hello, World!")
    # Add your main code logic here
    Park = ParkingController(2,2,0)
    print("Add Car 1:", Park.addCar(1))
    print("Add Car 2:", Park.addCar(2))
    print("Add Car 3:", Park.addCar(3))
    print("Add one more Car 1:", Park.addCar(1))

if __name__ == "__main__":
    main()