# TimeWarp
Time Warp is the idea around node based warping of maya's time. This tool consists of two parts; it's custom node 
called warpStatus and the GUI interface that allows you to add remove and bake out warps.

------------

## Install
TimeWarp can be installed in multiple ways.
### Drag and Drop
For simple installation use the drag_drop_install.py file into maya's viewport. This will launch a GUI follow the prompts to install.

### Manual Install
1. Copy the folder "timeWarp" into your maya/scripts/ preferences directory. So your resulting path will be like:

    **Windows**
    C:/Users/<user>/Documents/maya/scripts/timeWarp

    **Linux (Centos)**
    /home/<user>/maya/scripts/timeWarp

    **OSX**
    /Users/<user>/Library/Preferences/Autodesk/maya/timeWarp
     *OSX Note: To open the Preferences directory:*
     *Select Finder > Go, press Alt and the Library folder will appear in the menu.*

2. Copy **timeWarp.mod** file to documents/maya/modules, create the folder “modules” if it does not exist.

3. Open the .mod file and change "/path/to/timeWarp" to your path to the TimeWarp folder. Hit save.
    **Windows**
    C:/Users/<user>/Documents/maya/scripts/

    **Linux (Centos)**
    /home/<user>/maya/scripts/

    **OSX**
    /Users/<user>/Library/Preferences/Autodesk/maya/
     *OSX Note: To open the Preferences directory:*
     *Select Finder > Go, press Alt and the Library folder will appear in the menu.*

4. While inside the timeWarp.mod file set the correct version number. this can be found in the _version.py file or in the download page.

5. Open Maya, the make sure plugin in loaded for menu to load.
