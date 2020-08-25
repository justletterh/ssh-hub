from prompt_toolkit.application import Application
from prompt_toolkit.application.current import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.key_binding.bindings.focus import focus_next, focus_previous
from prompt_toolkit.layout import HSplit, Layout, VSplit
from prompt_toolkit.styles import Style
from prompt_toolkit.widgets import Box, Button, Frame, Label, TextArea
import subprocess, sys
from os import get_terminal_size as get_size

def txt():
    text_area.text="ssh will start\nmomentarily..."
def stop():
    try:
        sys.exit()
    except SystemExit:
        pass
    finally:
        get_app().exit()
def button1_clicked():
    txt()
    subprocess.Popen(['chmod', '+x', './tst'])
    subprocess.Popen(['./tst'])
    stop()
def button2_clicked():
    txt()
def button3_clicked():
    txt()
def exit_clicked():
    stop()

button1 = Button("Host 1", handler=button1_clicked)
button2 = Button("Host 2", handler=button2_clicked)
button3 = Button("Host 3", handler=button3_clicked)
button4 = Button("Exit", handler=exit_clicked)
text_area = TextArea(focusable=True)

root_container = Box(
    HSplit(
        [
            Label(text="Press the up and down arrows to move the focus."),
            VSplit(
                [
                    Box(
                        body=HSplit([button1, button2, button3, button4], padding=1),
                        padding=1,
                        style="class:left-pane",
                    ),
                    Box(body=Frame(text_area), padding=1, style="class:right-pane"),
                ]
            ),
        ]
    ),
)

layout = Layout(container=root_container, focused_element=button1)

kb = KeyBindings()
kb.add("down")(focus_next)
kb.add("up")(focus_previous)

style = Style(
    [
        ("left-pane", "bg:#000000 #00aa00"),
        ("right-pane", "bg:#00aa00 #000000"),
        ("button", "#00aa00"),
        ("button-arrow", "#ffffff"),
        ("button focused", "bg:#00aa00"),
        ("text-area focused", "bg:#ff0000"),
    ]
)

application = Application(layout=layout, key_bindings=kb, style=style, full_screen=True)
def main():
    application.run()
if __name__ == "__main__":
    try:
        main()
    except:
        pass
    finally:
        for i in range(get_size().lines):
            print("")
