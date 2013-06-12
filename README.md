AutoHotkey - Syntax Package for Sublime Text 2/3
==========

AutoHotkey language package for SublimeText including syntax highlighting, comments toggling, autocompletions, build system, and an ahkexec command.

The ahkexec command will run the code in the current buffer by piping it as a temporary string to the AutoHotkey.exe executable. This enables you to run and test AutoHotkey scripts without needing to save them to a file first.

For the build system and ahkexec command, if you have a non-default installation then you will need to set your specific path to AutoHotkey.exe in a file named AutoHotkey.sublime-settings in your User folder. You can open these settings file via the Menu Preferences>Package Settings>AutoHotkey. You should make a copy of "AutoHotkey Settings - Default" at "AutoHotkey Settings - User" since then your settings file in your User folder will not get overwritten when this package updates.

LINKS
----------
http://www.autohotkey.com/board/topic/23575-how-to-run-dynamic-script-through-a-pipe/
