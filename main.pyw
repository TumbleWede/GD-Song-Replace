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
    root.geometry("300x130")
    root.resizable(False, False)
    root.anchor(CENTER)

    def select_file():
        # Open file prompt
        filename = askopenfilename(title = "Select a Song", filetypes = (("Audio Files", "*.mp3 OR *.wav OR *.ogg"), ("All Files", "*.*")))
        input2.delete(0, END)
        input2.insert(0, filename)
    
    def open_dir():
        startfile(path.abspath(getenv("LOCALAPPDATA") + "\GeometryDash"))
    
    def valid(input):
        if input.endswith(".mp3") or input.endswith(".wav") or input.endswith(".ogg"):
            return True
        else:
            return False

    def check():
        # Checking if both files exist and are valid
        foundId = False
        foundSong = path.exists(input2.get())
        idIsAudio = False
        songIsAudio = False
        incompleteId = False
        incompleteSong = False
        id = False

        if input1.get() == "":
           incompleteId = True

        if input2.get() == "":
            incompleteSong = True

        if foundSong:
            if valid(input2.get()):
                songIsAudio = True

        for file in listdir(path.abspath(getenv("LOCALAPPDATA") + "\GeometryDash")):
            if path.splitext(file)[0] == input1.get():
                foundId = True

                if valid(file):
                    id = path.join(path.abspath(getenv("LOCALAPPDATA") + "\GeometryDash"), file)
                    idIsAudio = True
        
        if idIsAudio and songIsAudio: # Incorrect entry
            if foundId and foundSong:
                return id
            else:
                if not foundId and not foundSong:
                    showerror(title = "An error occured :[", message = "Unable to find both songs")
                elif not foundId and foundSong:
                    showerror(title = "An error occured :[", message = "Unable to find Newgrounds song")
                else:
                    showerror(title = "An error occured :[", message = "Unable to find custom song")
        elif not incompleteId and not incompleteSong: # Invalid file formats
            if not idIsAudio and not songIsAudio:
                showerror(title = "File type error :[", message = "Invalid songs")
            elif not idIsAudio and songIsAudio:
                showerror(title = "File type error :[", message = "Invalid Newgrounds song")
            else:
                showerror(title = "File type error :[", message = "Invalid custom song")
        else: # An entry is blank
            if incompleteId and incompleteSong:
                showerror(title = "Blank entry error :[", message = "Both entries are blank")
            elif incompleteId and not incompleteSong:
                showerror(title = "Blank entry error :[", message = "Newgrounds song id entry is blank")
            else:
                showerror(title = "Blank entry error :[", message = "Custom song entry is blank")
        
        return False
    
    def replace():
        if check():
            id = check()
            song = input2.get()
            idDir, idTag = path.splitext(id)
            
            if toggle.get() == 1: # Keep replaced song
                rename(id, idDir + "_old" + idTag)
            else: # Remove replaced song
                remove(id)
            
            rename(song, id)

    # Creating the GUI
    text1 = Label(root, text = "Newgrounds Song Id", width = 20)
    text2 = Label(root, text = "Custom Song File Location")
    input1 = Entry(root)
    input2 = Entry(root)
    input2Button = Button(root, text = "Open File", command = select_file, width = 10)
    button1 = Button(root, text = "Replace", command = replace)
    button2 = Button(root, text = "Open Song Folder", command = open_dir)
    toggle = IntVar()
    check1 = Checkbutton(root, text = "Keep Replaced Song", variable = toggle)
    
    # Positioning the UI
    text1.grid(row = 0)
    text2.grid(row = 1, pady = 2)
    input1.grid(row = 0, column = 1, pady = 2)
    input2.grid(row = 1, column = 1, pady = 2)
    input2Button.grid(row = 2, column = 1, pady = 2)
    button1.grid(row = 3, pady = 2)
    button2.grid(row = 3, column = 1, pady = 2)
    check1.grid(row = 2, pady = 2)

    root.mainloop()
    return None

main()
