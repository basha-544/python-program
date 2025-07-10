class Application:
    def TurnOn(self):
        print()
class Wmachine(Application):
    def TurnOn(self=None):
        print("washingmachine is on")
class fridge(Application):
    def TurnOn(self=None):
        print("fridge is on")
wm = Wmachine()
Wmachine.TurnOn()
fm = fridge()
fridge.TurnOn()