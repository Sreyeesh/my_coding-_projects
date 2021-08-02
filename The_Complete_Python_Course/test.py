import maya.cmds as cmds

keyframes = cmds.keyframe(attribute ='focusDistance', q=True)
# print('these are the keyframes',keyframes)
new_keyframes = []
keyframe_value = 51

CurrentUnit = cmds.currentUnit( query = True, linear= True)
print('this is the current unit', CurrentUnit)


  
