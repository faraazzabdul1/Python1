class Vehicle:

    vehicle_brand = String
    vehicle_model = String

    def _init__(self, make, model):
        self.make = make
        self.model = model
        Vehicle.count += 1
        Vehnical.total_vehicles += 1

    def display_info(self):
        return f"{self.make} {self.model}"
    

    @classmethod
    def get_vehicle_count(cls):
        return f" Total Vehcicles Created: {cls.count}"
    
    @classmethod
    def get_average_vehicles(cls):
        if cls.total_vehicles == 0:
            return "No vehicles created yet."
        else:
            average = cls.count / cls.total_vehicles
            return f"Average Vehicles per Creation: {average:.2f}"
    
vehicle1 =Vehicle("Volkswagen", "Jetta")
vehicle2 =Vehicle("Mercedes-Benz", "C63 AMG")
vehicle3 =Vehicle("BMW", "M3 Competition")

print (Vehicle.get_vehicle_count())