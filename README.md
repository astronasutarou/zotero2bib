# Zotero2BIB
This provides a Python script to convert a `.bib` file exported by __Zotero__
into a more TeX-friendly `.bib` file.

The `.bib` file directly exported by __Zotero__ usually contains non-ascii
characters, especially in the `author` entry. This converts such characters
into a TeX-friendly format: &Aacute; is converted into `{\'A}` and &alpha; is
converted into `${\alpha}$`.


## How to Install
Create a symbolic link in `/usr/local/bin/`.

~~~sh
sudo ln -s ${PWD}/zotero2bib.py /usr/local/bin/zotero2bib
~~~


## Usage
`zotero2bib` requires two arguments: The first argument is the name of the
original `.bib` file exported by __Zotero__; The second argument is the name
of the converted `.bib` file.

~~~sh
zotero2bib source.bib converted.bib
~~~
