import argparse
import json
import numpy as np
from PIL import Image, ImageFilter
from scipy.spatial import KDTree
from rich.console import Console
from rich.table import Table
from rich.progress import track

console = Console()

def load_colorscheme():
    with open("color-scheme.json") as f:
        data = json.load(f)
        themes = {i + 1: theme["name"] for i, theme in enumerate(data["themes"])}
        return data, themes

def select_theme(themes):
    console.print("[bold cyan]Available Themes:[/bold cyan]")
    table = Table(title="Themes", show_header=True, header_style="bold magenta")
    table.add_column("Number", justify="center")
    table.add_column("Theme Name", justify="left")

    for key, value in themes.items():
        table.add_row(str(key), value)

    console.print(table)

    selection = console.input("[bold yellow]Select a theme by number:[/bold yellow] ")
    if selection.isdigit() and int(selection) in themes:
        return themes[int(selection)]
    else:
        raise ValueError("Invalid theme selection")

def generate_extended_palette(colors, steps=10):
    extended_colors = []
    for color in colors:
        for i in range(-steps, steps + 1):
            new_color = tuple(max(0, min(255, c + i)) for c in color)
            extended_colors.append(new_color)
    return np.unique(extended_colors, axis=0)

def apply_colorscheme(image_path: str, colors, theme: str):
    img = Image.open(image_path).convert("RGB")
    img_data = np.array(img)
    original_shape = img_data.shape
    img_data_flat = img_data.reshape(-1, 3)

    # Extend the palette for smoother gradients
    colors = generate_extended_palette(colors)
    tree = KDTree(colors)

    console.print("[bold green]Applying colorscheme, please wait...[/bold green]")

    # Process pixels in batches for progress
    batch_size = len(img_data_flat) // 100  # Divide into 100 batches
    indices = []
    for i in track(range(0, len(img_data_flat), batch_size), description="Transforming pixels..."):
        batch = img_data_flat[i:i + batch_size]
        _, batch_indices = tree.query(batch)
        indices.extend(batch_indices)

    new_img_data_flat = np.array([colors[i] for i in indices])
    new_img_data = new_img_data_flat.reshape(original_shape)

    new_img = Image.fromarray(np.uint8(new_img_data), mode="RGB")
    new_img = new_img.filter(ImageFilter.SMOOTH)  # Smooth to reduce artifacts

    output_path = f'{image_path.split(".")[0]}_{theme}.png'
    new_img.save(output_path)
    console.print(f"[bold cyan]Colorscheme applied successfully![/bold cyan] [green]{output_path}[/green]")

def main():
    parser = argparse.ArgumentParser(description="Apply a colorscheme to an image")
    parser.add_argument("image", help="Path to the image")
    args = parser.parse_args()

    data, themes = load_colorscheme()

    try:
        selected_theme = select_theme(themes)
        colors = [
            tuple(int(color[i: i + 2], 16) for i in (1, 3, 5))
            for theme in data["themes"]
            if theme["name"] == selected_theme
            for color in theme["colors"]
        ]
        if not colors:
            raise ValueError("No colors found for the selected theme")

        apply_colorscheme(args.image, colors, selected_theme)
    except ValueError as e:
        console.print(f"[bold red]Error:[/bold red] {e}")

if __name__ == "__main__":
    main()
