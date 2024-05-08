from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

# Converting png to ico to use as icon
from PIL import Image
filename = "YTvidDownloader.png"
img = Image.open(filename)
img.save('logoforYTD.ico')

folder_name = ""

# file location

def openLocation():
    global folder_name
    folder_name = filedialog.askdirectory()
    
    if (len(folder_name) > 1):
        locationError.config(text=folder_name, fg="green")
        if (len(folder_name) > 30):
            bigger_frame = round(400 + len(folder_name)**1.3)
            root.geometry(f"{bigger_frame}x400")
            
    else:
        locationError.config(text="Please choose a proper folder.", fg="red")
    
# Downloading the video
def DownloadVideo():
    try:
        choice = ytdChoices.get()
        url = ytdEntry.get()
        
        if (len(url) > 1):
            ytdError.config(text="Valid", fg='green')
            yt = YouTube(url)

            if (choice == choices[0]):
                select = yt.streams.filter(progressive=True).first()

            elif (choice == choices[1]):
                select = yt.streams.filter(progressive=True, file_extension='mp4').last()

            elif (choice == choices[2]):
                select = yt.streams.filter(only_audio=True).first()
    except:        
        ytdError.config(text="Invalid", fg='red')
    
    # Download function
    select.download(folder_name)
    ytdError.config(text="Downloaded!", fg='green', font=('jost', 30, 'bold'))
    ytdError.grid(row = 12)
    
# Fonts
ft = ('jost', 15)
fter = ('jost', 10)
ftb = ('jost', 15, 'bold')

root = Tk()
root.title("YouTube Downloader")
root.geometry("350x400") # Sets the size of the window
root.columnconfigure(0, weight=1) # Centers the content
ytdLogo = root.iconbitmap(bitmap="logoforYTD.ico")

ytdLabel = Label(root, text="Enter the URL", font=ftb)
ytdLabel.grid()

# Entry box
ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=50, textvariable = ytdEntryVar)
ytdEntry.grid()

# In case of an error
ytdError = Label(root, text="", fg='red', font=fter)
ytdError.grid()

# Asking save file label
saveLabel = Label(root, text= "Save the video", font=ftb)
saveLabel.grid()

# Button for the path to save at
saveEntry = Button(root, text="Choose Path",width=10, bg="red", fg="white", command=openLocation)
saveEntry.grid()

# Path finding error # In case of an error
locationError = Label(root, text="", fg='red', font=fter)
locationError.grid()

# Download Quality
ytdQuality = Label(root, text="Select Quality", font=ftb)
ytdQuality.grid()

# Choices for quality
choices = ["720p","144p", "Audio Only"]
ytdChoices = ttk.Combobox(root, values=choices)
ytdChoices.grid()

# Download Button. Obviously
downloadBTN = Button(root, text="Download",width=10, bg="red", fg="white", command=DownloadVideo)
downloadBTN.grid(row = 15)

root.resizable(False, False)
root.mainloop()