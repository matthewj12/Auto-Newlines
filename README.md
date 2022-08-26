# UPDATE
If you somehow managed to haplessly stumble upon this repo, the `fmt` command in Linux is what you're looking for. Also, I now realize the stupidity of creating an interpreted script for a command line utility rather than a compiled one that can more naturally make use of environment variables. I may convert this to C++ in the future just for the heck of it...

# Command format:
```
py anl.py {old-file} {new-file} {width}
    {old-file}, {new-file} = Names, including file extensions, of text files to work with
    {width} = Integer specifying target line width.
```
    
# How it works:
This simple utility writes the contents ```old-file```, including any preexisting line breaks, to ```new-file``` with newlines inserted after the space character nearest to     ```width``` on every line whose width exceedes ```width```.
