# q

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

* github
* google
 * maps
 * weather
 * inbox
* reddit
 * sub
* spotify
* duckduckgo
* stackoverflow
* wikipedia
