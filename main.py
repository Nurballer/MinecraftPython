from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
Sky()
player = FirstPersonController()
block_pick = 1
def update():
    global block_pick
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
glass_texture = load_texture('assets/glass_block.png')

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.rgb(211,211,211),
            scale = 1)
    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal, texture=glass_texture)

            if key == 'left mouse down':
                destroy(self)

for z in range(20):
    for x in range(20):
        voxel = Voxel (position = (x,0,z))

app.run()
