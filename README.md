# q
[![Build Status](https://travis-ci.org/borzecki/q.svg)](https://travis-ci.org/borzecki/q)
[![PyPI version](https://badge.fury.io/py/quicksearch.svg)](https://badge.fury.io/py/quicksearch)

Quick search command tool for your terminal.

# Usage

```
Usage: q [OPTIONS] QUERY...

  Quick search command tool for your terminal

Options:
  -e, --search-engine TEXT  Search engine.
  -o, --search-option TEXT  Optional search module.
  -l, --list-engines        List all search engines with options.
  --help                    Show this message and exit.
```

# Examples

Search for location on google maps
```
q -o maps 221b Baker Street, London
```

Look up github
```
q -e github django-rest-framework
```

Check what's hot on spotify
```
q -e spotify Walking On Sunshine
```

And many more!

# Currently supported engines

 * 500px
 * 8tracks
 * amazon
 * archpkg
 * archwiki
 * arstechnica
 * arxiv
 * atmospherejs
 * aur
 * baidu
 * bandcamp
 * bgr
 * bing
 * buzzfeed
 * cnn
 * codepen
 * coursera
 * cplusplus
 * crunchyroll
 * debianpkg
 * digg
 * diigo
 * dockerhub
 * dribbble
 * duckduckgo
 * dumpert
 * engadget
 * facebook
  * people
  * pages
 * flickr
 * flipkart
 * foursquare
 * gist
 * github
 * gmail
 * go
 * godoc
 * google
  * maps
  * weather
  * inbox
 * googledocs
 * googleplus
 * hackernews
 * ietf
 * ifttt
 * imdb
 * imgur
 * inbox
 * instagram
 * kickasstorrents
 * libgen
 * linkedin
 * lmgtfy
 * macports
 * mdn
 * medium
 * metacpan
 * msdn
 * naver
 * netflix
 * nhaccuatui
 * npm
 * npmsearch
 * npr
 * nvd
 * overstock
 * packagist
 * phandroid
 * php
 * pinterest
 * python
 * quora
 * reddit
  * sub
 * rottentomatoes
 * rubygems
 * soundcloud
 * spotify
 * stackoverflow
 * steam
 * taobao
 * thepiratebay
 * theregister
 * torrentz
 * twitchtv
 * twitter
 * unity3d
 * upcloud
 * vimeo
 * wikipedia
 * wolframalpha
 * yahoo
 * yandex
 * youtube

# Example aliases :sparkles:

```bash
alias qd='q -e duckduckgo'
alias qr='q -e reddit'
alias qm='q -o maps'
```

# Bash completion :bomb:

In order to use autocomplete functionality simply add this line to your ``.bash_profile`` or ``.bashrc`` file

```bash
source ~/path/to/q/complete/q-complete.sh
```
