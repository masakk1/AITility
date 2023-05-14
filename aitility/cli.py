import click
import json
from . import client
from rich.console import Console
from rich import print
from rich.prompt import Prompt

console = Console()


@click.group()
def main():
    pass


@main.command()
@click.option("--verbose", is_flag=True)
@click.argument("prompt", nargs=-1)
def question(verbose, prompt):
    prompt_context = client.get_prompt_preset("question", verbose)

    question = prompt_context + " Question: " + prompt[0] + "\nAnswer: "
    response = client.request(question)

    client.display_message("Bot", response)


@main.command()
@click.option("--verbose", is_flag=True)
@click.argument("prompt", nargs=-1)
def fix(verbose, prompt):
    prompt_context = client.get_prompt_preset("fix", verbose)

    question = prompt_context + " Question: " + prompt[0] + "\nAnswer: "
    response = client.request(question)

    client.display_message("Bot", response)


@main.command()
@click.argument("prompt", nargs=-1)
def complete(prompt):
    prompt_context = client.get_prompt_preset("complete", False)

    question = prompt_context + " " + prompt[0] + "\nAnswer: "
    response = client.request(question)

    client.display_message("Bot", response)


@main.command()
@click.argument("initial_prompt", nargs=-1)
def chat(initial_prompt):
    print(
        "[bold green]Chat mode [italic yellow]activated[/italic yellow].\nWrite a message or press [italic yellow]/quit[/italic yellow] to quit"
    )

    chat = []

    if initial_prompt:
        print("[bold yellow]You:[/bold yellow]", initial_prompt[0])

        initial_response = client.request(prompt=initial_prompt[0])
        client.display_message("Bot", initial_response)

        chat.append({"question": initial_prompt[0], "answer": initial_response})

    while True:
        prompt = client.ask_user()
        if prompt == "/q" or prompt == "/quit":
            break
        response = client.request(prompt=prompt, chat=chat)

        client.display_message("Bot", response)

        chat.append({"question": prompt, "answer": response})


if __name__ == "__main__":
    main()
