# Command format:
```
py anl.py {old-file} {new-file} {width}
    {old-file}, {new-file} = Names, including file extensions, of text files to work with
    {width} = Integer specifying target line width.
```
    
# How it works:
This simple utility writes the contents ```old-file```, including any preexisting line breaks, to ```new-file``` with newlines inserted after the space character nearest to     ```width``` on every line whose width exceedes ```width```.
