# md2html
Simple tool to convert .md markdown files into html for display.
### Requirements
Python  
Python markdown2 module
```
pip install markdown2
```

## Usage (Windows)

Either drag an .md file onto [md2html.py](https://github.com/megarobohobo/md2html/blob/main/md2html.py "md2html.py") or use the included [markdown.reg](https://github.com/megarobohobo/md2html/blob/main/markdown.reg "markdown.reg").  
A table of contents will be generated, if you don't want a TOC, use [md2html_no_toc.py](https://github.com/megarobohobo/md2html/blob/main/md2html_no_toc.py "md2html_no_toc.py").

### Adding/Using a context menu shortcut with [markdown.reg](https://github.com/megarobohobo/md2html/blob/main/markdown.reg "markdown.reg")

1. Move [md2html.py](https://github.com/megarobohobo/md2html/blob/main/md2html.py "md2html.py") to somewhere you don't mind keeping it forever.
2. Edit [markdown.reg](https://github.com/megarobohobo/md2html/blob/main/markdown.reg "markdown.reg") to point to your **pythonw.exe**, and the location of [md2html.py](https://github.com/megarobohobo/md2html/blob/main/md2html.py "md2html.py").
	- Specifically pythonw.exe and **not** python.exe, so it doesn't pop open a terminal window every time it runs , unless you're into that.
3. Run the [markdown.reg](https://github.com/megarobohobo/md2html/blob/main/markdown.reg "markdown.reg") file to add it to the registry.
4. Right click any .md file and select `Convert and view as HTML`.
	- A .html file with the same names as the md file will be created in the same directory, and the .html file will be immediately opened in your browser.
5. ???
6. Profit
