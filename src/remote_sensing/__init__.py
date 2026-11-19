"""remote-sensing.

metadata schema for NASA and NOAA satellite data
"""

try:
    from remote_sensing._version import __version__, __version_tuple__
except ImportError:  # pragma: no cover
    __version__ = "0.0.0"
    __version_tuple__ = (0, 0, 0)
