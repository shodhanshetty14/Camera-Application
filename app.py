from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import Font
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

img_count = 1
video_count = 1


def notification(name):
    noti = messagebox.showwarning("Image Captured!!", "Captured and saved as {}".format(name))
    # noti.after(2000, noti.destroy)  



def video_capture():
    global video_count
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 700)
    capture.set(cv2.CAP_PROP_FPS, 30)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    name = f"video-{video_count}.avi"
    out = cv2.VideoWriter(name, fourcc, 20.0, (640, 480))
    while True:
        
        ret, frame = capture.read()
        out.write(frame)
        
        cv2.imshow('Recording....', frame)
        
        if (cv2.waitKey(30) == 27):
            capture.release()
            out.release()
            cv2.destroyAllWindows()
            notification(name)
            video_count += 1
            break



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
    global img_count
    name = f"capture-{img_count}.png"
    cv2.imwrite(name, frame)
    notification(name)
    img_count +=1

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
    
    video_btn = Button(root, text="Open Video recoder", command=video_capture)
    video_btn.pack()
    
    root.mainloop()