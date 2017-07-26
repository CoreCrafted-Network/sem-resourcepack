import os
from configobj import ConfigObj

state = 0

def checkBasics(props, root, filename):
    global state
    if props.get('items') is None:
        print('======================================================')
        print("-> Problem found at " + os.path.join(root, filename) + ":")
        print('-> Missing / invalid "items" property')
        state = 1
    if props.get('nbt.display.Name') is None:
        print('======================================================')
        print("-> Problem found at " + os.path.join(root, filename) + ":")
        print('-> Missing / invalid "nbt.display.Name" property')
        state = 1


def checkTexture(props, root, filename):
    global state
    texture = props.get('texture')
    if not os.path.isfile(os.path.join(root, texture)):
        print('======================================================')
        print("-> Problem found at " + os.path.join(root, filename) + ":")
        print('-> "texture" not found')
        state = 1
    if texture.replace(".png", "") != filename.replace(".properties", ""):
        print('======================================================')
        print("-> Problem found at " + os.path.join(root, filename) + ":")
        print('-> "texture" filename is not the same as properties file name')
        state = 1


def main():
    global state
    for root, dirs, files in os.walk(os.getcwd()):
        for filename in files:
            if filename.endswith('.properties'):
                props = ConfigObj(os.path.join(root, filename))
                citType = props.get('type')
                # print("null" if citType is None else citType)
                if citType in ("item", "elytra", "enchantment"):
                    checkBasics(props, root, filename)
                    checkTexture(props, root, filename)
                elif citType == "armor":
                    checkBasics(props, root, filename)
                else:
                    print('======================================================')
                    print("-> Problem found at " + os.path.join(root, filename) + ":")
                    print('-> "type" is invalid')
                    state = 1


main()
if state == 0:
    print('======================================================')
    print("=> Processed finished No problem found :)")
exit(state)
