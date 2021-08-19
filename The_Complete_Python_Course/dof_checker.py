import maya.cmds as cmds




new_keyframes = []
keyframe_value = 51



#list camera
def list_camera():
    list_cameras = cmds.listCameras()
    return list_cameras[0]
    
print(list_camera())

#get attributes

def attributesofcam():
    pass

def getkeyframes():
    keyframes = cmds.keyframe(selected=False, q=True)
   
    if keyframes:
        for key in keyframes:
            new_keyframes.append(key)
        print('these are the keyfra1mes of the maya camera: ', new_keyframes)
        
    print('no keyframes are keyed on the camera')

getkeyframes()
 

#subtracting maya focus distance from Maya to Game Engine

def subtract_keyframes():
    # attributes = ['focusDistance', '...']

    # game_engine_keys =  [key - keyframe_value for key in cmds.keyframe(attribute ='focusDistance', q=True) if key > 50]

    game_engine_keys = []
    keys = cmds.keyframe(selected=False, q=True)
    if keys:
        for key in keys:
            game_engine_keys.append(key - keyframe_value)
            print('these are the game engine key frames', game_engine_keys)


subtract_keyframes()


#get current unit

def get_current_unit():
    currentUnit = cmds.currentUnit(fullName=True, query = True, linear= True)
    return currentUnit

print('this is the current unit',get_current_unit())

#change unit to meters if not meters

def change_to_meters():
    newUnit = cmds.currentUnit( linear='m' )
    return newUnit

print('this is the new unit',change_to_meters())



#not changing unit

def nounitdisplay():
   unit = cmds.currentUnit( linear='m' )
   currentUnit =  cmds.currentUnit( linear='m' )
   while unit:
       if unit ==  currentUnit:
           print('not changing unit')
           break
                   
nounitdisplay()













