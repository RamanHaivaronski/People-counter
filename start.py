from tkinter import Tk, filedialog, Button, Label
import people_counter as pc
import datetime
import pl


class Movie:
    filenameOpen = ""
    filenameSave = ""

    def openFile(self):
        self.filenameOpen = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                       filetypes=(("Video files", "*.mp4"), ("all files", "*.*")))
        print(self.filenameOpen)

    def saveFile(self):
        self.filenameSave = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                                         filetypes=(("Video files", "*.mp4"), ("all files", "*.*")))
        print(self.filenameSave)

    def start(self):
        info, stat = pc.counter(self.filenameOpen, self.filenameSave)
        currentDate = datetime.datetime.today()
        pl.graph(stat)


def main():
    root = Tk()
    root.title("People counter")
    root.minsize(width=1280, height=1024)

    obj = Movie()

    button1 = Button(root, text="Open Me!", command=obj.openFile)
    button1.place(x=10, y=10)

    button2 = Button(root, text="Save Me!", command=obj.saveFile)
    button2.place(x=80, y=10)

    button3 = Button(root, text="Count", command=obj.start)
    button3.place(x=150, y=10)

    root.mainloop()


if __name__ == "__main__":
    main()
