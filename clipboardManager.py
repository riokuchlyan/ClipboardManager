import subprocess
import tkinter as tk

items=[]

def writeToClipboard():
    clipboardNumber=clipboardNumberVar.get()
    try:
        if int(clipboardNumber)>len(items):
            return
        else:
            subprocess.run("pbcopy", text=True, input=str(items[int(clipboardNumber)-1]))
    except:
        return

def tkWindow():
    labeledLastClipboardItem=str(len(items)) + ": " + str(items[-1])
    T.insert(tk.END, labeledLastClipboardItem)
    T.insert(tk.END, "\n")
    T.insert(tk.END, "\n")
    window.update()

def getClipboardData():
    p = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    data = str(p.stdout.read())
    return data[2:-1]

def writeToList():
    if len(items)!=0:
        for i in range (len(items)):
            if str(getClipboardData())==items[i]:
                return
    items.append(str(getClipboardData()))
    return

def job():
    length=len(items)
    getClipboardData()
    writeToList()
    if len(items)>length:
        tkWindow()
    length=len(items)
    window.after(2000, job)

window=tk.Tk()
T = tk.Text(window, height = 7, width = 250)
T.pack()
window.title("Clipboard Manager")
window.geometry("200x200")
clipboardNumberVar=tk.StringVar()
entryLabel=tk.Label(window, text="Enter item number to copy.")
entryInput=tk.Entry(window, textvariable=clipboardNumberVar)
button=tk.Button(window, text="Copy", command=writeToClipboard)
entryLabel.pack(padx=2, pady=1)
entryInput.pack(padx=2, pady=1)
button.pack(padx=2, pady=1)
window.update()

window.after(2000, job)

while True:
    window.update()