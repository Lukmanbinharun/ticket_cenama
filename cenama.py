class star_cinema:
    __hall_list = []

    def entry_hall(self, hall):
        self.__hall_list.append(hall)


class Hall(star_cinema):
    def __init__(self, row, col, hall_no):
        self.__seats = {}
        self.__show_list = []
        self._avil_seat_num = {}
        self._row = row
        self._col = col
        self._hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self, id, movey_name, time):
        self.__show_list.append((id, movey_name, time))
        self.oll_sets = [[True for i in range(self._col)] for j in range(self._row)]
        self.__seats[id] = self.oll_sets
        self._avil_seat_num[id] = self._row * self._col

    def book_seats(self, cos_name, number, id, seat):
        for i in self.__show_list:
            if i[0] == id:
                move_name = i[1]
                break
        print('\n_____________________________________\n')
        print(f"Name: {cos_name}  Number: {number}")
        print(f"Move Id: {id}   Move name: {move_name}")
        print(f"booked seat :",end=' ')
        self._avil_seat_num[id] -= len(seat)
        for i in seat:
            a = ord(i[0]) - 65
            b = int(i[1])
            if len(i) > 2:
                b = int(i[1] + i[2])
            print(i[0]+i[1],end=' ')
            self.__seats[id][a][b] = False
        print('\n_____________________________________\n')
           

           
    def view_show_list(self):
        print('_____________________________________\n1')
        print(f"Hall Number: {self._hall_no}")
        for i in self.__show_list:
            print(f'Move Id: {i[0]}  Move name: {i[1]}  Time: {i[2]}')
        print('_____________________________________\n')

    def view_aviable_sets(self, id):
        print("___________________________________\n")
        print("xx for allready booked seat")
        print(f'Avilavle seats = {self._avil_seat_num[id]}')
        a = 65
        for i in self.__seats[id]:
            b = 0
            for j in i:
                if j == True:
                    print(chr(a)+f"{b}", end='  ')
                else:
                    print('xx', end='  ')
                b += 1
            print('')
            a += 1
        print("___________________________________\n")
    def is_valid_id(self, id):
        for i in self.__seats:
            if i == id:
                return True
        print("This id is not valid, please enter a valid id")
        self.view_show_list()
        return False

    def is_valid_seat(self, id, seat_no,li):
        a = ord(seat_no[0]) - 65
        b = int(seat_no[1])
        if len(seat_no) > 2:
            b = int(seat_no[1] + seat_no[2])
        if a >= self._row or b >= self._col:
            print('invalid seat number,please enter a valid number')
            return False
        if self.__seats[id][a][b] == False:
            print('This seat allready booked,choose other seat')
            return False
        for i in li:
            if seat_no[0] == i[0] and str(b) == i[1]:
                print("YOU already booked it")
                return False

        return True


a = Hall(5,10, 1)
a.entry_show('a1', 'Targan', '5:30')
a.entry_show('b1', 'Hare potar', '8:00')

while 1:
    print('')
    print('1. View all show today')
    print('2. view avilable seats')
    print('3. Book ticket \n')
    com = int(input('Enter option: '))
    if com == 1:
        a.view_show_list()
    elif com == 2:
        id = input('Enter movey id: ')
        while not (a.is_valid_id(id)):
            id = input('Enter movey id: ')
        a.view_aviable_sets(id)
    else :
        name = input('Enter name: ')
        num = input('Enter number: ')
        id = input('Enter move id: ')
        while not (a.is_valid_id(id)):
            id = input('Enter movey id: ')
        num_seats = int(input('How maney seats do you need: '))
        if a._avil_seat_num[id] < num_seats:
            if a._avil_seat_num[id] == 0:
                print("Sorry,No seats avilable")
                continue
            else:
                print("Not enought seat")
                print(f"Only {a._avil_seat_num[id]} is free")
            continue
        li = []
        for i in range(num_seats):
            while True:
                s = input('Enter a seat number: ')
                b = s[1]
                if len(s) > 2:
                    b = s[1] + s[2]
                if a.is_valid_seat(id, s,li) == True:
                    li.append((s[0], b))
                    break
        a.book_seats(name, num, id, li)

