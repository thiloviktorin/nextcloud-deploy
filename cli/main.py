import typer
from pydantic import ValidationError
from rich.console import Console

from cli.settings import get_settings

app = typer.Typer()
console = Console()
err_console = Console(stderr=True)


@app.command()
def validate() -> None:
    """Validate the configuration and report any errors."""
    try:
        get_settings()
        console.print("[green]Configuration is valid.[/green]")
    except ValidationError as ve:
        err_console.print("[red]Validation error:[/red]")
        for error_dict in ve.errors():
            loc_resolved = ".".join(str(item) for item in error_dict["loc"])
            err_console.print(f"[red]{error_dict['msg']}: {loc_resolved}[/red]")
        raise typer.Exit(code=1)


@app.callback()
def main() -> None:
    """Deploy and manage a self-hosted Nextcloud instance."""
    pass


if __name__ == "__main__":
    app()
