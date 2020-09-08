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
        self.room_type = room_type
        self.count = count

    def __repr__(self):
        pass

    def get_type(self):
        pass

    def get_count(self):
        pass

    def reserve(self):
        pass

    def checkout(self):
        pass


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

    def __init__(self, rating, rater_count, rooms):
        self.rating = rating
        self.rater_count = rater_count
        self.rooms = rooms

    def get_rating(self):
        pass

    def get_rooms(self):
        pass

    def reserve(self):
        pass

    def checkout(self):
        pass

    def rate(self):
        pass
