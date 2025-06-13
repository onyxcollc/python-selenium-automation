
# Examples 
class Page:
    def click(self):
        print("clicking....")

    def find_element(self):
        print('Searching ....')

    def verify_text(self):
        print('Testing for text')

class LoginPage(Page):
    def login(self):
        print('Loging ')

class SignupPage(Page):
    def signup(self):
        print('registering')



login_page = LoginPage()