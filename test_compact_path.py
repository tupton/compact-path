from compact_path import compact_path

def test_empty():
    assert '' == compact_path('')

    assert None == compact_path(None)

def test_root():
    assert '/' == compact_path('/')

def test_absolute():
    assert '/usr' == compact_path('/usr')

    assert '/u/local' == compact_path('/usr/local')

    assert '/u/l/bin' == compact_path('/usr/local/bin')

def test_relative():
    assert 'usr' == compact_path('usr')

    assert 'u/local' == compact_path('usr/local')

def test_home():
    assert '~' == compact_path('~')

    assert '~/code' == compact_path('~/code')

    assert '~/c/compact_path' == compact_path('~/code/compact_path')

def test_max_length():
    path = '/usr/local/bin'
    assert path == compact_path(path, len(path))

    assert '/u/l/bin' == compact_path(path, trigger=1)

def test_trailing_slash():
    assert '/u/l/bin' == compact_path('/usr/local/bin/')

def test_spaces():
    assert "/u/l/b in" == compact_path("/usr/lo cal/b in")

    assert "/u/l/b in" == compact_path("/usr/ lo cal/b in")

    assert "/u/l/ bin" == compact_path("/usr/ lo cal/ bin")
