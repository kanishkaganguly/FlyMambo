from mambo_utils.Mambo import Mambo

'''
Thanks to https://github.com/amymcgovern/pyparrot for the original interface
on which this wrapper has been built
'''


class FlyMambo(object):
    def __init__(self, mamboAddr):
        print("Initializing Mambo...")
        self.mamboAddr = mamboAddr
        self.mambo = Mambo(mamboAddr, use_wifi=True)
        print("Trying to connect...")
        self.success = self.mambo.connect(num_retries=5)
        if not self.success:
            print("Failed to connect...")
            exit(0)
        else:
            print("Connected to Mambo...")
            print("sleeping")
            self.mambo.smart_sleep(2)
            self.mambo.ask_for_state_update()
            self.mambo.smart_sleep(2)
            self.set_mode("NORMAL")
            print("Mambo ready to fly...")

    def set_mode(self, mode="NORMAL"):
        if mode == "NORMAL":
            self.mambo.set_max_tilt(7.0)
            self.mambo.set_max_vertical_speed(0.5)
            print("Mambo in NORMAL mode...")
        elif mode == "SPORT":
            self.mambo.set_max_tilt(30.0)
            self.mambo.set_max_vertical_speed(3.0)
            print("Mambo in SPORT mode...")

    def move_mambo(self, move="STOP", amount=50.0, degrees=0.0):
        print(("Mambo moving %s by %.2f%%") % (move, amount))
        if move == "STOP":
            self.mambo.hover()
        elif move == "FWD":
            self.mambo.fly_direct(0.0, amount, 0.0, 0.0, 0.25)
        elif move == "BCK":
            self.mambo.fly_direct(0.0, -amount, 0.0, 0.0, 0.25)
        elif move == "RGT":
            self.mambo.fly_direct(amount, 0.0, 0.0, 0.0, 0.25)
        elif move == "LFT":
            self.mambo.fly_direct(-amount, 0.0, 0.0, 0.0, 0.25)
        elif move == "UP":
            self.mambo.fly_direct(0.0, 0.0, 0.0, amount, 0.25)
        elif move == "DWN":
            self.mambo.fly_direct(0.0, 0.0, 0.0, -amount, 0.25)
        elif move == "RGT_TURN":
            self.mambo.turn_degrees(degrees)
        elif move == "LFT_TURN":
            self.mambo.turn_degrees(-degrees)
        self.mambo.smart_sleep(1)

    def takeoff(self):
        print("Mambo taking off...")
        self.mambo.safe_takeoff(10)

    def land(self):
        print("Mambo landing...")
        self.mambo.safe_land(10)

    def emergency(self):
        print("Mambo emergency landing...")
        self.mambo.safe_emergency(2)

    def get_battery(self):
        print(self.mambo.sensors.battery)
        return self.mambo.sensors.battery
