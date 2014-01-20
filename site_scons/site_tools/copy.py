from SCons.Builder import Builder
from SCons.Errors import StopError

from site_scons.site_tools.warnings import ThereCanBeOnlyOne


def copy_generator(source, target, env, for_signature):
    if len(target) != 1 or len(source) != 1:
        raise StopError(ThereCanBeOnlyOne,
                        'copy only support one target and one source')

    env['COPY_BIN'] = 'cp'

    return '$COPY_BIN $SOURCE $TARGET'


def generate(env):
    """ Add builders and construction variables to the Environment. """

    env['BUILDERS']['copy'] = Builder(generator=copy_generator)


def exists(env):
    return env.Detect('cp')
