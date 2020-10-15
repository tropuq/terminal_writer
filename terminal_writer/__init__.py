import os, fcntl, termios

class TerminalWriter:
	def __init__(self, pt_ids_str, extended_format=False):
		pt_ids = pt_ids_str.split(",")
		prefix = "/dev/" if extended_format else "/dev/pts/"
		self.fds = [os.open(prefix + pt_id, os.O_RDWR) for pt_id in pt_ids]

	def __del__(self):
		for fd in self.fds:
			os.close(fd)

	def write(self, tid, data):
		for c in data:
			fcntl.ioctl(self.fds[tid], termios.TIOCSTI, c)

	def writeln(self, tid, data):
		self.write(tid, data + "\n")
