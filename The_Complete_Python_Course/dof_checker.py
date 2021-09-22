import maya.cmds as cmds

# keyframes = cmds.keyframe(attribute ='focusDistance', q=True)


new_keyframes = []
keyframe_value = 51

# CurrentUnit = cmds.currentUnit(fullName=True, query = True, linear= True)

# changeUnit = cmds.currentUnit(fullName=True,linear ='meter')

# list_cameras = cmds.listCameras()

#value = cmds.getAttr("myCameraShape.attrName")

#list camera
def list_camera():
    list_cameras = cmds.listCameras()
    return list_cameras[0]
    
print(list_camera())

#get keyframes focus distance keys from camera in Maya

def getkeyframes():
    keyframes = cmds.keyframe(attribute ='focusDistance', q=True)
    get_keyframes = keyframes
   
    for key in get_keyframes:
        new_keyframes.append(key)
    print(' these are the keyfra1mes of the maya camera: ',new_keyframes)

getkeyframes()    
 

#subtracting maya focus distance from Maya to Game Engine 

def subtract_keyframes():

    game_engine_keys =  [key - 51 for key in cmds.keyframe(attribute ='focusDistance', q=True) if key > 50 ]
    print('these are the game engine key frames',game_engine_keys)

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












