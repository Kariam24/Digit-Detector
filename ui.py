#Interface for Digit Detector using Convolutional Neural Network
#Project developed by Sebastian Barrera, Izze Lino, Kariam Rodriguez, and Yanni Pierre
#Made for Intro to Artificial Intelligence -- CAP 4630-001
#Due by 11/30/25

from tensorflow import keras
import numpy as np
import tkinter as tk
from PIL import Image, ImageDraw

#Load CNN model
cnn_model = keras.models.load_model('cnn_digit_detector.keras')
print('CNN Model loaded successfully!')

#Create window
root = tk.Tk()
root.title('Digit Detector')
root.geometry('980x560') #Width x Height

#Set the variables for the canvas
canvas_width, canvas_height = 560, 560
line_color = "#fffab0"
bg_color = "#38054F"

#Create canvas
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg=bg_color)
canvas.place(x=0,y=0)

#Create an image that mirrors what is drawn on the canvas
image = Image.new('L', (canvas_width, canvas_height), 0)
draw = ImageDraw.Draw(image)

#Set the default values for line width and radius
line_width, radius = 10, 5

#Set the edges of the canvas to limit drawing range
top_edge, bottom_edge, left_edge, right_edge = 0, canvas_width, 0, canvas_height

#Set coordinate values
last_x, last_y = None, None

#Function for when drawing is starting
def start_draw(event):
    global last_x, last_y
    last_x, last_y = event.x, event.y

#Function for when lines are being drawn
def draw_line(event):
    global last_x, last_y
    #Check to see that drawing has begun
    if last_x is not None and last_y is not None:
        #Ensure that lines outside of the edges are not accepted
        if left_edge <= event.x <= right_edge and top_edge <= event.y <= bottom_edge:
            #Draw line and update coordinates
            canvas.create_line(last_x, last_y, event.x, event.y, width=line_width, fill=line_color, capstyle=tk.ROUND)
            draw.line([last_x, last_y, event.x, event.y], fill='white', width=line_width)
            draw.ellipse([last_x-radius, last_y-radius, last_x+radius, last_y+radius], fill='white')
            draw.ellipse([event.x-radius, event.y-radius, event.x+radius, event.y+radius], fill='white')
            last_x, last_y = event.x, event.y
        else:
            last_x, last_y = None, None

#Function for stopping the drawing of lines
def stop_draw(event):
    global last_x, last_y
    last_x, last_y = None, None

canvas.bind('<Button-1>', start_draw) #Drawing starts when left mouse button is pressed
canvas.bind('<B1-Motion>', draw_line) #Drawing continues while the left mouse button is being pressed and the mouse is moving
canvas.bind('<ButtonRelease-1>', stop_draw) #Drawing ends when the left mouse button is released

#Function for clearing all drawings
def clear_canvas():
    canvas.delete('all')

    global image, draw
    image = Image.new('L', (canvas_width, canvas_height), 0)
    draw = ImageDraw.Draw(image)

    output_label.config(text='. . .')

#Function for saving drawing as a png file
def save_image():
    image.save('img.png')

#Function for opening saved image, formatting it, and then outputting the predicted digit
def predict_digit():
    save_image()
    image = Image.open('img.png')
    image_resized = image.resize((28, 28), Image.Resampling.LANCZOS)
    image_array = np.array(image_resized) / 255.0
    image_array = image_array.reshape(1, 28, 28)
    cnn_prediction = cnn_model.predict(image_array)
    cnn_predicted_digit = np.argmax(cnn_prediction)
    cnn_confidence = max(cnn_prediction[0]) * 100.0
    output_label.config(text=f"CNN is {cnn_confidence:.1f}% certain it's '{int(cnn_predicted_digit)}'")

#Function for updating the line width and radius variable
def change_line_width(value):
    global line_width, radius
    line_width = int(float(value))
    radius = line_width / 2

#Set the font type and font colors
font_name = 'Comic Sans MS'
clear_color, done_color = "#2d43af", "#229f20"

#Set up buttons and scales
clear_button = tk.Button(root,
                         text='Clear', bg=clear_color, fg='white', font=(font_name, 18, 'bold'),
                         command=clear_canvas)
done_button = tk.Button(root,
                        text='Done', bg=done_color, fg='white', font=(font_name, 18, 'bold'),
                        command=predict_digit)
output_label = tk.Label(root,
                        text='. . .', fg=bg_color, font=(font_name, 16))
line_width_scale = tk.Scale(root,
                            from_=10, to_=100, orient=tk.HORIZONTAL, resolution=2,
                            fg=bg_color, font=(font_name, 12),
                            command=change_line_width)

#Organize the placement of all the interactive features
clear_button.place(x=620, y=130, width=300, height=60)
done_button.place (x=620, y=210, width=300, height=60)
line_width_scale.place(x=620, y=290, width=300, height=60)
output_label.place(x=620, y=360, width=300, height=60)

root.mainloop()