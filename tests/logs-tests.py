from rich.console import Console
from rich.markdown import Markdown

console = Console()

code = """```python
from rich.console import Console
console = Console()
```"""

console.print(Markdown(code))
