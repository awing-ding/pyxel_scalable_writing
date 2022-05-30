# pyxel_scalable_writing
**This module is made to run with pyxel**

This module allow to write with a scaling text function

**Won't** work with an image unity width superior to 20

To show your personnalised text, you must use the method parsing of class Character

`Characters.parsing(string, x_depart, y_depart, unity_width)`

`string` is the text you want to show us

`x_depart` and `y_depart` is the top left position of your text

`unity_width` is the width of an unity of your image (like a pixel but bigger)

`transparence` is an optional element that is True by default, if you want to have your text on a black background, call it as False