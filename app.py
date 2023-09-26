from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import Font
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk


count = 1


def notification():
    global count
    name = f"capture-{count}.png"
    noti = messagebox.showwarning("Image Captured!!", "Image has been captured and saved as {}".format(name))
    # noti.after(2000, noti.destroy)  


def open_camera():
    result, frame = video.read()
    img_array_color = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2RGBA)
    
    image_captured = Image.fromarray(img_array_color)

    photo_image = ImageTk.PhotoImage(image=image_captured)
    
    
    widget_root.photo_image = photo_image
    widget_root.configure(image=photo_image)
    
    camera_button.configure(text="Capture", command=lambda:capture_image(frame))
    
    root.bind('<space>', lambda e: capture_image(frame))
    
    widget_root.after(10, open_camera)
    
    

def capture_image(frame):
    global count
    name = f"capture-{count}.png"
    cv2.imwrite(name, frame)
    notification()
    count +=1

if __name__ == "__main__":
    
    root = Tk()
    root.title("QR Genenrator")
    root.geometry('700x700')
    
    video = cv2.VideoCapture(0)
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 700)
    video.set(cv2.CAP_PROP_FPS, 30)
    
    root.bind('<Escape>', lambda e: root.quit())
    # root.bind('<space>', lambda e: )    
    widget_root = Label(root)
    widget_root.pack()
    
    # open_camera()
    camera_button = Button(root, text="Open Camera", command=open_camera)
    camera_button.pack()
    
    
    root.mainloop()