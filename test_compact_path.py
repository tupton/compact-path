from compact_path import compact_path

import nose.tools as tools

def test_empty():
    tools.eq_(None, compact_path(""))

    tools.eq_(None, compact_path(None))

def test_absolute():
    tools.eq_("/usr", compact_path("/usr"))

    tools.eq_("/u/local", compact_path("/usr/local"))

    tools.eq_("/u/l/bin", compact_path("/usr/local/bin"))

def test_relative():
    tools.eq_("usr", compact_path("usr"))

    tools.eq_("u/local", compact_path("usr/local"))

def test_home():
    tools.eq_("~", compact_path("~"))

    tools.eq_("~/code", compact_path("~/code"))

    tools.eq_("~/c/compact_path", compact_path("~/code/compact_path"))

def test_max_length():
    path = "/usr/local/bin"
    tools.eq_(path, compact_path(path, len(path)))

    tools.eq_('/u/l/bin', compact_path(path, trigger=1))
