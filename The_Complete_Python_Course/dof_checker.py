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
    unit = CurrentUnit
    if unit == CurrentUnit:
        unit =  CurrentUnit
        print('this was the unit',unit)
      
    elif unit != changeUnit:
        print('changing units to meters',unit)
    else:
        unit =  CurrentUnit
        print('not changing unit',unit)      


nochange()    

