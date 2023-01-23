from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Checkbox, Button, Input
from textual.containers import Horizontal, Vertical, Container
from packet import Packet

class Control(Static):
    def compose(self) -> ComposeResult:
        yield Vertical(
            Input("value", classes="entry"),
            Button("Increase", classes="button"),
            Button("Decrease",classes="button"), classes="controls" )

class LifxApp(App):
    """A Textual app to manage lifx lights."""

    BINDINGS = [("o", "turn_on", "Turn on lifx lights"),
                ("p", "turn_off", "Turn off lifx lights")]


    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("Current Color", classes="box")
        
        self.pallete = [Static("", classes="swatch") for _ in range(13)]
        yield Container(
            Horizontal(
                *self.pallete,
                id="colors"
            ), 
        classes="pallete") 

        yield Container(
            Vertical(
                Vertical(
                    Static("Hue\n", classes="label"),
                    Control(),
                ),
                Vertical(

                    Static("Saturation\n", classes="label"),
                    Control(),
                ),
                Vertical(
                    Static("Brightness\n", classes="label"),
                    Control(),
                )
             ), classes ="inputs")

        yield Checkbox(classes="container", id="switch")

    def on_mount(self) -> None:
        DEGREE_INTERVAL = 30
        for index, widget in enumerate(self.pallete):
            degrees = index * DEGREE_INTERVAL
            widget.update(f"{degrees}") 
            widget.styles.background = f"hsl({degrees},42.9%,49.4%)"


    def action_turn_on(self) -> None:
        """An action to turn on the light."""
        x = Packet()
        x.on()

    def action_turn_off(self) -> None:
        "An action to turn off the light"
        x = Packet()
        x.off()

if __name__ == "__main__":
    app = LifxApp(css_path="lifx.css")
    app.run()