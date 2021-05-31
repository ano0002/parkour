from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from player import Player
# App/Window
app = Ursina()

normalSpeed = 1
boostSpeed  = 2

normalJump = 0.3
boostJump  = 1

# Sky texture
sky_texture = load_texture("assets/sky.png")

# Normal Block Class
class NormalBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.8, 3),
            color = "#AFFF3C",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

# Jump Block Class
class JumpBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.8, 3),
            color = "#FF8B00",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

# Speed Block Class
class SpeedBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.5, 8),
            color = "#53FFF5",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

# Slow Block Class
class SlowBlock(Entity):
    def __init__(self, position = (0, 0, 0)):
        super().__init__(
            model = "cube",
            scale = Vec3(3, 0.5, 15),
            color = "#FF453F",
            collider = "box",
            texture = "white_cube",
            position = position,
        )

# Player
player = Player("cube",(0,2,0),"box")
player.SPEED = normalSpeed
player.jump_height = normalJump

# Sky
sky = Sky(texture = "assets/sky")

# Lighting
light = PointLight(parent = camera, position = (0, 10, -1.5))
light.color = color.white

AmbientLight(color = color.rgba(100, 100, 100, 0.1))

#Level01

block_1 = NormalBlock(position = (0, 1, 9))
block_1_1 = NormalBlock(position = (0, 2, 14))
block_1_2 = NormalBlock(position = (0, 3, 19))
block_1_3 = NormalBlock(position = (0, 4, 24))
block_1_4 = NormalBlock(position = (5, 5, 24))
block_1_5 = NormalBlock(position = (10, 6, 24))
block_1_6 = JumpBlock(position = (17, 2, 24))
block_1_7 = NormalBlock(position = (25, 10, 24))
block_1_8 = SpeedBlock(position = (25, 10, 33))

ground_1 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA")
finishBlock_1 = Entity(model = "cube", scale_x = 5, scale_z = 5, collider = "box", texture = "white_cube", color = "#CACACA", position = (25, 10, 45))

def speed():
    player.SPEED = normalSpeed

def update():
    # Escape button quits
    if held_keys["escape"]:
        application.quit()

    # Stops the player from falling forever
    if player.position.y <= -50:
        player.position = Vec3(0, 2, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump

    # Restart the level
    if held_keys["g"]:
        player.position = Vec3(0, 2, 0)
        player.SPEED = normalSpeed
        player.jump_height = normalJump

    # What entity the player hits
    hit = raycast(player.position, player.down, distance=2, ignore=[player,])
    
    if hit.entity == block_1_6:
        player.jump_height = boostJump
    elif hit.entity != block_1_6:
        player.jump_height = normalJump

    if hit.entity == block_1_8:
        player.SPEED = boostSpeed
        invoke(speed, delay=3)

    if hit.entity == finishBlock_1:
        destroyLevel01()
        player.position = Vec3(0,2,0)
    
    if block_2_2.enabled == True:
        if hit.entity == block_2_2:
            player.jump_height = boostJump*1.3
        elif hit.entity != block_2_2:
            player.jump_height = normalJump

    if block_2_5.enabled == True:
        if hit.entity == block_2_5:
            player.SPEED = boostSpeed
            invoke(speed, delay=3)

    if finishBlock_2.enabled == True:
        if hit.entity == finishBlock_2:
            destroyLevel02()
            player.position = Vec3(0,2,0)

    if hit.entity == block_3_1:
        player.SPEED = boostSpeed
    if hit.entity == block_3_2:
        player.SPEED = boostSpeed*1.5
    if hit.entity == block_3_3:
        player.SPEED = boostSpeed *2
    if hit.entity == block_3_4:
        player.SPEED = boostSpeed *2.5
    if hit.entity == block_3_5:
        player.SPEED = boostSpeed *3.5
    if hit.entity == block_3_6:
        player.SPEED = boostSpeed * 5
    if hit.entity == block_3_7:
        player.SPEED = boostSpeed *6
    if hit.entity == block_3_8:
        player.SPEED = normalSpeed

#Level02

ground_2 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA")
finishBlock_2 = Entity(model = "cube", scale_x = 5, scale_z = 5, collider = "box", texture = "white_cube", color = "#CACACA", position = (0, 11, 67))

block_2 = NormalBlock(position = (0, 1, 9))
block_2_1 = NormalBlock(position = (0, 2, 15))
block_2_2 = JumpBlock(position = (0, -20, 25))
block_2_3 = NormalBlock(position = (0, 10, 30))
block_2_4 = NormalBlock(position = (0, 10, 37))
block_2_5 = SpeedBlock(position = (0, 10, 45))
block_2_6 = NormalBlock(position = (0, 11, 60))

ground_2.disable()
finishBlock_2.disable()
block_2.disable()
block_2_1.disable()
block_2_2.disable()
block_2_3.disable()
block_2_4.disable()
block_2_5.disable()
block_2_6.disable()




#Level03

ground_3 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA")
block_3_1 = SpeedBlock(position = (0, 0, 13))
block_3_2 = SpeedBlock(position = (0, 0, 32))
block_3_3 = SpeedBlock(position = (0, 0, 58))
block_3_4 = SpeedBlock(position = (0, 0, 80))
block_3_5 = SpeedBlock(position = (0, 0, 120))
block_3_6 = SpeedBlock(position = (0, 0, 180))
block_3_7 = SpeedBlock(position = (0, 0, 240))
block_3_8 = SlowBlock(position = (0, 0, 300))

finishBlock_3 = Entity(model = "cube", scale_x = 10, scale_z = 10, collider = "box", texture = "white_cube", color = "#CACACA", position = (0, 0, 315))

ground_3.disable()
finishBlock_3.disable()
block_3_1.disable()
block_3_2.disable()
block_3_3.disable()
block_3_4.disable()
block_3_5.disable()
block_3_6.disable()
block_3_7.disable()
block_3_8.disable()



def destroyLevel01():
    block_1.disable()
    block_1_1.disable()
    block_1_2.disable()
    block_1_3.disable()
    block_1_4.disable()
    block_1_5.disable()
    block_1_6.disable()
    block_1_7.disable()
    block_1_8.disable()
    ground_1.disable()
    finishBlock_1.disable()

    ground_2.enable()
    finishBlock_2.enable()
    block_2.enable()
    block_2_1.enable()
    block_2_2.enable()
    block_2_3.enable()
    block_2_4.enable()
    block_2_5.enable()
    block_2_6.enable()
    player.SPEED = normalSpeed
    player.jump_height = normalJump

def destroyLevel02():
    block_2.disable()
    block_2_1.disable()
    block_2_2.disable()
    block_2_3.disable()
    block_2_4.disable()
    block_2_5.disable()
    block_2_6.disable()
    ground_2.disable()
    finishBlock_2.disable()

    ground_3.enable()
    finishBlock_3.enable()
    block_3_1.enable()
    block_3_2.enable()
    block_3_3.enable()
    block_3_4.enable()
    block_3_5.enable()
    block_3_6.enable()
    block_3_7.enable()
    block_3_8.enable()
    player.SPEED = normalSpeed
    player.jump_height = normalJump


    
app.run()
