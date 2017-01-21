import bge
import math

keyboard = bge.logic.keyboard

scene=bge.logic.getCurrentScene()

player = scene.objects["Player"]
print(player)

JUST_ACTIVATED = bge.logic.KX_INPUT_JUST_ACTIVATED

if keyboard.events[bge.events.SPACEKEY] == JUST_ACTIVATED:
    player["running"] = True
    player["timer"] = 0

phase = 0
amplitude = 0
frequency = 1


if player["running"]:
    t = player["timer"]
    player.localPosition.x = t
    player.localPosition.y = amplitude*math.sin(frequency*t+phase)

