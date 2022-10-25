class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the gam'es settings"""
        # Screen Settings
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230,230,230)

        # Ship Settings
        self.ship_speed = 1.5