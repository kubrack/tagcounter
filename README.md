# Overview
```
	tagcounter -h 					# get usage
	tagcounter -g http://a.tim.ua 	# count tags in http://a.tim.ua and print to STDOUT in parsable format
	tagcounter -v http://a.tim.ua 	# get previously fetched info about tags from DB and print to STDOUT in parsable format
	tagcounter -v a 				# the same by alias
	tagcounter 						# run GUI
```

	Tool for count tags by URI.
	With command line args, output the results in parsable format:
```
	uri|db <URI> {<tag1>: <number>[, <tag2>: <number>] ... }
```
		1-st fiels is source - 'db' or 'uri'
		2-hd filed is requested URI
		3-d fiels is result in '{}'

	The results saved locally in a sqlite base and could be fetched later via '-v' arg (or GUI).
	
	Aliases could be defined in the YAML config file which passed in '--cfg' parameter (default ./tagcounter.yaml). Example:
```
	$ cat ./tagcounter.yaml
	a: http://a.tim.ua
	ggl: http://google.com
	epam: http://epam.com
```
	then it could be called by alias instead of a full URL:
```
	tagcounter -g a epam ggl
	tagcounter -v a epam ggl
```


# Installation
```
	pip install https://github.com/kubrack/tagcounter
```

# testing
```
	git clone https://github.com/kubrack/tagcounter
	cd tagcounter
	pip install .
	py.test
```

# Usage
```
usage: tagcounter [-h] [--get URI|alias [URI|alias ...]]
                  [--view URI|alias [URI|alias ...]] [--cfg [cfgfile]]
                  [--log [logile]]

Tool for tags count.

optional arguments:
  -h, --help            show this help message and exit
  --get URI|alias [URI|alias ...], -g URI|alias [URI|alias ...]
                        URI or alias to tags counting
  --view URI|alias [URI|alias ...], -v URI|alias [URI|alias ...]
                        URI or alias to get saved from DB
  --cfg [cfgfile], -c [cfgfile]
                        YAML config file, default "./tagcounter.yaml"
  --log [logile], -l [logile]
                        logfile, default "tagcounter.log"
```

# Example
```
	$ tagcounter -v http://a.tim.ua -g http://epam.com http://google.com
	uri http://epam.com {'html': 1, 'head': 1, 'meta': 17, 'link': 12, 'script': 21, 'title': 1, 'body': 1, 'a': 316, 'img': 74, 'div': 461, 'noscript': 1, 'iframe': 1, 'header': 1, 'nav': 5, 'ul': 74, 'li': 257, 'span': 122, 'button': 37, 'strong': 21, 'p': 122, 'svg': 38, 'use': 38, 'form': 1, 'label': 1, 'input': 1, 'h3': 15, 'main': 1, 'video': 1, 'h2': 33, 'section': 10, 'br': 226, 'time': 1, 'hr': 2, 'b': 2, 'h5': 82, 'sup': 5, 'footer': 1}
	uri http://google.com {'html': 2, 'head': 2, 'meta': 19, 'link': 12, 'script': 26, 'title': 2, 'body': 2, 'a': 334, 'img': 76, 'div': 475, 'noscript': 1, 'iframe': 1, 'header': 1, 'nav': 5, 'ul': 74, 'li': 257, 'span': 130, 'button': 37, 'strong': 21, 'p': 123, 'svg': 38, 'use': 38, 'form': 2, 'label': 1, 'input': 10, 'h3': 15, 'main': 1, 'video': 1, 'h2': 33, 'section': 10, 'br': 231, 'time': 1, 'hr': 2, 'b': 3, 'h5': 82, 'sup': 5, 'footer': 1, 'style': 3, 'nobr': 2, 'u': 1, 'center': 1, 'table': 1, 'tr': 1, 'td': 3}
	db http://a.tim.ua {'html': 1, 'head': 1, 'meta': 4, 'title': 1, 'style': 1, 'body': 1, 'table': 1, 'tbody': 1, 'tr': 3, 'td': 3, 'h3': 1, 'b': 7, 'a': 1, 'p': 18, 'br': 4, 'ul': 8, 'li': 27}
```
