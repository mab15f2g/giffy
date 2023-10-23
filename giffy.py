import os
import subprocess
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Progressbar  # Import Progressbar from ttk


def gif_erstellen(datei_pfad, ziel_datei_pfad):
    """ Function to compress a video file to a gif
        :param datei_pfad: Pfad zur Videodatei
        :param ziel_datei_pfad: Pfad zur Zieldatei
    """    
    print(f"Generiere GIF aus {datei_pfad}...")  # Display progress
    ziel_datei_pfad_gif = os.path.splitext(ziel_datei_pfad)[0] + '.gif'
    gif_filter = 'scale=640:-1:flags=lanczos,fps=20'
    kommando = ['ffmpeg', '-i', datei_pfad, '-vf', gif_filter, ziel_datei_pfad_gif]
    subprocess.run(kommando, capture_output=True, text=True)


def all_videos_to_gif(quellpfad, zielpfad):
    """"Function to compress all videos in a directory"""
    for ordnername, unterordner, dateien in os.walk(quellpfad):
        # Erzeuge den Zielordner, wenn er nicht vorhanden ist
        zielordner = os.path.join(zielpfad, os.path.relpath(ordnername, quellpfad))
        if not os.path.exists(zielordner):
            os.makedirs(zielordner)

        # Komprimiere und kopiere jede Videodatei in den Zielordner
        for index, datei in enumerate(dateien, start=1):
            datei_pfad = os.path.join(ordnername, datei)
            ziel_datei_pfad = os.path.join(zielordner, datei)
            print(ziel_datei_pfad)
            if os.path.exists(os.path.join(ordnername, datei)):
                print(f"Die Zieldatei {ziel_datei_pfad} existiert bereits. Überspringe das Komprimieren.")
            else:
                if datei.endswith(('.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm')):
                    gif_erstellen(datei_pfad, ziel_datei_pfad)
                else:
                    # Kopiere andere Dateien einfach in den Zielordner
                    shutil.copy2(datei_pfad, ziel_datei_pfad)
            
            # Fortschritt anzeigen
            prozent = int(index / len(dateien) * 100)  # Berechne den Fortschritt in Prozent
            print(f"Fortschritt des Ordners: {prozent}%")  # Zeige den Fortschritt in der Konsole an
            update_progress(prozent)

def choose_source_directory():
    """Function to choose the source directory"""
    source_dir = filedialog.askdirectory()
    source_dir_entry.delete(0, tk.END)
    source_dir_entry.insert(0, source_dir)


def choose_destination_directory():
    """Function to choose the destination directory"""
    dest_dir = filedialog.askdirectory()
    dest_dir_entry.delete(0, tk.END)
    dest_dir_entry.insert(0, dest_dir)

# Function to update the progress bar
def update_progress(progress_value):
    """Function to update the progress bar"""
    progress_bar["value"] = progress_value
    app.update_idletasks()

def compress_button_click():
    """Function to start the compression"""
    source_dir = source_dir_entry.get()
    dest_dir = dest_dir_entry.get()
    all_videos_to_gif(source_dir, dest_dir)

# Create the main application window
app = tk.Tk()
app.geometry("500x400")  # Adjusted height to accommodate the progress bar
app.title("Video Kompressionswerkzeug")

# Add source directory entry and button
source_label = tk.Label(app, text="Quellverzeichnis:")  # Source Directory in German
source_label.pack()
source_dir_entry = tk.Entry(app)
source_dir_entry.pack()
# Choose Source Directory in German
source_dir_button = tk.Button(app, text="Quellverzeichnis auswählen", command=choose_source_directory)
source_dir_button.pack()

# Add destination directory entry and button
dest_label = tk.Label(app, text="Zielverzeichnis:")  # Destination Directory in German
dest_label.pack()
dest_dir_entry = tk.Entry(app)
dest_dir_entry.pack()

# Add a button to choose the destination directory
TEXT_ZIEL = "Zielverzeichnis auswählen"  # Choose Destination Directory in German
dest_dir_button = tk.Button(app, text=TEXT_ZIEL, command=choose_destination_directory)
dest_dir_button.pack()

TEXT_ERSTELLEN = "Gifs erstellen"
# Add compress button
compress_button = tk.Button(app, text=TEXT_ERSTELLEN, command=compress_button_click)
compress_button.pack()

# Add a Progressbar
progress_bar = Progressbar(app, length=300, mode="determinate")
progress_bar.pack()

# Start the GUI application
app.mainloop()
