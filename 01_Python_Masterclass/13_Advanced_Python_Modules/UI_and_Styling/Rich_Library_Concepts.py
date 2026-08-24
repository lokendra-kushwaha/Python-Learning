"""
====================================================================================
🎨 RICH LIBRARY MASTERCLASS - TERMINAL UI/UX GUIDE
====================================================================================
Description: A complete reference guide for designing beautiful terminal outputs 
             in Python using the 'rich' library.
             
Why use Rich? 
Normal print() statements are boring and hard to debug. Rich provides colors, 
tables, markdown, progress bars, and advanced error tracebacks out of the box!
====================================================================================
"""

import time
from rich.console import Console
from rich.text import Text
from rich.theme import Theme
from rich.traceback import install
from rich.table import Table
from rich.markdown import Markdown
from rich.progress import track

# GLOBAL CONSOLE OBJECT (Used throughout the script)
console = Console()

def section_divider(title):
    """A designer divider to keep the terminal output clean and organized."""
    console.print(f"\n[bold cyan]{'=' * 20} {title} {'=' * 20}[/]\n")


# 🟢 1. BASIC STYLING & MARKUP
section_divider("1. STYLING & MARKUP")
"""
Concept: You can style text using the `style` parameter or by utilizing 
markup tags like `[color]`.
"""
console.print("Lokendra", style='bold underline green')
console.print("Lokendra Kushwaha", style='bold underline red on white')

# Markup method (Similar to HTML/XML) - This is the most commonly used approach.
console.print("[bold]Lokendra [cyan]Kushwaha[/] is testing rich markup.[/]")

# Text Object: Useful when you want to style only specific parts of a string based on index.
text = Text("Hello world!")
text.stylize("bold magenta", 0, 5)  # Highlights from index 0 to 5 (the word 'Hello')
console.print(text)


# 🟢 2. CUSTOM THEMES
section_divider("2. CUSTOM THEMES")
"""
Concept: Instead of repeating color strings everywhere, you can define a custom 'Theme' 
(similar to CSS classes like success, error, warning).
"""
custom_theme = Theme({
    "success": "bold green", 
    "error": "bold red on white"
})
theme_console = Console(theme=custom_theme)

theme_console.print("Operation successful!", style="success")
theme_console.print("Operation failed!", style="error")

# Using the custom theme inside markup tags
theme_console.print("System status: [error]CRITICAL FAILURE[/error]")


# 🟢 3. EMOJIS
section_divider("3. EMOJIS")
"""
Concept: You can render emojis directly in the terminal using the `:emoji_name:` syntax.
(Note: Fixed 'thump_up' to the correct 'thumbs_up').
"""
console.print(":thumbs_up: File downloaded successfully!")
console.print(":apple: :bug: :fire: :rocket: [bold red]❌ Error[/]")


# 🟢 4. ADVANCED LOGGING
section_divider("4. ADVANCED LOGGING")
"""
Concept: Use `console.log()` instead of the standard `print()`. 
It automatically appends the execution time and the file path/line number!
"""
for i in range(3):
    console.log(f"Doing important stuff... step {i}")
    time.sleep(0.1)


# 🟢 5. TRACEBACKS & HTML EXPORT
section_divider("5. TRACEBACKS & HTML EXPORT")
"""
Concept: 
1. `install()` transforms standard, boring Python tracebacks into beautiful, readable errors.
2. `log_locals=True` displays the exact values of variables at the time of execution.
3. `record=True` allows you to export the entire terminal output to an HTML file.
"""
install() # Globally replaces default Python tracebacks with Rich tracebacks

record_console = Console(record=True)

def add(x, y):
    a = 'Hello Locals' # This variable will be visible in the locals output upon error
    record_console.log("Adding two numbers", log_locals=True)
    return x + y

try:
    add(1, 2)
    add(1, 'a') # 🚨 Intentional Error (int + string) to trigger the traceback
except Exception:
    # Prints the exception in a stylized, colorful format
    record_console.print_exception(show_locals=True)

# Saves the complete output/error report to an HTML file (great for sharing logs)
record_console.save_html("Rich_Error_Report.html")
console.print("[bold green]✅ Error report saved to 'Rich_Error_Report.html'[/]")


# 🟢 6. DATA TABLES
section_divider("6. DATA TABLES")
"""
Concept: Tables are the best way to display structured data coming from a Database or an API.
"""
table = Table(title="🌟 Star Wars Movies Box Office")

table.add_column("Released", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green bold italic")

table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,698")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$392,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. VIII: The Last Jedi", "$1,332,539,889")

console.print(table)


# 🟢 7. MARKDOWN RENDERING
section_divider("7. MARKDOWN RENDERING")
"""
Concept: The `Markdown` class renders markdown text or `.md` files directly 
in the terminal, looking just like a webpage.
"""
MARKDOWN = """
# 🚀 Python Rich Library
Rich can do a pretty *decent* job of rendering markdown.

### Key Features:
1. **Beautiful logs** and tracebacks.
2. Custom *themes* and **emojis**.
3. Awesome data tables!
"""
md = Markdown(MARKDOWN)
console.print(md)


# 🟢 8. PROGRESS BARS
section_divider("8. PROGRESS BARS")
"""
Concept: Wrap any iterable (like `range` or a list) with the `track` function, 
and it automatically generates a beautiful progress bar!
"""
for i in track(range(5), description="[bold green]Processing Data..."):
    time.sleep(0.3)

console.print("\n[bold gold1]🎉 ALL CONCEPTS EXECUTED SUCCESSFULLY! 🎉[/]")