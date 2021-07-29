import maya.cmds as cmds

keyframes = cmds.keyframe(attribute ='focusDistance', q=True)
# print('these are the keyframes',keyframes)
new_keyframes = []
keyframe_value = 51

def get_keyframes():
    for keys in keyframes:
        print(keys)
        
get_keyframes()

def Show_TED_keyframes():
    new_keyframes.append(keyframes)
    print('these keyframes will be converted into new  keyframes',new_keyframes)
    for key in  new_keyframes:
        if  key in new_keyframes: 
            print(key)
    # if
    #     Ted_Keyframes = keyframes - keyframe_value 
    #     print('these are the Ted_keyframes',Ted_Keyframes)

Show_TED_keyframes()

def calculate_keyframes(): # work on this 
    new_keyframes.append(keyframes)
    for key in keyframes:
        Ted_keyframes = new_keyframes - int(keyframe_value)
        print('these are the new keyframes',calculate_keyframes)

calculate_keyframes()    