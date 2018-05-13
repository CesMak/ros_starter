# !/usr/bin/python
# !/usr/bin/env python3

import os
import sys

new_name = sys.argv[1]

basedir = os.path.dirname(os.path.realpath(__file__))

dirlist1 = os.listdir(os.getcwd())

matching = [s for s in dirlist1 if "_description" in s]



#print "This dir1 contains: %s"%dirlist1

os.rename(matching[0], new_name+"_description")

inbasedir = basedir+"/"+new_name+"_description"

configdir = inbasedir+"/config"


config_files = os.listdir(configdir)



os.rename(configdir+"/"+config_files[0], configdir+"/"+new_name+"_state_visualize.rviz")


launchdir = inbasedir+"/launch"
launch_files = os.listdir(launchdir)
matchingload = [s for s in launch_files if "load" in s]
matchingdes = [s for s in launch_files if "description" in s]

os.rename(launchdir+"/"+matchingload[0], launchdir+"/"+new_name+"_load.launch")
os.rename(launchdir+"/"+matchingdes[0], launchdir+"/"+new_name+"_description.launch")

meshesdirvis = inbasedir+"/meshes/visual"
meshesdircoll = inbasedir+"/meshes/collision"

visual_files = os.listdir(meshesdirvis)
coll_files = os.listdir(meshesdircoll)

visualdd = [s for s in visual_files if "_visual" in s]
colldd = [s for s in coll_files if "_collision" in s]

os.rename(meshesdirvis+"/"+visualdd[0], meshesdirvis+"/"+new_name+"_visual.stl")
os.rename(meshesdircoll+"/"+colldd[0], meshesdircoll+"/"+new_name+"_collision.stl")


urdfdir = inbasedir+"/urdf"
urdf_files = os.listdir(urdfdir)
matchingurdfgz = [s for s in urdf_files if "gazebo" in s]
matchingurdf = [s for s in urdf_files if "urdf.xacro" in s]
matchingurdfroot = [s for s in urdf_files if "__" in s]

os.rename(urdfdir+"/"+matchingurdfgz[0], urdfdir+"/"+new_name+".gazebo.xacro")
os.rename(urdfdir+"/"+matchingurdf[0], urdfdir+"/"+new_name+".urdf.xacro")
os.rename(urdfdir+"/"+matchingurdfroot[0], urdfdir+"/"+new_name+".xacro")


### Change package name in CMakeLists.txt:
# Read in the file
with open(inbasedir+"/"+'CMakeLists.txt', 'r') as file :
  cmfiledata = file.read()

# Replace the target string
cmfiledata = cmfiledata.replace('project(plate_description)', 'project('+new_name+"_description)")

# Write the file out again
with open(inbasedir+"/"+'CMakeLists.txt', 'w') as file:
  file.write(cmfiledata)


### Change package name in package.xml:
with open(inbasedir+"/"+'package.xml', 'r') as file :
  packfiledata = file.read()

packfiledata = packfiledata.replace('<name>plate_description</name>', '<name>'+new_name+"_description</name>")

packfiledata = packfiledata.replace('<description>Just a plate</description>', '<description>Just a '+new_name+"</description>")

with open(inbasedir+"/"+'package.xml', 'w') as file:
  file.write(packfiledata)

## Change launch files:

with open(launchdir+"/"+new_name+'_description.launch', 'r') as file :
  deslaufiledata = file.read()

deslaufiledata = deslaufiledata.replace('<name>plate_description</name>', '<name>'+new_name+"_description</name>")

deslaufiledata = deslaufiledata.replace('plate_name', new_name+"_name")
deslaufiledata = deslaufiledata.replace('my_plate', 'my_'+new_name)
deslaufiledata = deslaufiledata.replace('plate_description', new_name+"_description")
deslaufiledata = deslaufiledata.replace('plate_state_visualize.rviz', new_name+"_state_visualize.rviz")
deslaufiledata = deslaufiledata.replace('plate.xacro', new_name+".xacro")


with open(launchdir+"/"+new_name+'_description.launch', 'w') as file:
  file.write(deslaufiledata)

## load launch:
with open(launchdir+"/"+new_name+'_load.launch', 'r') as file :
  loadlaufiledata = file.read()

loadlaufiledata = loadlaufiledata.replace('plate_description', new_name+"_description")
loadlaufiledata = loadlaufiledata.replace('plate_name', new_name+"_name")
loadlaufiledata = loadlaufiledata.replace('my_plate', 'my_'+new_name)
loadlaufiledata = loadlaufiledata.replace('plate.xacro', new_name+".xacro")

with open(launchdir+"/"+new_name+'_load.launch', 'w') as file:
  file.write(loadlaufiledata)



## change urdf:
with open(urdfdir+"/"+new_name+'.gazebo.xacro', 'r') as file :
  gzdata = file.read()

gzdata = gzdata.replace('plate_link', new_name+"_link")

with open(urdfdir+"/"+new_name+'.gazebo.xacro', 'w') as file:
  file.write(gzdata)


with open(urdfdir+"/"+new_name+'.urdf.xacro', 'r') as file :
  urdfdata = file.read()

urdfdata = urdfdata.replace('plate', new_name)

with open(urdfdir+"/"+new_name+'.urdf.xacro', 'w') as file:
  file.write(urdfdata)


print urdfdir+"/"+new_name+'.xacro'

with open(urdfdir+"/"+new_name+'.xacro', 'r') as file :
  data = file.read()

data = data.replace('plate', new_name)

with open(urdfdir+"/"+new_name+'.xacro', 'w') as file:
  file.write(data)

print "Finished Clearly! :) Success!"
