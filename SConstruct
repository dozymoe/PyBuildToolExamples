from os import getcwd, path

env = Environment()

ROOT_DIR = getcwd()
BUILD_DIR = path.join(ROOT_DIR, 'BUILD')

SConscript('site_scons/SConscript', exports='env ROOT_DIR BUILD_DIR')
