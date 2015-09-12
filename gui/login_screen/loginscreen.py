#Python Libs imports
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.properties import ObjectProperty
from kivy.animation import Animation
import pymysql
#Personnal Libs imports
from user.user import User
from database.db import MyDB

#Class creating the Login_screen
class MascaretLoginScreen(FloatLayout):
    login_box = ObjectProperty()
    password_box = ObjectProperty()
    error_box = ObjectProperty()
    login_area = ObjectProperty()

    def __init__(self):
        super(MascaretLoginScreen, self).__init__()
        self.register_event_type('on_right_id')

    def login(self):
        animation = Animation(x=self.login_area.x - self.login_area.width, duration=0.8)
        animation.start(self.login_area)
        self.pan_screen= Image(source= "gui/login_screen/loading", keep_ratio= False, allow_stretch= True,
                        color= (1, 1, 1, 0.1))
        self.add_widget(self.pan_screen)
        animation.bind(on_complete=self.check_login)

    def check_login(self, *args):
        user_login = self.login_box.text
        user_password = self.password_box.text


        # DB CONNECTION
        db = MyDB()

        login_query = "SELECT * FROM utilisateur WHERE login =%s AND password = %s"

        parameters_query =[user_login,user_password]

        try:
            db.query(login_query,parameters_query)
            db.commit()
        except:
            db.rollback()

        login_data = db.db_fetchall()

        if login_data:

            user_logged = User(user_login)
            self.dispatch('on_right_id')


        else:
            self.login_box.focus = True
            self.remove_widget(self.pan_screen)
            self.error_box.text = "Wrong credentials"
            # create an animation object. This object could be stored
            # and reused each call or reused across different widgets.
            # += is a sequential step, while &= is in parallel
            animation = Animation(x=(0), t='out_bounce')

            # apply the animation on the button, passed in the "instance" argument
            # Notice that default 'click' animation (changing the button
            # color while the mouse is down) is unchanged.
            animation.start(self.login_area)

    def on_right_id(self):
        pass
