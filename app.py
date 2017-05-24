from util import run2
import Tkinter


class IssTrackerGui(Tkinter.Tk):

    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.stime = 5000
        self.labelDist = Tkinter.Label()
        self.distance = run2()
        self.strDist = Tkinter.StringVar()

        self.initialize()

    def initialize(self):
        self.grid()

        self.labelDist = Tkinter.Label(self, anchor="w", fg="black", textvariable=self.strDist)
        self.labelDist.grid(column=1, row=1, columnspan=2, sticky="nsew")
        self.start()

    def start(self):
        self.distance = run2()
        self.strDist.set("Distance to ISS: " + str(self.distance) + " km")

        self.after(self.stime, self.start)


app = IssTrackerGui(None)
app.title('ISS Tracker')
app.mainloop()
