PyBuildTool examples
====================

Summary
-------

This is example implementation of [PyBuildTool][1]

The file users need to focus on is just the SConsfile.yml and
Sconsfile.production.yml

If you want to build your own tools/extensions, take a look at the
python modules inside site_scons/site_tools.


Instruction
-----------

If you haven't notice, there's a requirements.txt file in the root
directory, this example is meant to be a virtualenv (a python sandbox).

There's also a package.json, which will install jshint, which actually
won't be needed, but I kept it for fun, haha.

So first you need to create virtualenv on top of this example directory.
You'd need python2, since [SCons][2] which this project is build on top
of, does not support python3, currently.

Next, activate the virtualenv and install SCons with
`pip install --egg SCons`. That egg option is necessary.

Install the requirements with `pip install -r requirements.txt`.

This will install **PyYAML** (required to read the build configuration file,
SConsfile.yml and SConsfile.production.yml), and **yuicompressor**,
a required python module by SCons tool `cssmin` and `jsmin`. These
tools' module can be found in site_scons/site_tools named **cssmin.py**
and **jsmin.py**, the file names are the same as the tool names.

The current `copy` and `concat` SCons tools doesn't support Windows OS,
yet, they uses **cp** and **cat** binary found in the system, tipical of
\*NIX installation.
SCons itself support Windows, there're builtin functions that can be used
to replace those binaries, I'll try to fix them later.

Oh, Scons tools is equivalent to grunt.js plugins, they're extensions,
sort of.

And now for the real thing, provided that you have **scons** in the **bin/**
directory, run the following: `scons` and `scons --stage=production`.

`scons` read configuration from **SConsfile.yml** in the root directory,
it is equivalent to `scons --stage=default`, the build process' temporary
files can be found in **BUILD/default**.
Likewise with `scons --stage=production`, except this one reads from
**SConsfile.production.yml**, you can replace "production" with any staging
workflow name you can think of.

You can build for specific targets, we have `scons concat` to process files
that will be build by the tool `concat`. Or more specifically
`scons concat:group_main_css`, to _concat_ just the files under that group.

And, that's it.


PS: Fun fact, `scons` is actually reading build configuration in **SConsfile.py**,
    we support two file types now, py and yml, with py as the default because
    its content may be dynamic.


[1]: http://github.com/dozymoe/PyBuildTool
[2]: http://www.scons.org
