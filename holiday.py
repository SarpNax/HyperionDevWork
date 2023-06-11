def hotel_cost(flight, num_nights, hotel_price):  # Hotel cost per night function.
    if flight == "VIENNA":
        hotel_cost = float(num_nights) * float(hotel_price[0])
        return(hotel_cost)
    elif flight == "BARCELONA":
        hotel_cost = float(num_nights) * float(hotel_price[1])
        return(hotel_cost)
    elif flight == "SANTIAGO DE CHILE":
        hotel_cost = float(num_nights) * float(hotel_price[2])
        return(hotel_cost)
    elif flight == "TOKYO":
        hotel_cost = float(num_nights) * float(hotel_price[3])
        return(hotel_cost)#
def plane_cost(flight, city_cost):  #Plane cost function taking flight and city.
    if flight == "VIENNA":
        flight_cost = city_cost[0]
        return(float(flight_cost))
    elif flight == "BARCELONA":
        flight_cost = city_cost[1]
        return(float(flight_cost))
    elif flight == "SANTIAGO DE CHILE":
        flight_cost = city_cost[2]
        return(float(flight_cost))
    elif flight == "TOKYO":
        flight_cost = city_cost[3]
        return(float(flight_cost))
def car_rental (flight, rental_days, rental_cost): # function for price for days renting a car
    if flight == "VIENNA":
        car_rent_p = float(rental_days) * float(rental_cost[0])
        return(car_rent_p)
    elif flight == "BARCELONA":
        car_rent_p = float(rental_days) * float(rental_cost[1])
        return(car_rent_p)
    elif flight == "SANTIAGO DE CHILE":
        car_rent_p = float(rental_days) * float(rental_cost[2])
        return(car_rent_p)
    elif flight == "TOKYO":
        car_rent_p = float(rental_days) * float(rental_cost[3])
        return(car_rent_p)
def holiday_cost (cost1, cost2, cost3):
    holiday_cost = float(cost1) + float(cost2) + float(cost3)
    return(holiday_cost)
hotel_price = [65, 60, 120, 300]  # Hotel price list
city_cost = [350, 300, 1000, 1000]  # Flight cost to city
rental_cost = [50, 45, 35, 20]  # Car rental cost
city_flight = ["VIENNA", "BARCELONA", "SANTIAGO DE CHILE", "TOKYO"]  # Cities we offer flights to
hotel_c = " "  # the cost of the hotel with days
# next 3 Loops are first for which flight then how long in a hotel and then how many days the customer rents the car
while True:
    print("Welcome to the flight calculator")
    print("Please pick a destination from one of our 4 exclusive offers")
    flight = input("Vienna, Barcelona, Santiago de Chile, Tokyo \n >").upper()
    if flight in city_flight:
        print("thank you for your input")
        break
    else:
        print("please enter a valid destination!")
while True:
    num_nights = (input("Please enter the number of nights in a hotel e.g. 4\n> "))
    if num_nights.isnumeric():
        print("thank you for your input")
        break
    else:
        print("Please input a valid entry")
while True:
    rental_days = (input("Please enter the number of days you will rent a vehicle eg 3 \n> "))
    if rental_days.isnumeric():
        print("thank you for your input")
        break
    else:
        print("Please input a valid entry")
print("You have selected")
print("\nDestination> "+flight+"\nStays in hotel(nights)> "+num_nights+"\nRental days for vehicle> "+rental_days)
# Variables for the last function needing to be defined after flight
cost1 = hotel_cost(flight, num_nights, hotel_price)
cost2 = plane_cost(flight, city_cost)
cost3 = car_rental(flight, num_nights, rental_cost)
print("Breakdown of Costs\nHotel total>£", (hotel_cost(flight, num_nights, hotel_price)))
print("Flight total> £", (plane_cost(flight, city_cost)))
print("Car rental total> £", (car_rental(flight, num_nights, rental_cost)))
print("Total Cost of the Holiday >£", (holiday_cost(cost1, cost2, cost3)))
