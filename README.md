# 5eScripts
Helper scripts for a project.
All files that are needed for the scripts to run are included. All Output for the given scripts is collected in the `/Scripts/Example Output/` folder.

## MetaIni.py
Opens a simple GUI to fill out all meta information that is needed for the json file. Creates `jsonFile.json` with the correct json syntax and all the entered meta info.

## TableFixing.py
Takes a list of rows from inside `TableData.txt` and adds tags and transforms them to json syntax. Outputs the new table entries into `FixedTableData.txt`

## TextSplitting.py and TextEditing.py
Takes `Textfile.txt` with messy text inside, splits it in multiple files if needed and fixes the formatting. Creates multiple files, depending on how often a split occurs, starting with `Monster0`, counting up and writing the formatted  text in each.
