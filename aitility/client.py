from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.prompt import Prompt

from xdg.BaseDirectory import xdg_config_home
import yaml
import os
from os.path import exists

from . import you

console = Console()


def read_config() -> dict:
    # find a filepath
    filepath = os.path.join(xdg_config_home, "aitility", "config.yaml")

    print(exists(filepath))
    if not exists(filepath):
        print("[INFO] No *local* config found at " + filepath)
        # print("[INFO] Type 'aitility --config-warning=off' to stop receiving this message") # TODO: Actually write this
        # THIS DOESNT WORK IF ITS NOT INSTALLED TO ROOT - THIS IS WHATS GOTTA BE FIXED.
        filepath = os.path.join(os.path.dirname(__file__), "config.yaml")

    # Otherwise return config
    with open(filepath, "r") as f:
        config = yaml.safe_load(f)

    return config


def get_prompt_preset(name: str, verbose: bool) -> str:
    config = read_config()
    prompt_presets = config["prompt_presets"]

    prompt_type = "normal"
    if verbose:
        prompt_type = "verbose"

    return prompt_presets[name][prompt_type]


def display_message(sender, message) -> None:
    formatted_message = Markdown("**" + sender + "**" + ":\n" + message)
    panel = Panel(formatted_message, border_style="yellow")
    console.print(panel)


def ask_user() -> str:
    prompt = Prompt.ask("[bold yellow]You[/bold yellow]")
    return prompt


def request(prompt: str, chat: list | None = None) -> str:
    with console.status("[bold yellow]Generating an answer...", spinner="material"):
        response = you.Completion.create(
            prompt=prompt,
            detailed=True,
            include_links=False,
            chat=chat,
        )
    return response.text
