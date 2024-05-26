class StarCinema:
    __hallList=[]
    def entry_hall(hall):
        StarCinema.__hallList.append(hall)

class Hall(StarCinema):
    def __init__(self,hall_no,rows,cols) -> None:
        self.__hall_no=hall_no
        self.__rows=rows
        self.__cols=cols
        self.__show_list=[]
        self.__seats={}
        self.entry_hall()


    def entry_show(self,id,movie_name,time):
        info=[id,movie_name,time]
        seat=[[0 for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__show_list.append(info)
        self.__seats[id]=seat
    def book_seats(self, id, row, col):
        try:
            allSeats = self.__seats[id]
        except KeyError:
            print(f"Invalid Show Id")
            return
        try:
            if allSeats[row][col] != 0:
                print(f"\n\tSeat {row},{col} is already taken")
            else:
                allSeats[row][col] = 1
                print(f"\n\tSeat for {id} is booked successfully")
                print("--------------------------------------------")
                self.view_available_seats(id)
        except IndexError:
            print("Invalid seat number")

    def view_available_seats(self,id):
        allSeats=self.__seats[id]
        for i in allSeats:
            print(i)
    
    def view_show_list(self):
        for i in self.__show_list:
            print(i)
            print("-----------------------------------------------")


def first_screen():
    print("-----------------------------------------------")
    print("\t1. VIEW AVAILABLE SHOWS")
    print("\t2. VIEW AVAILABLE SEATS")
    print("\t3. BOOK TICKET")
    print("\t4. EXIT")



cineplex=Hall(111,5,10)
cineplex.entry_show(111,"Dune Part 2","4.00pm")
cineplex.entry_show(112,"Madmax furiosa","6.00pm")
cineplex.entry_show(113,"Deadpool and Wolverine","upcoming")
while True:
    first_screen()
    x=int(input())
    if x==1:
        cineplex.view_show_list()
    elif x==2:
        id=int(input("Enter show id: "))
        cineplex.view_available_seats(id)
    elif x==3:
        id=int(input("Enter show id: "))
        quantity=int(input("Number of ticket? "))
        for i in range(quantity):
            row=int(input("Enter row: "))
            col=int(input("Enter col: "))
            cineplex.book_seats(id,row,col)
    else:
        break

