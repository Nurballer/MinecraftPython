from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
player = FirstPersonController()
Sky()

Blocks = []
for i in range(20):
    for j in range(20):
        block = Button(color=color.green, model = "cube", position=(j, 0, i),
                texture = "grass.png", parent=scene, origin_y = 0.5)
        Blocks.append(block)
class Block(Button):
       def __init__(self, position = (0,0,0)):
            super().__init__(
                parent = scene,
                position = position,
                model = 'cube',
                texture = 'grass.png',
                color = color.white,
                highlight_color = color.black)
for z in range(8):
    for x in range(8):
     Block(position = (x,0,z))
def input(key):
    for block in blocks:
        if block.hovered:
            if key == 'right mouse down':
                new = Button(color=color.green, model= 'cube', position=box.position + mouse.normal,
                            texture = 'grass.png', parent = scene, origin_y = 0.5)
                boxes.append(new)
            if key == 'left mouse down':
                blocks.remove(block)
                destroy(block)
app.run()

