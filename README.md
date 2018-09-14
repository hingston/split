# Split Files
Split large file into a number of smaller files with a given number of lines.
### Usage
`$ python split.py [-h] [-s SUFFIX] [-e ENCODING] n path file`
###### positional arguments:
```
  n                     max number of lines per file
  path                  path of file
  file                  name of file to split
```
###### optional arguments:
```
  -h, --help            show this help message and exit
  -s SUFFIX, --suffix SUFFIX
                        suffix, default='part'
  -e ENCODING, --encoding ENCODING
                        encoding, default='utf8'
```