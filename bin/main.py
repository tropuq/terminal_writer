import time
import sys
from terminal_writer import TerminalWriter

term = TerminalWriter(sys.argv[1])
for i in range(10):
	term.writeln(0, "ls")
	time.sleep(1)
