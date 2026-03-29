import shutil
import subprocess
import glob
import os
import sys
from pathlib import Path
from datetime import datetime
from constants import constants

inputs = [
    "src/german_industries.pnml",
    "src/cargo_subtype_display.pnml",
    "src/default_graphics.pnml",
    "src/electricity.pnml",
    "src/location_checks.pnml",
    "src/production_rules.pnml",
]

cargos = sorted(glob.glob("src/cargos/*.pnml"))
inputs.extend(cargos)
industries = sorted(glob.glob("src/industries/*.pnml"))
inputs.extend(industries)

# check the ids from constants.py for duplicates, these can cause hard to track bugs
industry_ids = {}
industry_tile_ids = {}
for key, value in constants.items():
    if key.startswith("INDUSTRY_ID"):
        industry_ids[key] = value
    if key.startswith("INDUSTRY_TILE_ID"):
        industry_tile_ids[key] = value

reverse_dict = {}
for key, value in industry_ids.items():
    reverse_dict.setdefault(value, []).append(key)
duplicates = {value: keys for value, keys in reverse_dict.items() if len(keys) > 1}
if len(duplicates) > 0:
    print("ERROR, industry ids contain duplicates")
    print(duplicates)
    sys.exit(1)
    
reverse_dict = {}
for key, value in industry_tile_ids.items():
    reverse_dict.setdefault(value, []).append(key)
duplicates = {value: keys for value, keys in reverse_dict.items() if len(keys) > 1}
if len(duplicates) > 0:
    print("ERROR, industry tile ids contain duplicates")
    print(duplicates)
    sys.exit(1)

# clean the build dir, we'll recreate all files
shutil.rmtree('build',ignore_errors=True)
Path("build").mkdir()

# create custom tags including version + time/date
# on github the version number is passed in via command line, 
# if no such argument is given, a placeholder is used
now = datetime.now()
dt = now.strftime("%Y-%m-%d %H:%M:%S")
version = "local build " + dt
if len(sys.argv) > 1:
    version = sys.argv[1]
version = "VERSION:"+version

with open('custom_tags.txt', 'w') as file:
  file.write(version)
  file.write("\nTITLE :GIST - German Industries Set")

# create the actual nml file by concatenating all inputs
with open('build/german_industries.nml','wb') as output:
    for f in inputs:
        with open (f, 'rb') as fd:
            shutil.copyfileobj(fd, output)
            output.write(b"\n")
            
# replace the defined constants
# Read in the file
with open('build/german_industries.nml', 'r') as file:
  filedata = file.read()

# Replace the target string
for key,value in constants.items():
    filedata = filedata.replace(key, value)

# Write the file out again
with open('build/german_industries.nml', 'w') as file:
  file.write(filedata)

# call nmlc to create the grf output
subprocess.run(["nmlc", "-c", "--grf", "build/german_industries.grf","build/german_industries.nml"])

dt = now.strftime("%Y-%m-%d_%H-%M-%S")
grfdate="build/german_industries_"+dt+".grf"
shutil.copyfile('build/german_industries.grf', grfdate)
os.remove("custom_tags.txt")