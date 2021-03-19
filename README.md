## README

A promotional video on what this is:
https://www.youtube.com/watch?v=Bk59xnPL1Ao

###### **what is this**
This is a terminal program that fixes inputted sentences to the best they can be. It saves time by doing that first lookover to catch all the small spelling errors as well as well as grammar errors as well. Simply paste in the desired text, and `quickfix` will quickly and efficiently fix up your document. `Quickfix` has not been extensivly tested, so while it is in its initial stages, `quickfix` will have a feedback option embeded directly into the program for you to report bugs, recommend features, or just show your appreciation. _pls dont spam :)_ Alternatively you are able to leave [editorial requests within GitHub](https://github.com/there-are-higher-beings/quickfix/pulls) for everyone to see and be aware of.

###### **how to install**

[Click here](https://github.com/there-are-higher-beings/quickfix/archive/main.zip) to download the zip file. Alternitivly you can click on the `[⬇CODE]` in green. Once it is downloaded, follow the platform specific instructions below to install `quickfix`.

***for pc***

simply double click on `quickfix.exe` for it to run

***for mac***

for mac we need to go to `quickfix`'s directory, change the name of the program from `quickfix.py` to `quickfix.command`
and then turn it into an executable by typing in `chmod +x quickfix.command` in the terminal command prompt

heres how to do that:
1. open up a terminal window, and keep it open beside these instructions
2. open up a finder window that contains QUICKFIX
3. go to the terminal window and type in [cd ] (without the square brackets but with the space)
4. from finder, drag quickfix.py into the terminal window
5. click the right-arrow key to deselect the path and delete [quickfix.py] from the terminal line

	at this point the terminal command line should look like:
		cd /Users/YOURNAME/FOLDER/FOLDER 

	(idk how many folders there are on your pc, it should be different for everyone)


6. if the terminal line is as above, press `return` (or enter)

7. paste in:
	>`md quickfix.py quickfix.command`

	and press `return` (or enter)

8. paste in:
	>`chmod +x quickfix.command`

	and press `return` (or enter)

you are then free to double click on `quickfix.command` whenever you would like to use it


###### **how to use `quickfix`**

1. launch
2. paste in the text you would like to fix
3. choose what you want to do with the text from the list of options
4. copy the outputted text
5. complete finishing steps as listed in the command prompt

###### **how it works**

`Quickfix` was developed in python to work in inside of Terminal *(command prompt on pc)* for user interaction. It takes advatage of different string manipulation funcions that come with Python, as well as a [spellchecker](https://pypi.org/project/pyspellchecker/) and a [grammar checker](https://predictivehacks.com/languagetool-grammar-and-spell-checker-in-python/).

###### **to do**

- [x] create 1.0.0
- [x] get `quickfix` operational as a `.py` file
- [x] create a `.exe` file that works on all Windows platforms
- [x] create a `.command` file that works on all Mac platforms
- [x] make the README readable
- [ ] add a grammar module
