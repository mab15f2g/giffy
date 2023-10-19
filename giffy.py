import os
import subprocess
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar  # Import Progressbar from ttk

def komprimiere_video(datei_pfad, ziel_datei_pfad):
    print(f"Generiere GIF aus {datei_pfad}...")  # Display progress
    ziel_datei_pfad_gif = os.path.splitext(ziel_datei_pfad)[0] + '.gif'
    kommando = ['ffmpeg', '-i', datei_pfad, '-vf', 'scale=640:-1:flags=lanczos,fps=20', ziel_datei_pfad_gif]
    subprocess.run(kommando, capture_output=True, text=True)

def komprimiere_ordnerstruktur(quellpfad, zielpfad):
    for ordnername, unterordner, dateien in os.walk(quellpfad):
        # Erzeuge den Zielordner, wenn er nicht vorhanden ist
        zielordner = os.path.join(zielpfad, os.path.relpath(ordnername, quellpfad))
        if not os.path.exists(zielordner):
            os.makedirs(zielordner)

        # Komprimiere und kopiere jede Videodatei in den Zielordner
        for index, datei in enumerate(dateien, start=1):
            datei_pfad = os.path.join(ordnername, datei)
            ziel_datei_pfad = os.path.join(zielordner, datei)
            
            if os.path.exists(ziel_datei_pfad):
                print(f"Die Zieldatei {ziel_datei_pfad} existiert bereits. Überspringe das Komprimieren.")
            else:
                if datei.endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm')):  # Nur Dateien mit diesen Endungen komprimieren
                    komprimiere_video(datei_pfad, ziel_datei_pfad)
                else:
                    # Kopiere andere Dateien einfach in den Zielordner
                    shutil.copy2(datei_pfad, ziel_datei_pfad)
            
            # Fortschritt anzeigen
            prozent = int(index / len(dateien) * 100)  # Berechne den Fortschritt in Prozent
            print(f"Fortschritt des Ordners: {prozent}%")  # Zeige den Fortschritt in der Konsole an
            update_progress(prozent)

def choose_source_directory():
    source_dir = filedialog.askdirectory()
    source_dir_entry.delete(0, tk.END)
    source_dir_entry.insert(0, source_dir)

def choose_destination_directory():
    dest_dir = filedialog.askdirectory()
    dest_dir_entry.delete(0, tk.END)
    dest_dir_entry.insert(0, dest_dir)

# Function to update the progress bar
def update_progress(progress_value):
    progress_bar["value"] = progress_value
    app.update_idletasks()

def compress_button_click():
    source_dir = source_dir_entry.get()
    dest_dir = dest_dir_entry.get()
    komprimiere_ordnerstruktur(source_dir, dest_dir)

# Create the main application window
app = tk.Tk()
app.geometry("500x400")  # Adjusted height to accommodate the progress bar
app.title("Video Kompressionswerkzeug")

# Add source directory entry and button
source_label = tk.Label(app, text="Quellverzeichnis:")  # Source Directory in German
source_label.pack()
source_dir_entry = tk.Entry(app)
source_dir_entry.pack()
source_dir_button = tk.Button(app, text="Quellverzeichnis auswählen", command=choose_source_directory)  # Choose Source Directory in German
source_dir_button.pack()

# Add destination directory entry and button
dest_label = tk.Label(app, text="Zielverzeichnis:")  # Destination Directory in German
dest_label.pack()
dest_dir_entry = tk.Entry(app)
dest_dir_entry.pack()
dest_dir_button = tk.Button(app, text="Zielverzeichnis auswählen", command=choose_destination_directory)  # Choose Destination Directory in German
dest_dir_button.pack()

# Add compress button
compress_button = tk.Button(app, text="Videos komprimieren", command=compress_button_click)  # Compress Videos in German
compress_button.pack()

# Add a Progressbar
progress_bar = Progressbar(app, length=300, mode="determinate")
progress_bar.pack()

# Start the GUI application
app.mainloop()
