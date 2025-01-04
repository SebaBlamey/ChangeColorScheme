1: # Image Color Scheme Transformer
2:
3: This Python script applies a color scheme to an image by transforming its colors to match the selected theme. The color scheme are defined in a JSON file, 'color-scheme.json', which contains multiple themes with associated color palettes. The script then maps the original image colors to the closet colors from the selected theme using a KD-Tree for efficient color matching.
4:
5: ## How It Works
6:
7: 1. The script load a set of color schemes from 'color-scheme.json' file.
8: 2. The user is prompted to select a theme from the available options.
9: 3. The selected color palette is applied to the image, changing its appearance.
10: 4. Enjoy ricing.
11:
12: ### Example Usage
13:
14: `bash
15: python main.py {your_image path}
16: `
17:
18: ### Results
19:
20: Here is an example of the original image and the three resulting images:
21:
22: | Original Image | Nord | Gruvbox | Tokyo Night |
23: | ------------------------------------ | ------------------------------------- | ------------------------------------- | ----------------------------------------------- |
24: | ![Original Image](assets/makima.jpg) | ![Catppuccin](assets/makima_Nord.png) | ![Gruvbox](assets/makima_Gruvbox.png) | ![Tokyo Night](assets/makima_Tokyo%20Night.png) |
25:
26: ### Note
27:
28: This scripts works better with simple images. If you put an imagen with a lot of details it may not work as expected.
29:
30: ## License
31:
32: This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
33:
34: ## Dependencies
35:
36: To install the required dependencies, run:
37:
38: `bash
39: pip install -r requirements.txt
40: `
