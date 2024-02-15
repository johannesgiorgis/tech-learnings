import gradio as gr
import numpy as np

# Demo 1 - Single Input


def greet1(name):
    return "Hello " + name + "!"


demo1 = gr.Interface(fn=greet1, inputs="text", outputs="text")

# demo1.launch()

# Demo 2 - Multiple Inputs


def greet2(name, is_morning, temperature):
    salutation = "Good morning" if is_morning else "Good evening"
    greeting = f"{salutation} {name}! It is {temperature} degrees outside."
    celsius = (temperature - 32) * 5 / 9
    return greeting, round(celsius, 2)


demo2 = gr.Interface(
    fn=greet2,
    inputs=["text", "checkbox", gr.Slider(0, 100)],
    outputs=["text", "number"],
)

# demo2.launch()

# Demo 3 - Images


def sepia(input_img):
    sepia_filter = np.array(
        [[0.393, 0.769, 0.189], [0.349, 0.686, 0.168], [0.272, 0.534, 0.131]]
    )
    sepia_img = input_img.dot(sepia_filter.T)
    sepia_img /= sepia_img.max()  # Normalize values to be in the range [0, 1]
    print(input_img.shape, sepia_img.shape)
    return sepia_img


demo3 = gr.Interface(fn=sepia, inputs=gr.Image(), outputs="image")


# demo3.launch()
