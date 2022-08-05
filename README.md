<h1>Command format:</h1>

```py anl.py {old-file} {new-file} {width}
    {old-file}, {new-file} = Names, including extensions, of text files to work with
    {width} = Integer specifying target line width.</p>```
    
<h1>How it works:</h1>
<p>This simple utility writes the contents {old-file}, including any preexisting line breaks, to {new-file} with newlines inserted at the space character nearest to     {width} on every line whose width exceedes {width}.</p>
