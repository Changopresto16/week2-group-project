class parkingGarage():
    tickets = [{1:""}, {2:""}, {3:""}, {4:""}, {5:""}]
    parkingSpaces = [{1:""}, {2:""}, {3:""}, {4:""}, {5:""}]
    currentTicket = {}
    filledParkingSpot = {}

    def takeTicket(self):
        if self.tickets:
            print(self.tickets[0])
            del self.tickets[0]
            self.takenParking = self.parkingSpaces[0]
            del self.parkingSpaces[0]
        else:
            print("Parking garage is currently full. Please come back later.")

    def payForParking(self):
        if self.parkingSpaces:
            print("What is your parking ticket number?")
            print(self.tickets[0])
            self.currentTicket.update(self.tickets[0])