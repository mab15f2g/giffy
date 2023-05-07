import os
import multiprocessing
from tkinter import Tk, Button, Label, filedialog, Scale, HORIZONTAL
from moviepy.editor import VideoFileClip
from concurrent.futures import ThreadPoolExecutor

input_folder = ""
output_folder = ""

def convert_to_gif(video_path, output_folder, quality, frame_rate):
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_path = os.path.join(output_folder, f"{video_name}.gif")
    
    clip = VideoFileClip(video_path)
    clip.write_gif(output_path, fps=frame_rate, opt=quality)
    clip.close()

def select_input_folder():
    global input_folder
    input_folder = filedialog.askdirectory()

def select_output_folder():
    global output_folder
    output_folder = filedialog.askdirectory()

def convert_videos_to_gifs(quality, frame_rate):
    if not input_folder:
        print("No input folder selected.")
        return
    
    if not output_folder:
        print("No output folder selected.")
        return
    
    pool = ThreadPoolExecutor(max_workers=int(multiprocessing.cpu_count() * 0.75))
    
    for file_name in os.listdir(input_folder):
        if file_name.endswith(('.mp4', '.avi', '.mov')):
            video_path = os.path.join(input_folder, file_name)
            pool.submit(convert_to_gif, video_path, output_folder, quality, frame_rate)
            print(f"Converting {file_name} to GIF.")
    
    pool.shutdown(wait=True)
    print("Conversion completed.")

def get_short_path(path):
    short_path = os.path.basename(path)
    if len(short_path) > 20:
        short_path = '...' + short_path[-20:]
    return short_path

def main():
    root = Tk()
    root.title("GIF Converter")
    root.geometry("640x480")
    
    quality_label = Label(root, text="Quality")
    quality_label.pack(anchor="w")
    
    quality_scale = Scale(root, from_=1, to=10, orient=HORIZONTAL)
    quality_scale.pack(fill="x", padx=80)
    
    frame_rate_label = Label(root, text="Frame Rate")
    frame_rate_label.pack(anchor="w")
    
    frame_rate_scale = Scale(root, from_=1, to=30, orient=HORIZONTAL)
    frame_rate_scale.pack(fill="x", padx=80)
    
    convert_button = Button(root, text="Convert", command=lambda: convert_videos_to_gifs(quality_scale.get(), frame_rate_scale.get()))
    convert_button.pack(side="bottom")
    
    input_button = Button(root, text="Select Input Folder", command=select_input_folder)
    input_button.pack(side="left", padx=20, pady=10)
    
    output_button = Button(root, text="Select Output Folder", command=select_output_folder)
    output_button.pack(side="right", padx=20, pady=10)
    
    input_label = Label(root, text=f"Input Folder: {get_short_path(input_folder)}")
    input_label.pack(anchor="w")
    
    output_label = Label(root, text=f"Output Folder: {get_short_path(output_folder)}")
    output_label.pack(anchor="w")
    
    root.mainloop()

if __name__ == '__main__':
    main()
