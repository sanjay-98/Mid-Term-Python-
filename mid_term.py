class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(self, hall):
        self._hall_list.append(hall)

class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._seats[id] = [['O'] * self._cols for _ in range(self._rows)]

    def book_seats(self, id, seat_list):
        if id not in self._seats:
            raise ValueError("Error ID")
        for row, col in seat_list:
            if row < 1 or row > self._rows or col < 1 or col > self._cols:
                raise ValueError("Invalid seat")
            if self._seats[id][row - 1][col - 1] == True:
                raise ValueError("Seat has already booked")
            self._seats[id][row - 1][col - 1] = True

    def view_show_list(self):
        return self._show_list

    def view_available_seats(self, id):
        if id not in self._seats:
            raise ValueError("Error ID")
        return [[(i + 1, j + 1) for j, seat in enumerate(row) if seat == 'O'] for i, row in enumerate(self._seats[id])]


hall101 = Hall(5, 10, 1)
hall101.entry_show(1, "ABC", "01:00 PM")
hall101.book_seats(1, [(1, 5), (2, 4)])
print(hall101.view_show_list())
print(hall101.view_available_seats(1))