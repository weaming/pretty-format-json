version = '0.2.21'

from signal import signal, SIGPIPE, SIG_DFL

signal(SIGPIPE, SIG_DFL)
