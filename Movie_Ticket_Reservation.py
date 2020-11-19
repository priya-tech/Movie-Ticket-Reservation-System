class Movie:
    def __init__(self,name,code,date,price):
        self.name=name
        self.code=code
        self.date=date
        self.price=price

    def display(self):
        print(self.name,self.code,self.date,self.price)

class Person:
    def __init__(self,name,password,age,mobile):
        self.name=name
        self.password=password
        self.age=age
        self.mobile=mobile

    def display(self):
        print(self.name,self.password,self.age,self.mobile)

class Booking(Movie):
    def __init__(self,Pname,mobile,seats,name,code,date,price):
        super().__init__(name,code,date,price)
        self.Personname=Pname
        self.mobile=mobile
        self.seats=seats
        self.amount=seats*self.price

    def display(self):
        print(self.Personname,self.mobile,self.seats,self.amount,self.name)


movie_list=[]
Transactions_list=[]
Person_list=[]

def insert_movie():
    name=input("\n Enter Movie Name")
    find=0
    for movie in movie_list:
        if movie.name==name:
            print("\n Movie name already exists ")
            return
    code=input("\n Enter Movie Code")
    date=input("\n Enter Movie date")
    price=int(input("\n Enter Movie Price"))
    movie_list.append(Movie(name,code,date,price))
    print("\n Movie Inserted Successfully")
    return

def view_movies():
    if movie_list:
        print("\n Name   Code  Date  Price")
        for movie in movie_list:
            movie.display()
    else:
        print("\nMovie List is empty")


def find_movie():
    name=input("\n Enter the movie name for find  ")
    if not (movie_list):
        print("\nMovie List is empty")
        return
    for movie in movie_list:
        if movie.name==name:
            print("\n The movie details you searched are")
            movie.display()
            return
    print("\n The details are not found try with another one")

def book_ticket(person):
    print("\n The movie details are")
    view_movies()
    name=input("\n Enter the movie name for booking")
    for movie in movie_list:
        if movie.name==name:
            seats=int(input("\n Enter No.of seats"))
            Transactions_list.append(Booking(person.name,person.mobile,seats,movie.name,movie.code,movie.date,movie.price))
            print("\n Movie Booked Successfully")
        else:
            print("\n Movie name is not in the list :( Try with another one")

def all_transactions():
    if Transactions_list:
        print("\n Name  Mobile  Seats  Amount  MovieName")
        for Transactions in Transactions_list:
            Transactions.display()
    else:
        print("\n List is empty")

def view_transactions(person):
    find=0
    for Transactions in Transactions_list:
        if Transactions.Personname == person.name:
            if find==0:
                print("\nName  Mobile  Seats  Amount  MovieName")
            find=1
            Transactions.display()
    if find==0:
        print("\n OOPS :( You have no transactions yet! ")

def view_profile(person):
    print("\n Name is "+person.name)
    print("\n password is "+person.password)
    print("\n age is"+person.age)
    print("\n  mobile is "+person.mobile)

def menu(person):
    while True:
        print("\n WELCOME "+person.name+"\n Enter 1.View Movies \n 2.Find Movie \n 3.Booking \n 4.View Transactions \n 5.View Profile \n 0.logout")
        choice=int(input())
        if choice==1:
            view_movies()
        elif choice==2:
            find_movie()
        elif choice==3:
            book_ticket(person)
        elif choice==4:
            view_transactions(person)
        elif choice==5:
            view_profile(person)
        elif choice==0:
            return
        else:
            print("\n Please enter correct one")

def Register():
    name=input("\n Enter Your Name")
    for person in Person_list:
        if person.name==name:
            print("\n name already exists try with another one")
            return
    password=input("\n Enter password")
    age=input("\n Enter age")
    mobile=input("\n Enter Mobile")
    Person_list.append(Person(name,password,age,mobile))
    print("\n  Registered Successfully")

def login():
    find=0
    name=input("\n Enter Name")
    for person in Person_list:
        if person.name==name:
            find=1
            password=input("Enter password")
            if password==person.password:
                print("\n Login Successfully")
                menu(person)
            else:
                print("password entered wrongly")
    if find==0:
        print("name doesnt exists")

def admin_login():
    print("Admin Login")
    name=input("Enter Username")
    if name=="admin":
        password=input("Enter Password")
        if password=="admin":
            print("\n WELCOME Admin")
            while True:
                print("\n 1.Insert Movies \n 2.View Movies \n 3.View all Transactions\n 0.logout")
                choice=int(input())
                if choice==1:
                    insert_movie()
                elif choice==2:
                    view_movies()
                elif choice==3:
                    all_transactions()
                elif choice==0:
                    return
                else:
                    print("\n Please enter correct one")
        else:
            print("\n Password is incorrect")


if __name__ == "__main__":
    while True:
        print("\nEnter 1.Admin login \n 2.User Register \n 3.User Login \n 4.Exit")
        choice=int(input())
        if choice==1:
            admin_login()
        elif choice==2:
            Register()
        elif choice==3:
            login()
        elif choice==4:
            exit()
        else:
            print("\n Please enter correct one")
