# using pdb to debug


use:

`import pdb; pdb.set_trace()`

- **n** execute next line
- c complete execution
- l list 3 lines before and after current line
- s step (into function call)
- b show all breakpoints
- b[int]  set breakpoint at line number
- b [func] break at function name
- cl clear all breakpoints
- p(var) print the value var

debugger commands: https://docs.python.org/3/library/pdb.html#debugger-commands