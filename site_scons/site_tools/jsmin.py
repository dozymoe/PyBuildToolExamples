from SCons.Builder import Builder
from SCons.Errors import StopError

from site_scons.site_tools.warnings import ThereCanBeOnlyOne


def jsmin_generator(source, target, env, for_signature):
    if len(target) != 1:
        raise StopError(ThereCanBeOnlyOne, 'jsmin only support one target')

    env['JSMIN_BIN'] = 'yuicompressor'

    return '$JSMIN_BIN -o "$TARGET" $SOURCE'


def generate(env):
    """ Add builders and construction variables to the Environment. """

    env['BUILDERS']['jsmin'] = Builder(generator=jsmin_generator,
                                        src_suffix='.js', suffix='.js')


def exists(env):
    return env.Detect('yuicompressor')
