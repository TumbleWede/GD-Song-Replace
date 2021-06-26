# Don't roast my code please lol
from os import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *

def main():
    # Creating the window
    root = Tk()
    root.title("GD Song Replace")
    root.iconbitmap("logo.ico")
    root.geometry("300x100")
    root.resizable(False, False)
    root.anchor(CENTER)

    def select_file():
        # Open file prompt
        filename = askopenfilename(title = "Select a Song", filetypes = (("Audio Files", "*.mp3 OR *.wav OR *.ogg"), ("All Files", "*.*")))
        input2.delete(0, END)
        input2.insert(0, filename)
    
    def valid(input):
        if input.endswith(".mp3") or input.endswith(".wav") or input.endswith(".ogg"):
            return True
        else:
            return False

    def check():
        # Checking if both files exist and are valid
        foundId = False
        foundSong = path.exists(input2.get())
        IdIsAudio = False
        SongIsAudio = False
        id = False

        if foundSong:
            if valid(input2.get()):
                SongIsAudio = True

        for file in listdir(path.abspath(getenv("LOCALAPPDATA") + "\GeometryDash")):
            if path.splitext(file)[0] == input1.get():
                foundId = True

                if valid(file):
                    id = path.join(path.abspath(getenv("LOCALAPPDATA") + "\GeometryDash"), file)
                    IdIsAudio = True
        
        if IdIsAudio and SongIsAudio:
            if foundId and foundSong:
                return id
            else:
                if not foundId and not foundSong:
                    showerror(title = "An error occured :[", message = "Unable to find both songs")
                elif not foundId and foundSong:
                    showerror(title = "An error occured :[", message = "Unable to find Newgrounds song")
                else:
                    showerror(title = "An error occured :[", message = "Unable to find custom song")
        else:
            if not IdIsAudio and not SongIsAudio:
                showerror(title = "An error occured :[", message = "Invalid file types")
            elif not IdIsAudio and SongIsAudio:
                showerror(title = "An error occured :[", message = "Invalid Newgrounds song file type")
            else:
                showerror(title = "An error occured :[", message = "Invalid custom song file type")
        
        return False
    
    def replace():
        if check():
            id = check()
            song = input2.get()
            idDir, idTag = path.splitext(id)
            rename(id, idDir + "_old" + idTag)
            rename(song, id)

    # Creating the GUI
    text1 = Label(root, text = "Newgrounds Song Id", width = 20)
    text2 = Label(root, text = "Custom Song File Location")

    input1 = Entry(root)
    input2 = Entry(root)
    
    input2Button = Button(root, text = "Open File", command = select_file, width = 10)
    button1 = Button(root, text = "Replace", command = replace)

    # Positioning the UI
    text1.grid(row = 0)
    text2.grid(row = 1)
    input1.grid(row = 0, column = 1)
    input2.grid(row = 1, column = 1)
    input2Button.grid(row = 2, column = 1)
    button1.grid(row = 2)

    root.mainloop()
    return None

main()