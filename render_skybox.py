######################################################################
# Script to automatically create skybox compatible with Unity 
# Set these variables to choose saving folder and image size:
savePath = "D:/"
imageSize = 1024
######################################################################

import bpy
import math
import mathutils
import os


scene = bpy.context.scene

cam_data = bpy.data.cameras.new('SkyBoxCamera')
cam = bpy.data.objects.new('SkyBoxCamera', cam_data)
bpy.context.collection.objects.link(cam)
scene.camera = cam

bpy.context.scene.render.resolution_x = imageSize
bpy.context.scene.render.resolution_y = imageSize
cam.data.lens_unit = 'FOV'
cam.data.angle = 1.5708

#cam.rotation_clear(clear_delta=False)0
scene.render.image_settings.file_format = 'PNG'

cam.rotation_euler = mathutils.Euler((0, 0, 0))
scene.render.filepath = os.path.join(savePath, "SkyBox_Down.png")
bpy.ops.render.render(write_still = 1)

cam.rotation_euler = mathutils.Euler((math.pi/2, 0, 0))
scene.render.filepath = os.path.join(savePath, "SkyBox_Front.png")
bpy.ops.render.render(write_still = 1)

cam.rotation_euler = mathutils.Euler((math.pi, 0, 0))
scene.render.filepath = os.path.join(savePath, "SkyBox_Up.png")
bpy.ops.render.render(write_still = 1)

cam.rotation_euler = mathutils.Euler((math.pi*3/2, math.pi, 0))
scene.render.filepath = os.path.join(savePath, "SkyBox_Back.png")
bpy.ops.render.render(write_still = 1)

cam.rotation_euler = mathutils.Euler((-math.pi/2, math.pi,-math.pi/2))
scene.render.filepath = os.path.join(savePath, "SkyBox_Right.png")
bpy.ops.render.render(write_still = 1)

cam.rotation_euler = mathutils.Euler((math.pi/2,0,-math.pi/2))
scene.render.filepath = os.path.join(savePath, "SkyBox_Left.png")
bpy.ops.render.render(write_still = 1)

objs = bpy.data.objects
objs.remove(cam, do_unlink=True)
