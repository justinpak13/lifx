from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from packet import Packet

class LifxApp(App):
    """A Textual app to manage lifx lights."""

    BINDINGS = [("o", "turn_on", "Turn on lifx lights"),
                ("p", "turn_off", "Turn off lifx lights")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

    def action_turn_on(self) -> None:
        """An action to turn on the light."""
        x = Packet()
        x.on()

    def action_turn_off(self) -> None:
        "An action to turn off the light"
        x = Packet()
        x.off()

if __name__ == "__main__":
    app = LifxApp()
    app.run()