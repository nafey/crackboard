# Crackboard Sublime Text Plugin

> A Sublime Text plugin for Crackboard

## Introduction

This plugin allows you to connect your crackboard profile with Sublime text and track your work.

To use:
1. Create account on crackboard.dev
2. Copy the session_key for your account
3. Use the Command+Shift+P (or Ctrl+Shift+P) to bring up the command palette and enter *Crackboard: Set Session Key*
4. Paste the session key in the text box and press enter
5. You are good to go.

## Installation


### With Package Control (recommended)

1. Open your command palette and type in : `Package Control: Install Package`
2. Browse the list or search for `Crackboard`
3. Press `Enter` and you're done !


### Manually

1. Go to the Sublime Text packages folder (usually `$HOME/.config/sublime-text/Packages/` or `%AppData%\Sublime Text\Packages\`)
2. Clone this repository there : `git clone https://github.com/nafey/crackboard`
3. Edit the package settings and fill your session key in the "crackboard_session_key" property of the settings file.
4. Save the changes
