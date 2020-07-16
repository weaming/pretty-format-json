version = '0.2.20'

from signal import signal, SIGPIPE, SIG_DFL

signal(SIGPIPE, SIG_DFL)
