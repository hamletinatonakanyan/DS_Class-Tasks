class Room:
    """
    Class: as arguments gets the type and amount of free rooms, returns available free rooms type and count.
    class field 1. room_type: rooms' type (penthouse, double, single, etc  - string)
    class field 2. count: amount of rooms (int)
    methods:
    1. __repr__()
    2. get_type():  returns the type of the room
    3. get_count(): returns the amount of free rooms
    4. reserve(): takes room's count - returns message about amount of successfully or not reserved rooms.
    5. checkout(): takes room's count - returns messagea about amount of successfully or not checked out rooms.
    """

    def __init__(self, room_type, count):
        self.__room_type = room_type
        self.__count = count
        self.__total_rooms_count = count

    def __repr__(self):
        return f'In the hotel there is {self.__count} {self.__room_type}'

    def get_type(self):
        return self.__room_type

    def get_count(self):
        return self.__count

    def reserve(self, cnt):
        try:
            if cnt > self.__count:
                raise ReservationException
        except ReservationException:
            print(f'Room.reserve(): Incorrect number of free rooms. We have only {self.__count} available rooms.')
        else:
            self.__count -= cnt
            print(f'Room.reserve(): {cnt} rooms has been successfully reserved.')

    def checkout(self, cnt):
        reserved_rooms_count = self.__total_rooms_count - self.__count
        try:
            if reserved_rooms_count < cnt:
                raise ReservationException
        except ReservationException:
            print(f'Room.checkout(): Incorrect number of rooms for checking out. You have reserved only {reserved_rooms_count} rooms.')
        else:
            self.__count += cnt
            print(f'Room.checkout(): {cnt} rooms has been successfully checked out.')


class Hotel:
    """
    Class: as arguments takes hotel's name and list of Room type objects.
    class fields:
    1. name - str, hotel's name
    2.rating - int, hotel's rating
    3.rater count - int, counts how many different customers have rated
    4. rooms - lst, takes list of Room type objects
    methods:
    1. set_rating(): takes rating, checks and add to total rating, increases total number of raters
    2. get_rating(): counts and returns the total rating of the hotel
    3. set_rooms(): to the list appends new  Room type objects
    4. get_rooms(): returns list of Room type objects
    5. get_room_by_type(): takes room_type as argument, checks if it exists in the list of rooms, returns the relevant Room object by type
    6. operation(): takes room_type, count of room, operation type(reserve or checkout), returns reserved/checked out rooms \
                   or information about incorrect type of provided room
    7. reserve(): takes room's type and count, calls operation() method
    8. checkout(): takes room's type and count, calls operation() method
    9. get_hotel_name(): returns hotel's name

    """

    def __init__(self, name, rooms_list):
        self.__name = name
        self.__rating = 0
        self.__rater_count = 0
        self.__rooms = rooms_list

    def get_hotel_name(self):
        return self.__name

    def set_rating(self, rating):
        if rating < 1 or rating > 6:
            rating = 5
        self.__rating += rating
        self.__rater_count += 1
        print(f'Thank you for rating, you rated {rating} for the {self.get_hotel_name()} hotel.')

    def get_rating(self):
        if self.__rater_count == 0:
            print('Hotel rating is: ', 0)
        print(f'{self.get_hotel_name()} hotel\'s rating is: {self.__rating / self.__rater_count}')

    def set_rooms(self, room):
        self.__rooms.append(room)

    def get_room_by_type(self, room_type):
        for r in self.__rooms:
            if r.get_type() == room_type:
                return r
        return None

    def get_rooms(self):
        return self.__rooms

    def operation(self, room_type, cnt, operation_type):
        room = self.get_room_by_type(room_type)

        try:
            if room is None:
                raise ReservationException
        except ReservationException:
            print(f"Hotel.{operation_type} : Incorrect room type. Provided {room_type} room type is not valid.")
        else:
            if operation_type == 'reserve()':
                room.reserve(cnt)
            elif operation_type == 'checkout()':
                room.checkout(cnt)

    def reserve(self, room_type, cnt):
        self.operation(room_type, cnt, 'reserve()')

    def checkout(self, room_type, cnt):
        self.operation(room_type, cnt, 'checkout()')


class Customer:
    """
    Class: as argument takes list of hotels(class field)
    methods:
    1. get_hotel_by_name(): checks if the hotel exists in the list of hotels or not and return Hotel type object
    2. reservation(): as argument takes hotel's name, room's type and count, through calling hotel reservation \
                      returns message about successfully or not room's reserving.
    3. checking_out(): works same as reservation()
    4. rate(): through Hotel.set_rating() rates Hotel, where was reserved the room.
    """

    def __init__(self, hotel_list):
        self.__hotel_list = hotel_list

    def get_hotel_by_name(self, name):
        for n in self.__hotel_list:
            if name == n.get_hotel_name():
                return n
        return None

    def reservation(self, hotel_name, room_type, room_count):
        hotel = self.get_hotel_by_name(hotel_name)

        try:
            if hotel is None:
                raise ReservationException
        except ReservationException:
            print(f"Customer.checkout(): There isn't hotel by {hotel_name}.")
        else:
            return hotel.reserve(room_type, room_count)

    def checking_out(self, hotel_name, room_type, room_count):
        hotel = self.get_hotel_by_name(hotel_name)
        return hotel.checkout(room_type, room_count)

    def rate(self, hotel_name, rate):
        hotel = self.get_hotel_by_name(hotel_name)
        return hotel.set_rating(rate)


class ReservationException(Exception):
    pass


def main():
    room1 = Room('president', 4)
    room2 = Room('double', 10)
    room3 = Room('single', 12)
    room4 = Room('double lux', 6)
    room5 = Room('single lux', 9)
    rooms_list1 = [room1, room2,  room4, room5]
    rooms_list2 = [room1, room2, room3]
    rooms_list3 = [room2, room3, room4, room5]

    hotel1 = Hotel('Messier87', rooms_list1)
    hotel2 = Hotel('Andromeda', rooms_list2)
    hotel3 = Hotel('Halsey', rooms_list3)
    hotels_list = [hotel1, hotel2, hotel3]

    customer1 = Customer(hotels_list)
    customer1.reservation('Messier87', 'president', 2)
    customer1.checking_out('Messier87', 'president', 2)
    customer1.rate('Messier87', 4.6)
    hotel1.get_rating()


main()
