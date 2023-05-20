import click
from . import client
from rich.console import Console
from rich import print

console = Console()
bot_name = "AIT"


@click.group()
def main():
    pass


@main.command()
@click.option("--verbose", "-v", is_flag=True)
@click.argument("prompt", nargs=-1)
def question(verbose, prompt):
    """
    Ask a question to AITility. Add your prompt between double quotes "".
    Use the '--verbose' flag to get a longer and more detailed answer.
    """
    prompt_context = client.get_prompt_preset("question", verbose)

    question = prompt_context % prompt[0]
    response = client.request(question)

    client.display_message(bot_name, response)


@main.command()
@click.option("--verbose", "-v", is_flag=True)
@click.argument("prompt", nargs=-1)
def fix(verbose, prompt):
    """
    Tries its best to fix a command you gave it. Type your command surrounded by double quotes "".
    """
    prompt_context = client.get_prompt_preset("fix", verbose)

    question = prompt_context % prompt[0]
    response = client.request(question)

    client.display_message(bot_name, response)


@main.command()
@click.argument("prompt", nargs=-1)
def complete(prompt):
    """
    Gives some suggestions to complete your command. Type an uncomplete command surrounded by double quotes "".
    """
    prompt_context = client.get_prompt_preset("complete", False)

    question = prompt_context % prompt[0]
    response = client.request(question)

    client.display_message(bot_name, response)


@main.command()
@click.argument("initial_prompt", nargs=-1)
def chat(initial_prompt):
    """
    Activates the chat. Type /quit to quit.
    If you wish, you can give an initial prompt surrounded by double quotes ""
    """
    print(
        "[bold green]Chat mode [italic yellow]activated[/italic yellow].\nWrite a message or press [italic yellow]/quit[/italic yellow] to quit"
    )

    chat = []

    if initial_prompt:
        print("[bold yellow]You:[/bold yellow]", initial_prompt[0])

        initial_response = client.request(prompt=initial_prompt[0])
        client.display_message(bot_name, initial_response)

        chat.append({"question": initial_prompt[0], "answer": initial_response})

    while True:
        prompt = client.ask_user()
        if prompt == "/q" or prompt == "/quit":
            break
        response = client.request(prompt=prompt, chat=chat)

        client.display_message(bot_name, response)

        chat.append({"question": prompt, "answer": response})


if __name__ == "__main__":
    main()
