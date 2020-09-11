class Room:
    """
    Class: information about rooms' type, about being reserved or free
    constructor:
    instance variable 1. room_type: rooms' type (penthouse, double, single, etc  - string)
    instance variable 2. count: amount of rooms (int)
    methods:
    1. __repr__()
    2. get_type():  gets the type of the room
    3. get_count(): gets the amount of free rooms
    4. reserve(): reserving room - changes the amount of free rooms
    5. checkout(): leaving room - changes the amount of free rooms
    """

    def __init__(self, room_type, count):
        self.__room_type = room_type
        self.__count = count
        self.__total_rooms_count = count

    def __repr__(self):
        print(f'In the hotel there is {self.__count} {self.__room_type}')

    def get_type(self):
        return self.__room_type

    def get_count(self):
        return self.__count

    def reserve(self, cnt):
        try:
            if cnt > self.__count:
                raise ValueError
        except ValueError:
            print(f'Room.reserve(): Incorrect number of free rooms. We have only {self.__count} available rooms.')
        else:
            self.__count -= cnt
            print(f'Room.reserve(): {cnt} rooms has been successfully reserved.')

    def checkout(self, cnt):
        reserved_rooms_count = self.__total_rooms_count - self.__count
        try:
            if reserved_rooms_count < cnt:
                raise ValueError
        except ValueError:
            print(
                f'Room.checkout(): Incorrect number of reserved rooms. You have only reserved {reserved_rooms_count} rooms.')
        else:
            self.__count += cnt
            print(f'Room.checkout(): {cnt} rooms has been successfully checked out.')


class Hotel:
    """
    Class: information about hotel's rating, rooms' type
    constructor:
    instance variable 1. rating: hotel's rating
    instance variable 2. rater_count: amount of raters
    methods:
    1. get_rating():  gets the rating of the hotel
    2. get_rooms(): gets the amount of all rooms
    3. reserve(): calls the Room.reserve()
    4. checkout(): calls the Room.checkout()
    5. rate(): rates the hotel
    """

    def __init__(self, name, rooms_list):
        self.__name = name
        self.__rating = 0
        self.__rater_count = 0
        self.__rooms = rooms_list

    def set_rating(self, rating):
        if rating < 1 or rating > 6:
            rating = 5
        self.__rating += rating
        self.__rater_count += 1

    def get_rating(self):
        if self.__rater_count == 0:
            print('Hotel rating is: ', 0)
        print('Hotel rating is: ', self.__rating / self.__rater_count)

    def set_room(self, room):
        return self.__rooms.append(room)

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
                raise ValueError
        except ValueError:
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


def main():
    room1 = Room('penthouse', 4)
    room2 = Room('double', 10)
    room3 = Room('single', 12)
    room4 = Room('double lux', 6)
    room5 = Room('single lux', 9)

    rooms_list = [room1, room2, room3, room4, room5]

    hotel = Hotel('Plaza', rooms_list)

    hotel.reserve('penthouse', 2)
    hotel.checkout('penthouse', 2)
    hotel.set_rating(4)
    hotel.reserve('penthouse', 6)
    hotel.checkout('penthouse', 6)
    hotel.set_rating(-1000)
    hotel.get_rating()


main()
