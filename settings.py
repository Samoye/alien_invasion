
class Settings():

    def __init__(self):

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (240, 255, 255)
        self.ship_speed_factor = 3

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 10
        self.ship_limit = 3

