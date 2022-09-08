class Truck:
    def __init__(self, capacity, speed, depart_time, packages, miles, address, loaded):
        self.capacity = capacity
        self.speed = speed
        self.depart_time = depart_time
        self.packages = packages
        self.miles = miles
        self.address = address
        self.loaded = loaded
        self.time = depart_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.capacity, self.speed, self.depart_time, self.packages,
                                               self.miles, self.address, self.loaded)
