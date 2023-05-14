from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from markdown import markdown
from bs4 import BeautifulSoup
from time import sleep

console = Console()
status = console.status(status="green", spinner="dots")


def md_to_text(md):
    html = markdown(md)
    soup = BeautifulSoup(html, features="html.parser")
    return soup.get_text()


def display_message(sender, message, is_bot=False):
    formatted_message = Text(sender + ": " + md_to_text(message), style="yellow")
    panel = Panel(formatted_message, border_style="white")
    console.print(panel)


tasks = [f"task {n}" for n in range(1, 11)]
# Example usage
display_message("User", "Hello, how are you?")
with console.status("[bold green]Working on tasks...") as status:
    sleep(3)

display_message("Bot", "I'm doing **great**! How about you?", is_bot=True)
