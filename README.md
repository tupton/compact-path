# Compact Path

[![CircleCI Build Status](https://circleci.com/gh/tupton/compact-path/tree/master.svg?style=svg)](https://circleci.com/gh/tupton/compact-path/tree/master)

Reduce path elements to one character save the last element, like vim buffer names.

``` sh
❯ pwd
/Users/tupton/code/compact_path
❯ python compact_path.py $(pwd)
/U/t/c/compact_path
❯ python compact_path.py $(pwd | sed "s:$HOME:~:")
~/c/compact_path
```

Pass the `--trigger` or `-t` option to specify the length at which compaction will
take place. Any paths that are *less* than this length will not be compacted.

``` sh
❯ pwd
/Users/tupton/code/compact_path
❯ python compact_path.py $(pwd) --trigger 35
/Users/tupton/code/compact_path
❯ python compact_path.py $(pwd) -t 10
/U/t/c/compact_path
```

You can use this in your shell prompt.

``` sh
function compact_path() {
    local cp="/usr/local/bin/compact_path"
    if [[ -e "$cp" ]]; then
        echo $("$cp" "$1" --trigger 20)
    else
        echo "$1"
    fi
}

PROMPT='$(compact_path "${PWD/#$HOME/~}") %# '
```

In `zsh`, that would result in a prompt that looks like the following.

``` sh
~/code/compact_path % cd /usr/local/Library/Homebrew/
/u/l/L/Homebrew % cd ~/code/compact_path
~/code/compact_path %
```

See my `zshrc` for the actual [`compact_path` function][cp] and how I use it [in my prompt][p].

  [cp]: https://github.com/tupton/dotfiles/blob/656350a5a060ec5cf162fe02f6c8f3e3cdebf3d4/zsh/zshrc.d/prompt.zsh#L18-L25
  [p]: https://github.com/tupton/dotfiles/blob/656350a5a060ec5cf162fe02f6c8f3e3cdebf3d4/zsh/zshrc.d/prompt.zsh#L101
