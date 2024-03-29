from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.scene import Scene

app = Ursina()
player = FirstPersonController()
block_pick = 1
break_sound = Audio('assets/break_sound',loop = False, autoplay = False)
place_sound = Audio('assets/place_sound',loop = False, autoplay = False)
background_sound = Audio('assets/background_sound',loop = True, autoplay = True, volume = 0.5)
background_sound.play()

camera.fov = 100
def update():
    global block_pick
    player.y -= 0.0099
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
    if held_keys['1']: block_pick = 1
    if held_keys['2']: block_pick = 2
    if held_keys['3']: block_pick = 3
    if held_keys['4']: block_pick = 4
    if player.intersects(Death).hit:
        print('die')
        player.position = player.start_position

grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
glass_texture = load_texture('assets/glass_block.png')
sky_texture = load_texture('assets/skybox1.png')
arm_texture = load_texture('assets/arm_texture.png')
white_cube = load_texture('assets/white_cube')

class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = "assets/block",
            origin_y = 0.5,
            texture = texture,
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.rgb(211,211,211),
            scale = 0.5)
    def input(self,key):
        if self.hovered:
            if key == 'right mouse down':
                place_sound.play()
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2: voxel = Voxel(position=self.position + mouse.normal, texture=stone_texture)
                if block_pick == 3: voxel = Voxel(position=self.position + mouse.normal, texture=dirt_texture)
                if block_pick == 4: voxel = Voxel(position=self.position + mouse.normal, texture=glass_texture)

            if key == 'left mouse down':
                break_sound.play()
                destroy(self)

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = "sphere",
            texture = sky_texture,
            scale = 10000,
            double_sided = True
        )
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'assets/arm',
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.6,-0.6)
        )
    def active(self):
        self.position = Vec2(0.5, -0.5)

    def passive(self):
        self.position = Vec2(0.6, -0.6)
class Death(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'cube',
            color=color.orange,
            scale= (100,1000,100),
            collider='box'
        )

for z in range(20):
    for x in range(20):
        voxel = Voxel (position = (x,0,z))

sky = Sky()
hand = Hand()

app.run()
