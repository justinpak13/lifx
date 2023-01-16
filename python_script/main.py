from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Checkbox, Button, Input
from textual.containers import Horizontal, Vertical
from packet import Packet

class LifxApp(App):
    """A Textual app to manage lifx lights."""

    BINDINGS = [("o", "turn_on", "Turn on lifx lights"),
                ("p", "turn_off", "Turn off lifx lights")]


    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        self.color_widget  = Static("This is a test of colors")
        yield self.color_widget
        
        yield Vertical(
            Static("Test of the hue"), Input(placeholder="Test placeholder", classes = "container")
        )

        
        for i in range(0, 361, 12):
            stripe = Button(f"{str(i)}")
            stripe.styles.background = f"hsl({str(i)},50%,30%)"
            stripe.styles.padding=0
            yield stripe 

        self.saturation_widget   = Static("This is a test of saturation")
        yield self.saturation_widget 
        self.brightness_widget   = Static("This is a test of brightness")
        yield self.brightness_widget 



        focused_checkbox = Checkbox()
        focused_checkbox.focus()
        yield Horizontal(
            Static("focused: ", classes="label"), focused_checkbox, classes="container"
        )

    def on_mount(self) -> None:
        # Color widget styes 
        self.color_widget.styles.background = "hsl(150,0%,0%)"
        self.color_widget.styles.width = "100%"
        self.color_widget.styles.height = "20%"
        self.color_widget.styles.padding = 1
        self.color_widget.styles.margin = 1


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