# Compact Path

[![CircleCI Build Status](https://circleci.com/gh/tupton/compact-path/tree/main.svg?style=svg)](https://circleci.com/gh/tupton/compact-path/tree/main)

Reduce path elements to one character save the last element, like vim buffer names.

``` sh
❯ pwd
/Users/tupton/code/compact_path
❯ compact-path $(pwd)
/U/t/c/compact_path
❯ compact-path "${PWD/#$HOME/~}"
~/c/compact_path
```

Pass the `--trigger` or `-t` option to specify the length at which compaction will
take place. Any paths that are *less* than this length will not be compacted.

``` sh
❯ pwd
/Users/tupton/code/compact_path
❯ compact-path $(pwd) --trigger 35
/Users/tupton/code/compact_path
❯ compact-path $(pwd) -t 10
/U/t/c/compact_path
```

## Installation

`compact-path` is not published to any package index. Install from a repository checkout with `uv tool install`.

```sh
gh repo clone tupton/compact-path # or clone with git
cd compact-path
uv tool install .
```

## Prompt integration

You can use this in your shell prompt.

``` sh
function __compact_path() {
    if hash compact-path 2>/dev/null; then
        compact-path --trigger=20 "${PWD/#$HOME/~}"
    else
        echo "%~"
    fi
}

PROMPT='$(__compact_path) %# '
```

In `zsh`, that would result in a prompt that looks like the following.

``` sh
~/code/compact_path % cd /usr/local/Library/Homebrew/
/u/l/L/Homebrew % cd ~/code/compact_path
~/code/compact_path %
```

See my `zshrc` for the actual [`__compact_path` function][cp] and how I use it [in my prompt][p].

  [cp]: https://github.com/tupton/dotfiles/blob/72661925418a364b08e9de7c2ddcb14a73b3eb16/zsh/zshrc.d/prompt.zsh#L18-L25
  [p]: https://github.com/tupton/dotfiles/blob/72661925418a364b08e9de7c2ddcb14a73b3eb16/zsh/zshrc.d/prompt.zsh#L101
