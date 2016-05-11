from util import hook

WIDE_MAP = dict((i, i + 0xFEE0) for i in xrange(0x21, 0x7F))
WIDE_MAP[0x20] = 0x3000


def widen(s):
    return unicode(s).translate(WIDE_MAP)

@hook.command
def ft(inp):
    caps = inp.upper()
    future = widen(caps.decode('utf-8')).encode('utf-8')
    return future
