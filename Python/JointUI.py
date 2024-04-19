import maya.cmds as cmds

def renameJoints(startJoint, endJoint, prefix, *args):
    joints = cmds.ls(startJoint, endJoint)
    for i, joint in enumerate(joints):
        newName = prefix + str(i+1)
        cmds.rename(joint, newName)
    cmds.text('Joints renamed to: ' + ', '.join(cmds.ls(prefix + '*')))

def createUI():
    windowName = "RenameJointsWindow"
    if cmds.window(windowName, exists=True):
        cmds.deleteUI(windowName)

    cmds.window(windowName, title="Rename Joints", widthHeight=(300, 150))
    cmds.columnLayout(adjustableColumn=True)

    cmds.text(label="Start Joint:")
    startJointField = cmds.textField()
    cmds.text(label="End Joint:")
    endJointField = cmds.textField()
    cmds.text(label="Prefix:")
    prefixField = cmds.textField()

    cmds.rowLayout(numberOfColumns=2)
    cmds.button(label="Rename", command=lambda *args: renameJoints(
        cmds.textField(startJointField, query=True, text=True),
        cmds.textField(endJointField, query=True, text=True),
        cmds.textField(prefixField, query=True, text=True),
        args))
    cmds.button(label="Close", command=lambda *args: cmds.deleteUI(windowName))

    cmds.showWindow(windowName)

createUI()