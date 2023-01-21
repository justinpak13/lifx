from textual.app import App, ComposeResult
from textual.widgets import Static, Checkbox, Header, Footer, Input, Button
from textual.containers import Horizontal, Container, Vertical

class LayoutExample(App):
    CSS_PATH = "layout.css"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Static("Current Color", classes="box", id = "current_color")
        
        self.pallete = [Static("", classes="swatch") for _ in range(13)]
        yield Container(
            Horizontal(
                *self.pallete,
                id="colors"
            ), 
        classes="box") 

        yield Container(
            Vertical(
                Static("Hue"),
                Horizontal(
                    Input(classes="input"),
                    Button("Increase", classes="button"),
                    Button("Decrease",classes="button"),
                ),
                Static("\nSaturation"),
                Horizontal(
                    Input(classes="input"),
                    Button("Increase", classes="button"),
                    Button("Decrease",classes="button"),
                ),
                Static("\nBrightness"),
                Horizontal(
                    Input(classes="input"),
                    Button("Increase", classes="button"),
                    Button("Decrease",classes="button"),
                ),
            ), classes="box", id="inputs"
        )

        yield Checkbox(classes="container", id="switch")

    def on_mount(self) -> None: 
        DEGREE_INTERVAL = 30
        for index, widget in enumerate(self.pallete):
            degrees = index * DEGREE_INTERVAL
            widget.update(f"{degrees}") 
            widget.styles.background = f"hsl({degrees},42.9%,49.4%)"


if __name__ == "__main__":
    app = LayoutExample()
    app.run()