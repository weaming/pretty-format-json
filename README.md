# Pretty Format JSON

Pretty print json contains python style coments, string literal.

```
pip3 install pretty-format-json
```

## Binaries

* `pretty_format_json`: parse NodeJS style, Python style text to JSON
* `yaml_json`: Convert between Yaml and JSON

## Use it in VIM

Add `noremap <a-j> :%!pretty_format_json<CR>` (or your key binding) to your config file.

```
noremap <a-j> :%!pretty_format_json<CR>
noremap <a-k> :%!yaml_json<CR>
noremap <a-c> :%!csv_json<CR>
```

When you open a blank buffer, paste the text copied from somewhere into,
then use `Alt+j` to convert to JSON,
use `Alt-k` to convert to Yaml and back to JSON.
