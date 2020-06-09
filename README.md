# Bython
Takes directory paths as command line arguments and then 
for each directory prints all files not present in any of
the other directories.

```
python3 bython.py folder/1 folder/2 ...
``` 

Assuming you have the following directory layout
```
folder/1
|-- 1.MP4
|-- 2.MP4
|-- 3.MP4

folder/2
|-- 1.MP4
|-- 2.MP4
|-- 4.MP4
```
You will get
```
File 3 is in files/1 but not in files/2
File 4 is in files/2 but not in files/1
```