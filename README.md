# pyxel_scalable_writing
**This module is made to run with pyxel**

This module allow to write with a scaling text function

you MUST have a pyxres file that contain a white square of 20 pyxel width named writing_module.pyxres, you can use the one of the github

WON'T work with a white square superior to 20 px

To show your personnalised text, you must use the method parsing of class Character

`Characters.parsing(string, x_depart, y_depart, unity_width, transparence)`

`string` is the text you want to show us

`x_depart` and `y_depart` is the top left position coordinates of your text

`unity_width` is an optional paremeter, it's the width of an unity of your image (like a pixel but bigger), its default value is 5

`transparence` is an optional element that is True by default, if you want to have your text on a black background, call it as False

[on pypi !](https://pypi.org/project/scalablewritingpyxel/)