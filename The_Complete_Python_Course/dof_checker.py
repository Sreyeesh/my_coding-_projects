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
    return('this is the camera',CameraSelect[0])
    
   

print(select_camera())

#get keyframes focus distance keys from camera in Maya

def getkeyframes():

    get_keyframes = keyframes
    for key in get_keyframes:
        new_keyframes.append(key)
        if key == None: 
            print('not running because no focus distance keys are keyd')
    print(' these are the keyframes of the maya camera: ',new_keyframes)

getkeyframes()    
 

#subtracting maya focus distance from Maya to Game Engine 

def subtract_keyframes():

    game_engine_keys =  [key - 51 for key in cmds.keyframe(attribute ='focusDistance', q=True) if key > 50 ]
    print('these are the game engine key frames',game_engine_keys)

subtract_keyframes()    
#change unit to meters
def change_unit():
    oldUnit = CurrentUnit
    if oldUnit !=  cmds.currentUnit(linear = 'm'):
        print('trying to chang into correct unit ....')
    print(oldUnit)
  

change_unit()        

#don't change  units if it's correct unit 
def nochange():
    unit = cmds.currentUnit(query = True, linear = True)
    if unit == CurrentUnit:
        print('not changing unit because it is in the correct unit meters',unit) 
    


nochange()

def camera_attribute():
    key = []
    for key in

