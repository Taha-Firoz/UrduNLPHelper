from transliteration import get_browser_context, transliterate
import os.path
from os import path
import tkinter as tk
import recorder
import csv
# --- functions ---
rec = recorder.Recorder(channels=2)
output_folder = "recorded_audio"
running = None
current = 1
checkpoint_file = 'checkpoint.txt'

def start_recording():
    global running
    global current_row
    global var
    global recording_var
    global current
    global start

    if running is not None:
        var.set("Not Recording: Currently viewing phrase #{}".format(start+current))
        running.stop_recording()
        running.close()
        running = None
        with open(checkpoint_file, 'w') as checkpointFile:
            checkpointFile.write(str(start + current))
        
        recording_var.set('Redo')
    else:
        var.set("Recording: {}".format(current_row[0]))
        recorded_file_name = path.join(output_folder,"{}.wav".format(current_row[0]))
        running = rec.open(recorded_file_name, 'wb')
        running.start_recording()
        recording_var.set('Stop')

def next_sent():
    global text_widget
    global current_row
    global csv_reader
    global current
    global recording_var
    global root
    global start
    global var
    global text_widget
    global hidden
    
    current_row = next(csv_reader, None)
    if current_row is None:
        root.destroy()
    else:
        if not(hidden):
            trans_widget.config(state=tk.NORMAL)
            trans_widget.delete(1.0, tk.END)
            trans_widget.update()
            trans_widget.pack_forget()
            hidden = True
        text_widget.config(state=tk.NORMAL)
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, current_row[1])
        text_widget.config(state=tk.DISABLED)
        current+=1
        recording_var.set('Start')
        var.set("Not Recording: Currently viewing phrase #{}".format(start+current))

def goToMain():
    global splash
    global root
    global input_start
    global input_stop
    global start
    global end
    global warning_text
    global csv_file
    global csv_reader
    global current_row
    global text_widget
    global checkpoint_file 
    global var
    global current
    if input_start.get().isdigit() and input_stop.get().isdigit(): 
        start = int(input_start.get())
        end = int(input_stop.get())
        #remove the other window entirely
        splash.destroy()
        #make root visible again
        root.iconify()
        root.deiconify()
        checkpoint_file = "{}_{}-checkpoint.txt".format(start,end)
        if path.exists(checkpoint_file):
            with open(checkpoint_file, 'r') as checkpointFile:
                start = int(checkpointFile.read())
        if not(path.exists(output_folder)):
            os.mkdir(output_folder)
        
        csv_file = open("transcription.csv", encoding="utf8")
        csv_reader = csv.reader(islice(csv_file, start - 1, end), delimiter=",")
        current_row = next(csv_reader)
        var.set("Not Recording: Currently viewing phrase #{}".format(start+current))
        text_widget.insert(tk.END, current_row[1])
        text_widget.config(state=tk.DISABLED)

    else:
        warning_text.set("Invalid input: You need to enter numbers")

def on_closing():
    global root
    global splash
    splash.destroy()
    root.destroy()

def on_transliterate():
    global browser_context
    global trans_var
    global current_row
    global trans_widget
    global hidden

    trans_var.set("Loading...")
    if browser_context is None :
        browser_context = get_browser_context()

    try:
        transliteration = transliterate(browser_context, current_row[1])
        trans_var.set("To Roman Urdu")
        trans_widget.pack()
        trans_widget.delete(1.0, tk.END)
        trans_widget.insert(tk.END, "{}".format(transliteration))
        hidden = False
    except:
        trans_var.set("Error Loading")
        browser_context = get_browser_context()



# --- main ---
from itertools import islice
browser_context = get_browser_context()

start = None
end = None
current_row = None
csv_reader = None
csv_file = None
csv_reader = None
current_row = None


root = tk.Tk()
top = tk.Frame(root)
bottom = tk.Frame(root)
top.pack(side=tk.TOP)
bottom.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

hidden = True
text_widget = tk.Text(root, height=5, width=50, font=("Helvetica", 32))
text_widget.pack()

trans_widget = tk.Text(root, height=5, width=50, font=("Helvetica", 32))
trans_widget.pack()
trans_widget.pack_forget()

trans_var = tk.StringVar()
trans_var.set("To Roman Urdu")
button_trans = tk.Button(root, textvariable=trans_var, command=on_transliterate, height = 2, width = 15)
button_trans.pack(in_=bottom, side=tk.RIGHT)

recording_var = tk.StringVar()
recording_var.set("Start")
button_rec = tk.Button(root, textvariable=recording_var, command=start_recording, height = 2, width = 8)
button_rec.pack(in_=bottom, side=tk.LEFT, padx = (10,10))

var = tk.StringVar()
label = tk.Label( root, textvariable=var )

var.set("Not Recording")
label.pack(in_=bottom, side=tk.LEFT, padx = (20, 0))

button_next = tk.Button(root, text='Next', command=next_sent, height = 2, width = 8)
button_next.pack(in_=bottom, side=tk.LEFT, padx = (30, 0))
root.bind('s',lambda event: start_recording())
root.bind('n',lambda event: next_sent())
root.bind('d',lambda event: next_sent())

root.withdraw()

splash = tk.Toplevel(root)

warning_text = tk.StringVar()
warning_label = tk.Label(splash, textvariable = warning_text)
warning_label.grid(column = 0, row = 0)

start_label = tk.Label(splash, text = "Enter Your Start Row")
start_label.grid(column = 0, row = 1)
 
input_start = tk.StringVar()
input_start_widget = tk.Entry(splash, width = 15, textvariable = input_start)
input_start_widget.grid(column = 1, row = 1)
 
 
stop_label = tk.Label(splash, text = "Enter Your Last Row")
stop_label.grid(column = 0, row = 2)
 
input_stop = tk.StringVar()
input_stop_widget = tk.Entry(splash, width = 15, textvariable = input_stop)
input_stop_widget.grid(column = 1, row = 2)

button = tk.Button(splash, text = "Continue", command = goToMain)
button.grid(column= 0, row = 4)

splash.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop() 