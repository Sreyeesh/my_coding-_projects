from maya import cmds

current_unit = cmds.currentUnit( query=True, linear=True )



new_unit = cmds.currentUnit( linear= 'm' )





