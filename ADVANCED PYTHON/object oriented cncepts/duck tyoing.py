class Pycharm:
    def open(self):
        print("opening in pycharm")
    def run(self):
        print("run in pycharm")
    def debug(self):
        print("debugging in pycharm")
class Vscode:
    def open(self):
        print("opening in vscode")
    def run(self):
        print("run in vscode")
    def debug(self):
        print("debugging in vscode")
class Programmer:
    def coding(self,ide):
        ide.open()
        ide.run()
        ide.debug()
p1=Pycharm()
m1=Programmer()
m1.coding(p1)
