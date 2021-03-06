from compact_path import compact_path

import nose.tools as tools

def test_empty():
    tools.eq_('', compact_path(''))

    tools.eq_(None, compact_path(None))

def test_root():
    tools.eq_('/', compact_path('/'))

def test_absolute():
    tools.eq_('/usr', compact_path('/usr'))

    tools.eq_('/u/local', compact_path('/usr/local'))

    tools.eq_('/u/l/bin', compact_path('/usr/local/bin'))

def test_relative():
    tools.eq_('usr', compact_path('usr'))

    tools.eq_('u/local', compact_path('usr/local'))

def test_home():
    tools.eq_('~', compact_path('~'))

    tools.eq_('~/code', compact_path('~/code'))

    tools.eq_('~/c/compact_path', compact_path('~/code/compact_path'))

def test_max_length():
    path = '/usr/local/bin'
    tools.eq_(path, compact_path(path, len(path)))

    tools.eq_('/u/l/bin', compact_path(path, trigger=1))

def test_trailing_slash():
    tools.eq_('/u/l/bin', compact_path('/usr/local/bin/'))

def test_spaces():
    tools.eq_("/u/l/b in", compact_path("/usr/lo cal/b in"))

    tools.eq_("/u/l/b in", compact_path("/usr/ lo cal/b in"))

    tools.eq_("/u/l/ bin", compact_path("/usr/ lo cal/ bin"))
