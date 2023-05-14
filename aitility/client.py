from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.markdown import Markdown
from rich.prompt import Prompt
from . import you

console = Console()

# Look for prompt_presets.ini
from configparser import ConfigParser
import os.path

dir_path = os.path.dirname(os.path.realpath(__file__))
presets_filepath = dir_path + "/prompt_presets.ini"

# check if the config file exists
prompt_presets_exists = os.path.exists(presets_filepath)
prompt_presets = None

if not prompt_presets_exists:
    print(
        "[WARNING!] Presets not found on path: ",
        presets_filepath,
        " \n AITility won't use prompt presets.",
    )
else:
    prompt_presets = ConfigParser()
    prompt_presets.read(presets_filepath)


def get_prompt_preset(name: str, verbose: bool):
    if not prompt_presets_exists:
        return ""

    container = "normal"
    if verbose:
        container = "verbose"

    return prompt_presets[container][name]


def md_to_text(md):
    html = markdown(md)
    soup = BeautifulSoup(html, features="html.parser")
    return soup.get_text()


def display_message(sender, message, is_bot=False):
    formatted_message = Markdown("**" + sender + "**" + ":\n" + message)
    panel = Panel(formatted_message, border_style="yellow")
    console.print(panel)


def ask_user():
    prompt = Prompt.ask("[bold yellow]You[/bold yellow]")
    return prompt


def request(prompt: str, chat: list = None) -> str:
    with console.status(
        "[bold yellow]Generating an answer...", spinner="material"
    ) as status:
        response = you.Completion.create(
            prompt=prompt,
            detailed=True,
            include_links=False,
            chat=chat,
        )
    return response.text
