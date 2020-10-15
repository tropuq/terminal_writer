# Terminal writer

It's a library allowing multi-terminal scripting and creating scripts for applications with command-line interfaces. Allows to create easy ad-hoc scripts.

# Usage

The package consists of one module terminal_writer and TerminalWriter class within it.

TerminalWriter class constructor accepts a list of ids of terminals (names of terminals' character devices from `/dev/pts` directory or `/dev` if `extended_format=True`). After constructing, one can interact with these terminals using write and writeln methods allowing executing some commands. To execute a command root privileges are needed.

To read current terminal's path to the character device use `tty` command.

## Example:
```python
import time
from terminal_writer import TerminalWriter

# use /dev/pts/2 and /dev/pts/3 terminals
term = TerminalWriter("2,3")
for i in range(10):
	# write 'ls' to terminal 0 from specified in constructor list (/dev/pts/2)
	term.writeln(0, "ls")
	time.sleep(1)
```
