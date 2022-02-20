from __future__ import annotations

import fnmatch
import os
import posixpath
import re

from pathlib import PurePath
from urllib.parse import quote_from_bytes


class _KeyChainFlavour(object):
    sep = "/"
    altsep = ""
    exp = "~"
    here = "."
    has_drv = False
    pathmod = posixpath

    is_supported = (os.name != "nt")

    def __init__(self):
        self.join = self.sep.join

    def parse_parts(self, parts):
        raise NotImplementedError

    def join_parsed_parts(self, drv, root, parts, drv2, root2, parts2):
        raise NotImplementedError

    def splitroot(self, path: str, sep: str = sep) -> tuple[str, str, str]:
        """
        Return ``tuple(drv, root, part)`` where ``drv=""``.

        In a KeyChain there are no drives so ``drv`` is always ``""``.

        ``root``, if present, comes from the prefix of ``path`` and can be either ``/`` or a ``~(name|op|num)?``
        expansion.

        If ``path`` starts with ``"/"`` then ``root="/"`` and ``part`` becomes ``path[1:]``.

        If ``path`` starts with the ``"~"`` expansion then ``root`` will be ``~(name|op|num)?``. ``name`` is of the
        form ``([a-z_][a-z0-9_]*)?`` where ``name=""`` implies the *home link* otherwise ``name`` refers to a link
        named ``name``. ``op`` can be ``+`` or ``-`` and refer to the *current link* or the *previous link*,
        respectively. ``num`` is of the form ``[0-9]+`` and represents an index to an item in the *current link*. In
        any of these cases ``root`` consumes all the characters up to the first ``"/"`` and ``part`` will be all the
        remaining characters after the first ``"/"``.

        Otherwise, ``root=""`` and ``part=path``.

        Args:
            path: ``str``
            sep: Will always be ``"/"``. If set to any other value then :class:`exception.ValueError` will be raised.

        Returns:
            ``tuple("", root, part)``

        Raises:
            :class:`exception.TypeError`: If ``part`` or ``sep`` are not of type ``str``.
            :class:`exception.ValueError`: If ``sep != "/"`` or if an expansion is invalid.

        """
        if not isinstance(path, str):
            raise TypeError(f"path: type str required (got type {type(path)})")
        if not isinstance(sep, str):
            raise TypeError(f"sep: type str required (got type {type(sep)})")
        if sep != "/":
            raise ValueError(f'sep: invalid "{sep}" sep character (must be "/")')
        path = re.sub(r'//+', '/', str(path))
        sep = str(sep)
        if path.startswith(sep):
            return "", sep, path.lstrip(sep)
        elif path.startswith(self.here):
            dots, _, part = path.partition(sep)
            if not (ms := re.match(r'(\.(\.+)?)$', dots)):
                raise ValueError(f'path: invalid "." dot path "{dots}"')
            if ms.group(2):
                part = f"{dots}{sep}{part}"
            return "", "", part
        elif path.startswith(self.exp):
            name, _, part = path.partition(sep)
            if not re.match(r"(~(?:[a-z_][a-z0-9_]*|[-+]|\d+)?)$", name):
                raise ValueError(f'path: invalid "~" name expansion "{name}"')
            return "", name, part
        else:
            return "", "", path

    def casefold(self, s):
        return s

    def casefold_parts(self, parts):
        return parts

    def compile_pattern(self, pattern):
        return re.compile(fnmatch.translate(pattern)).fullmatch

    def is_reserved(self, parts):
        return False

    def make_uri(self, path):
        return "file://" + quote_from_bytes(bytes(path))


class KeyChain(PurePath):
    """

    """
    _flavour = _KeyChainFlavour()
    __slots__ = ("_name", )

    def __new__(cls, *args):
        self = cls._from_parts(args)

    @classmethod
    def resolve(cls, *args):
        pass

