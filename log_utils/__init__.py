import logging
import os
import sys
import traceback
import io


class LoggerFactory:
    @classmethod
    def set_logger(cls, self, name):
        if hasattr(self, 'logger'):
            return getattr(self, 'logger')
        logger = logging.getLogger(name)
        logger.location = "<*****>"
        setattr(self, 'logger', logger)


class LogMixin:
    def debug(self, msg):
        self.logger.debug(msg, extra={"location": self.logger.location}, stacklevel=2)

    def info(self, msg):
        self.logger.info(msg, extra={"location": self.logger.location}, stacklevel=2)

    def warning(self, msg):
        self.logger.warning(msg, extra={"location": self.logger.location}, stacklevel=2)

    def error(self, msg):
        self.logger.error(msg, extra={"location": self.logger.location}, exc_info=1, stacklevel=2)

    def critical(self, msg):
        self.logger.critical(msg, extra={"location": self.logger.location}, stacklevel=2)


if hasattr(sys, '_getframe'):
    currentframe = lambda: sys._getframe(1)
else:  # pragma: no cover
    def currentframe():
        """Return the frame object for the caller's stack frame."""
        try:
            raise Exception
        except Exception:
            return sys.exc_info()[2].tb_frame.f_back


def hold_function():
    pass


_srcfile = os.path.normcase(hold_function.__code__.co_filename)


def findCaller(stack_info=False, stacklevel=1):
    """
    Find the stack frame of the caller so that we can note the source
    file name, line number and function name.
    """
    f = currentframe()
    # On some versions of IronPython, currentframe() returns None if
    # IronPython isn't run with -X:Frames.
    if f is not None:
        f = f.f_back
    orig_f = f
    while f and stacklevel > 1:
        f = f.f_back
        stacklevel -= 1
    if not f:
        f = orig_f
    rv = "(unknown file)", 0, "(unknown function)", None
    while hasattr(f, "f_code"):
        co = f.f_code
        filename = os.path.normcase(co.co_filename)
        if filename == _srcfile:
            f = f.f_back
            continue
        sinfo = None
        if stack_info:
            sio = io.StringIO()
            sio.write('Stack (most recent call last):\n')
            traceback.print_stack(f, file=sio)
            sinfo = sio.getvalue()
            if sinfo[-1] == '\n':
                sinfo = sinfo[:-1]
            sio.close()
        rv = (co.co_filename, f.f_lineno, co.co_name, sinfo)
        break
    return rv
