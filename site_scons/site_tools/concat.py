from SCons.Builder import Builder
from SCons.Errors import StopError

from site_scons.site_tools.warnings import ThereCanBeOnlyOne


def concat_generator(source, target, env, for_signature):
    if len(target) != 1:
        raise StopError(ThereCanBeOnlyOne, 'concat only support one target')

    env['CONCAT_BIN'] = 'cat'

    return '$CONCAT_BIN $SOURCE > $TARGET'


def generate(env):
    """ Add builders and construction variables to the Environment. """

    env['BUILDERS']['concat'] = Builder(generator=concat_generator)


def exists(env):
    return env.Detect('cat')
