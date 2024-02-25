import maya.cmds as cmds

# The start and end joint names
startJoint = 'joint1'
endJoint = 'joint10'

# The new joint name prefix
newPrefix = 'arm_'

# Get a list of all the joints from start to end
joints = cmds.ls(startJoint, endJoint)

# Rename each joint with the new prefix
for i, joint in enumerate(joints):
    newName = newPrefix + str(i+1)
    cmds.rename(joint, newName)

print 'Joints renamed to:', cmds.ls(newPrefix + '*')