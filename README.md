# Image Color Scheme Transformer

This Python script applies a color scheme to an image by transforming its colors to match the selected theme. The color scheme are defined in a JSON file, 'color-scheme.json', which contains multiple themes with associated color palettes. The script then maps the original image colors to the closet colors from the selected theme using a KD-Tree for efficient color matching.

## How It Works

1. The script load a set of color schemes from 'color-scheme.json' file.
2. The user is prompted to select a theme from the available options.
3. The selected color palette is applied to the image, changing its appearance.
4. Enjoy ricing.

### Example Usage

```bash
python main.py {your_image path}
```

### Results

Here is an example of the original image and the three resulting images:

| Original Image                       | Nord                                  | Gruvbox                               | Tokyo Night                                     |
| ------------------------------------ | ------------------------------------- | ------------------------------------- | ----------------------------------------------- |
| ![Original Image](assets/makima.jpg) | ![Catppuccin](assets/makima_Nord.png) | ![Gruvbox](assets/makima_Gruvbox.png) | ![Tokyo Night](assets/makima_Tokyo%20Night.png) |

### Note

This scripts works better with simple images. If you put an imagen with a lot of details it may not work as expected.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
