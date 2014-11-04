#MP3 Tag Editor By Pradd

MP3 Tag Editor is a Python Script that helps in fixing missing Album and Artist name details and Album Art of MP3 Music Files.

This Script uses EyeD3 for changing the tag information of MP3 Files and requires this Python module to be installed. 

This can  be done by using the following commands in the terminal (pip must be installed):

```
pip install eyeD3
```

Alternatively [ this link](http://eyed3.nicfit.net//releases/eyeD3-0.7.5.tgz) will download the tar.gz archive of the module from where you can install by the following command:

```
python setup.py install
```

##Usage

This Script can be used either from the console or from the IDLE by modifying the folder variable.

Usage Pattern for the Terminal is:

```
python mp3-tag-editor.py [Entire Folder name]
```

The folder variable in the Script can also be modified if you want to run it in the IDLE.

##About

This Script uses GrooveShark for the Song Information and Last.fm API for the Album Art. It uses  EyeD3,  JSON, urllib2, os and sys python modules.
Works with Python 2.x Only. Version 2.7.8 recomendded

###To-Do

- <s> Add Capability to Integrate Album Art  
</s>
- Add Functions to remove garbage text from Title to increase support for more MP3 Files

- Create a GUI using PySide

Created By Pradd.
Copyright 2014