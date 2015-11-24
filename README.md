# SublimeAutoHotkey - Syntax Package for Sublime Text 2/3
AutoHotkey AHK language package for SublimeText including syntax highlighting, comments toggling, auto-completions, build system definitions, commands for ahkrun, ahkcompile, ahkrunpiped.

## Package Installation
* Manual method: Download ZIP from github. Extract the files to [Sublime_Data_Dir](http://docs.sublimetext.info/en/latest/basic_concepts.html#the-data-directory)\Packages\AutoHotkey
* Automatic method: Install 'AutoHotkey' from [Package Control](http://packagecontrol.io).

## Key Bindings
If you have the default Sublime keybindings intact, then:
* <kbd>Ctrl+B</kbd> will run the current file (with AutoHotkey.exe)
* <kbd>Ctrl+Shift+B</kbd> will compile the current file (with Ahk2Exe.exe)
* <kbd>Ctrl+Alt+H</kbd> will open a popup help for the keyword under the cursor.
* <kbd>F1</kbd> will show the help file page for the selected AutoHotkey command or keyword. If nothing is selected, the command name will be extracted from the beginning of the current line.

## Advanced Configuration
For the build system and ahkrun, ahkrunpiped, and ahkcompile commands, if you have a non-default installation then you will need to set your specific path to AutoHotkey.exe and Ahk2Exe.exe in a file named AutoHotkey.sublime-settings in your User folder. You can access these settings file from the Menu `Preferences > Package Settings > AutoHotkey`. You should make a copy of `AutoHotkey Settings - Default` at `AutoHotkey Settings - User` and modify there since then any settings defined in your User folder will take precedence and the package can still update itself without overwriting your custom settings.

## ahkrunpiped
The ahkrunpiped command will allow you to run your code as a piped text string to AutoHotkey (this allows you to run snippets of code without having to save them to a file):
* If text is selected - ahkrunpiped will pipe and run the selected text only.
* If no text is selected - ahkrunpiped will pipe and run the entire contents of the current document.

## ahkpopuphelp
The ahkpopuphelp command shows a popup when it is called while the cursor (i.e. caret) is on a command, function or directive. Its default key binding is <kbd>Ctrl+Alt+H</kbd>. This feature works only in Sublime Text builds 3070 and later. For prior versions, a message is shown in the Console stating this fact.

## Goto-documentation Integration
SublimeAutoHotkey provides an ``ahkgotodocs`` command. This is mapped to <kbd>F1</kbd> by default.

Alternatively, follow these [instructions](http://www.autohotkey.com/board/topic/46447-sublime-text-editor-very-nice/page-3#entry540187) on how to configure goto-documentation plugin for AutoHotkey using [sublime-text-2-goto-documentation](#https://github.com/kemayo/sublime-text-2-goto-documentation).

## Credits
* S0und: http://www.autohotkey.com/board/topic/46447-sublime-text-editor-very-nice/page-2#entry529723
* Misc: http://www.sublimetext.com/forum/viewtopic.php?f=2&t=4008
* Misc: http://www.autohotkey.com/board/topic/44924-yatmb4ahk-yet-another-textmate-bundle-for-ahk/
* ahkrunpiped, Coco: https://gist.github.com/cocobelgica/6296475
* ahkrunpiped, greycode: https://gist.github.com/grey-code/4728413
* ahkrunpiped, Lexikos: http://www.autohotkey.com/board/topic/23575-how-to-run-dynamic-script-through-a-pipe/
* gotodocs, Rajat: https://www.autohotkey.com/docs/scripts/ContextSensitiveHelp.htm
