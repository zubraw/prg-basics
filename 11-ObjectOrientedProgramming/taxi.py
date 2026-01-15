class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km 
    
    def print_receipt(self):
        print('PRINT RECEIPT')
        print('================')
        print(f'Distance: {self.distance} km')
        print(f'Rate: ${self.rate_per_km}')
        print(f'Fare: ${self.fare:.2f}')


def main():
    # your program
    ride1 = TaxiRide(2)
    ride1.calculate_fare(10)
    ride1.print_receipt()

    ride2 = TaxiRide(1.5)
    ride2.calculate_fare(16)
    ride2.print_receipt()

if __name__ == "__main__":
    main()
