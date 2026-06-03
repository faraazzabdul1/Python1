class Vehicle:

    count = 0
    total_mileage = 0

    def __init__ (self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        Vehicle.count += 1
        Vehicle.total_mileage += mileage

    def get_info(self):
        return f"{self.make} {self.model} {self.year} {self.mileage}"  
    

    @classmethod
    def get_count(cls):
        return f"Total number of vehicles: {cls.count}"
    
    @classmethod
    def get_average_mileage(cls):
        if cls.count == 0:
            return 0
        return cls.total_mileage / cls.count

vehicle1 = Vehicle ("Volkswagen", "Jetta", "2024", 36550)
vehicle2 = Vehicle ("Lamborghini", "Urus", "2026", 12000)
vehicle3 = Vehicle ("Mercedes-Benz", "AMG C63", "2025", 56000)
vehicle4 = Vehicle ("Honda", "Civic", "2002", 200000 )

print (Vehicle.get_count())
print (Vehicle.get_average_mileage())