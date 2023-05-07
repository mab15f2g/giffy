import os
from tkinter import Tk, Button, Label, filedialog
from moviepy.editor import VideoFileClip

def convert_to_gif(video_path, output_folder, quality):
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_path = os.path.join(output_folder, f"{video_name}.gif")
    
    clip = VideoFileClip(video_path)
    clip.write_gif(output_path, fps=10, quality=quality)
    clip.close()

def select_folder():
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    root.destroy()
    return folder_path

def convert_videos_to_gifs(input_folder, output_folder, quality):
    for file_name in os.listdir(input_folder):
        if file_name.endswith(('.mp4', '.avi', '.mov')):
            video_path = os.path.join(input_folder, file_name)
            convert_to_gif(video_path, output_folder, quality)
            print(f"Converted {file_name} to GIF.")

def main():
    input_folder = select_folder()
    if not input_folder:
        print("No folder selected.")
        return
    
    output_folder = select_folder()
    if not output_folder:
        print("No output folder selected.")
        return
    
    quality = int(input("Enter quality (1-10): "))
    
    convert_videos_to_gifs(input_folder, output_folder, quality)
    print("Conversion completed.")

if __name__ == '__main__':
    main()
