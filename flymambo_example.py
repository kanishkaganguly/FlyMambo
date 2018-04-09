from flymambo import *


def main():
    try:
        mamboAddr = "e0:14:d0:63:3d:d0"
        fly = FlyMambo(mamboAddr)
        fly.get_battery()
        fly.takeoff()
        for i in range(2):
            fly.move_mambo(move="FWD", amount=50)
        fly.move_mambo(move="RGT_TURN", degrees=180)
        fly.land()
        exit(0)
    except KeyboardInterrupt:
        fly.emergency()
    return


if __name__ == '__main__':
    main()
