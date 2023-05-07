import os
from tkinter import Tk, Button, Label, filedialog, Scale, HORIZONTAL
from moviepy.editor import VideoFileClip

def convert_to_gif(video_path, output_folder, quality, frame_rate):
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_path = os.path.join(output_folder, f"{video_name}.gif")
    
    clip = VideoFileClip(video_path)
    clip.write_gif(output_path, fps=frame_rate, quality=quality)
    clip.close()

def select_folder():
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    root.destroy()
    return folder_path

def convert_videos_to_gifs(input_folder, output_folder, quality, frame_rate):
    for file_name in os.listdir(input_folder):
        if file_name.endswith(('.mp4', '.avi', '.mov')):
            video_path = os.path.join(input_folder, file_name)
            convert_to_gif(video_path, output_folder, quality, frame_rate)
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
    
    root = Tk()
    root.title("GIF Converter")
    
    quality_label = Label(root, text="Quality")
    quality_label.pack()
    
    quality_scale = Scale(root, from_=1, to=10, orient=HORIZONTAL)
    quality_scale.pack()
    
    frame_rate_label = Label(root, text="Frame Rate")
    frame_rate_label.pack()
    
    frame_rate_scale = Scale(root, from_=1, to=30, orient=HORIZONTAL)
    frame_rate_scale.pack()
    
    def convert_videos():
        quality = quality_scale.get()
        frame_rate = frame_rate_scale.get()
        root.destroy()
        convert_videos_to_gifs(input_folder, output_folder, quality, frame_rate)
        print("Conversion completed.")
    
    convert_button = Button(root, text="Convert", command=convert_videos)
    convert_button.pack()
    
    root.mainloop()

if __name__ == '__main__':
    main()
