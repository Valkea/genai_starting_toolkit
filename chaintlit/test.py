# chainlit run test.py -w  


import chainlit as cl
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from chainlit.input_widget import Select, Switch, Slider


@cl.action_callback("action_button")
async def on_action(action):
    await cl.Message(content=f"Executed {action.name}").send()
    # Optionally remove the action button from the chatbot user interface
    # await action.remove()


    res = await cl.AskActionMessage(
        content="Pick an action!",
        actions=[
            cl.Action(name="continue", value="continue", label="✅ Continue"),
            cl.Action(name="cancel", value="cancel", label="❌ Cancel"),
        ],
    ).send()

    if res and res.get("value") == "continue":
        await cl.Message(
            content="Continue!",
        ).send()


@cl.action_callback("action_button_image")
async def on_action_image(action):
    image = cl.Image(path=action.value, name="image1", display="inline")

    # Attach the image to the message
    await cl.Message(
        # content="This message has an image!",
        content="",
        elements=[image],
    ).send()


@cl.action_callback("action_button_sound")
async def on_action_sound(action):
    elements = [
        cl.Audio(name="example.mp3", path=action.value, display="inline"),
    ]
    await cl.Message(
        # content="Here is an audio file",
        content="",
        elements=elements,
    ).send()


@cl.action_callback("action_button_pyplot")
async def on_action_pyplot(action):
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [1, 4, 2, 3])

    elements = [
        cl.Pyplot(name="plot", figure=fig, display="inline"),
    ]
    await cl.Message(
        # content="Here is a simple plot",
        content="",
        elements=elements,
    ).send()


@cl.action_callback("action_button_plotly")
async def on_action_plotly(action):
    fig = go.Figure(
        data=[go.Bar(y=[2, 1, 3])],
        layout_title_text="An example figure",
    )
    elements = [cl.Plotly(name="chart", figure=fig, display="inline")]
    await cl.Message(
        # content="This message has a chart", 
        content = "",
        elements=elements
    ).send()


@cl.action_callback("action_button_text")
async def on_action_text(action):
    text_content = "Hello, this is a text element."
    elements = [cl.Text(name="simple_text", content=action.value, display="inline")]

    await cl.Message(
        content="Check out this text element!",
        elements=elements,
    ).send()


@cl.on_chat_start
async def start():
    # Sending an action button within a chatbot message
    actions = [
        cl.Action(name="action_button", value="example_value", description="Click it", collapsed=True),
        cl.Action(
            name="action_button_image",
            value="medias/demo_chat.png",
            description="Display Image",
        ),
        cl.Action(
            name="action_button_sound",
            value="medias/test.mp3",
            description="Play sound",
        ),
        cl.Action(name="action_button_pyplot", value="", description="Display Pyplot", collapsed=True),
        cl.Action(name="action_button_plotly", value="", description="Display Plotly"),
        cl.Action(name="action_button_text", value="This is a demo text :) ", description="Display text"),
    ]

    await cl.Message(
        content="Interact with this action button:", actions=actions
    ).send()

    settings = await cl.ChatSettings(
    [
        Select(
            id="Model",
            label="OpenAI - Model",
            values=["gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-4", "gpt-4-32k"],
            initial_index=0,
        ),
        Switch(id="Streaming", label="OpenAI - Stream Tokens", initial=True),
        Slider(
            id="Temperature",
            label="OpenAI - Temperature",
            initial=1,
            min=0,
            max=2,
            step=0.1,
        ),
        Slider(
            id="SAI_Steps",
            label="Stability AI - Steps",
            initial=30,
            min=10,
            max=150,
            step=1,
            description="Amount of inference steps performed on image generation.",
        ),
        Slider(
            id="SAI_Cfg_Scale",
            label="Stability AI - Cfg_Scale",
            initial=7,
            min=1,
            max=35,
            step=0.1,
            description="Influences how strongly your generation is guided to match your prompt.",
        ),
        Slider(
            id="SAI_Width",
            label="Stability AI - Image Width",
            initial=512,
            min=256,
            max=2048,
            step=64,
            tooltip="Measured in pixels",
        ),
        Slider(
            id="SAI_Height",
            label="Stability AI - Image Height",
            initial=512,
            min=256,
            max=2048,
            step=64,
            tooltip="Measured in pixels",
        ),
    ]
    ).send()


@cl.on_settings_update
async def setup_agent(settings):
    print("on_settings_update", settings)
