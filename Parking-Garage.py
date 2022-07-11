class parking_garage():
    tickets = [{1:""}, {2:""}, {3:""}, {4:"open"}, {5:""}]
    parking_spaces = [{1:""}, {2:""}, {3:""}, {4:""}, {5:""}]
    current_ticket = {}
    filled_parking_spot = {}

    def take_ticket(self):
        if self.tickets:
            print("Please go park.")
            print(self.tickets[0])
            self.current_ticket.update(self.tickets[0])
            del self.tickets[0]
            self.filled_parking_spot = self.parking_spaces[0]
            del self.parking_spaces[0]
        else:
            print("Parking garage is currently full. Please come back later.")

    def pay_for_parking(self):
        while True:
            pay = int(input("Please enter your ticket number:  "))
            if 0 < pay < 6 and pay in self.current_ticket:
                if self.current_ticket[pay]:
                    print("You have paid your ticket please leave within 10min.")
                    break
                else:
                    self.current_ticket[pay]=("paid")
                    break
            


    def leave_garage(self):
        while True:
            exit = int(input("What is your ticket number please?:  "))
            if 0 < exit < 6 and exit in self.current_ticket:
                if self.current_ticket[exit] == ('paid'):
                    print("Thanks, have a great day!")
                    self.current_ticket[exit]
                    self.tickets.append(self.current_ticket)
                    self.parking_spaces.append(self.current_ticket)
                    break
                else:
                    print("You have not paid your ticket. Please pay.  ")
                    break
            

    def com(self):
        while True:
            response = str(input("\n What would you like to do? Park, Pay, Leave or Quit \n")).lower()
            if response == "park":
                self.take_ticket()
            if response == "pay":
                self.pay_for_parking()
            if response == "leave":
                self.leave_garage()
            if response == "quit":
                print("Have a great day!")
                break
            

test = parking_garage()
test.com()