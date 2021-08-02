import maya.cmds as cmds

keyframes = cmds.keyframe(attribute ='focusDistance', q=True)

new_keyframes = []
keyframe_value = 51

CurrentUnit = cmds.currentUnit( query = True, linear= True)

changeUnit = cmds.currentUnit(linear ='m')

list_cameras = cmds.listCameras()

#select camera

def select_camera():
    CameraSelect =  list_cameras
    for cam in CameraSelect:
        print('this is the camera',CameraSelect[0])
        break

select_camera()  

#get the units of the maya scene 
 
# def currentunit():
#     unit = CurrentUnit
#     if unit  == CurrentUnit:
#         print('not changing unit')
  
# currentunit()

# # change units to meter if it's not meter
# def changingunit():
#      unit_changing = changeUnit
#      unit = CurrentUnit
#      if unit_changing != unit:
#          print('changing unit to: ',unit_changing)
#      if unit == currentunit:
#         print('not changing unit')

     

changingunit()

#get keyframes focus distance keys from camera in Maya

def getkeyframes():

    get_keyframes = keyframes
    for key in get_keyframes:
        new_keyframes.append(key)
    print(' these are the keyframes of the maya camera: ',new_keyframes)

getkeyframes()    
 

#subtracting maya focus distance from Maya to Game Engine 

def subtract_keyframes():

    game_engine_keys =  [key - 51 for key in cmds.keyframe(attribute ='focusDistance', q=True) if key > 50 ]
    print('these are the game engine key frames',game_engine_keys)

subtract_keyframes()    


#don't change  units if it's correct unit 
def nochange():
    unit = cmds.currentUnit( query = True, linear= True)
    if unit == CurrentUnit:
        print('not changing units already in meters')


nochange()    

