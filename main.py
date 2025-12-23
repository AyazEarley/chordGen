import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import chordGen


def generate_chords():
    global chords
    length = dropdown_var.get()
    lengthTable = { "Short" : 4,
                   "Medium" : 6,
                   "Long" : 8,
    }
    numChords = lengthTable[length]
    chords = chordGen.genChords(numChords)
    
    text_box.config(state=tk.NORMAL)
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, chords)
    text_box.config(state=tk.DISABLED)

def play_chords():
    chordGen.playChords(chords)

def export_to_midi():
    global chords
    if not chords:
        messagebox.showwarning("Warning", "Generate chords first!")
        return
    
    file_path = filedialog.asksaveasfilename(
        defaultextension=".mid",
        filetypes=[("MIDI files", "*.mid")],
        title="Save MIDI file"
    )
    
    if file_path:
        try:
            chordGen.writeMIDI(file_path, chords) 
            messagebox.showinfo("MIDI", f"Exported chords to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export MIDI:\n{e}")


root = tk.Tk()
root.title("Major Chord Generator")
root.geometry("500x150")

top_frame = tk.Frame(root)
top_frame.pack(pady=10)

length_label = tk.Label(top_frame, text="Length:")
length_label.pack(side=tk.LEFT, padx=5)

dropdown_var = tk.StringVar()
dropdown_options = ["Short", "Medium", "Long"]
dropdown_menu = ttk.Combobox(top_frame, textvariable=dropdown_var, values=dropdown_options, width=5)
dropdown_menu.current(0)
dropdown_menu.pack(side=tk.LEFT, padx=5)

generate_button = tk.Button(top_frame, text="Generate", command=generate_chords)
generate_button.pack(side=tk.LEFT, padx=10)

text_box = scrolledtext.ScrolledText(root, width=50, height=2, state=tk.DISABLED)
text_box.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

play_button = tk.Button(button_frame, text="Play", command=play_chords)
play_button.pack(side=tk.LEFT, padx=10)

midi_button = tk.Button(button_frame, text="To MIDI", command=export_to_midi)
midi_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
