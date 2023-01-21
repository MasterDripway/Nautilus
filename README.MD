## HOW TO USE
# Step 1: link to github repo in toolset.ns
open `toolset.ns` and change the default tool to specific directory.

Keep in mind the directory can have an `installer.ns` file within to run os-specific commands on installation
For example creating a venv and installing dependencies

# Step 2: Versioning
Be sure to add a `version.txt` on the base directory to allow Nautilus to update your software

The first line must contain the version
The second line is the raw.github.com address of `version.txt`
Lastly, the third line must have the repository address