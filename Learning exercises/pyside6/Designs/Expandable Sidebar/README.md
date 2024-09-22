# About
Based mainly in this [tutorial](https://www.youtube.com/watch?v=7DXxQV47jOU&)

# Guide
Mostly follow the tutorial.

At one point the resource file generated needs to be converted into python. It is generated in the same folder as the .ui file that is used by Qt Designer, thus you need to set the folder in the terminal with: 

    CD RAW_UI_Files

then convert with the following terminal command:
    
    pyside6-rcc MW_Resources.qrc -o MW_Resources_rc.py

## Changes from the youtube tutorial
I have used the expansion button both in the expanded and in the contracted sidebar. This requires setting one as toggled, and then in the main.py file to set up initial state of the sidebar.