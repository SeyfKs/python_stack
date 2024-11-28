class User:

    def __init__(self, first_name, last_name, email, age):    

        self.first_name = first_name 
        self.last_name  = last_name
        self.email = email 
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        
        print(f"\n First Name is {self.first_name}\n", 
            f"Last Name is {self.last_name}\n",
            f"Email is {self.email}\n",
            f"Age is {self.age}")
        if self.gold_card_points> 0:
            print (f"\n Your gold card points are {self.gold_card_points} ")
        else:
            print (f"\n you are not a memeber ")

        return self

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points += 200
        return self
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount
        return self





user1 = User("Sabrina", "harvey","sab.harvey@gmail.com",26)
user2= User("Mark", "Lowe","mrk.lw@gmail.com",37)
user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()

