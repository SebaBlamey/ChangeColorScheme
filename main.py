import argparse
import json

import numpy as np
from PIL import Image
from scipy.spatial import KDTree


def load_colorscheme():
    with open("color-scheme.json") as f:
        data = json.load(f)
        themes = {i + 1: theme["name"] for i, theme in enumerate(data["themes"])}
        return data, themes


def select_theme(themes):
    print("Available Themes:")
    for key, value in themes.items():
        print(f"{key}: {value}")

    selection = int(input("Select a theme by number: "))
    if selection in themes:
        return themes[selection]
    else:
        raise ValueError("Invalid theme selection")


def apply_colorscheme(image_path: str, colors, theme: str):
    img = Image.open(image_path).convert("RGB")
    img_data = np.array(img)
    original_shape = img_data.shape
    img_data_flat = img_data.reshape(-1, 3)

    colors = np.array(colors, dtype=np.uint8)
    tree = KDTree(colors)

    _, indices = tree.query(img_data_flat)
    new_img_data_flat = np.array([colors[i] for i in indices])
    new_img_data = new_img_data_flat.reshape(original_shape)

    new_img = Image.fromarray(np.uint8(new_img_data), mode="RGB")
    new_img.save(f'{image_path.split(".")[0]}_{theme}.png')


def main():
    parser = argparse.ArgumentParser(description="Apply a colorscheme to an image")
    parser.add_argument("image", help="Path to the image")
    args = parser.parse_args()

    data, themes = load_colorscheme()

    try:
        selected_theme = select_theme(themes)
        colors = [
            tuple(int(color[i : i + 2], 16) for i in (1, 3, 5))
            for theme in data["themes"]
            if theme["name"] == selected_theme
            for color in theme["colors"]
        ]
        if not colors:
            raise ValueError("No colors found for the selected theme")

        apply_colorscheme(args.image, colors, selected_theme)
        print("Colorscheme applied successfully")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
