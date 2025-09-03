class Session:
    def __init__(self):
        self.user = None
        
    def login(self, user):
        if self.user == None:
            self.user = user
            print(f"{user} logged in")
        else:
            print("Siz Log in qilgansiz, Iltimos birinchi logout qiling")
        
    def logout(self):
        if self.user == None:
            print("Siz hali login qilmagansiz")
        else:
            print(f"{self.user} logged out")
            self.user = None


s = Session()
s.login("Ozodjon")
s.login("Ali")
s.logout()
