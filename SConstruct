from imp import find_module
from os import getcwd, path

env = Environment()

ROOT_DIR = getcwd()


# Where temporary files, created during build process will be stored.
BUILD_DIR = path.join(ROOT_DIR, 'BUILD')

pybuildtool_dir = find_module('PyBuildTool')[1]

# Let pybuildtool creates rules/builders.
SConscript(path.join(pybuildtool_dir, 'SConscript'),
           exports='env ROOT_DIR BUILD_DIR')
