import pytest

from keychain.core import _KeyChainFlavour


class TestKeyChainFlavour(object):
    keychain_flavour = _KeyChainFlavour()

    # begin: test_splitroot
    @pytest.mark.parametrize(
        ("path", "root", "part", "msg"),
        [
            ("", "", "", "valid empty path"),
            ("/", "/", "", "valid root link with empty path part"),
            ("/some", "/", "some", "valid root link with short relative path part"),
            ("./some", "", "some", "valid dot here path with short relative path part"),
            ("/some/../other", "/", "some/../other", "valid root link with long double-dot path part"),
            ("./some/.../other/", "", "some/.../other/", "valid dot here path with long triple-dot path part"),
            ("../some/.../other/", "", "../some/.../other/", "valid double dot parent path with long triple-dot path "
                                                          "part"),
            ("/../some/.../other/", "/", "../some/.../other/", "valid root link with dot parent long triple-dot path "
                                                               "part"),
            ("some/dir/./../.../dur", "", "some/dir/./../.../dur", "valid relative path with many dot path parts"),
            ("/some/dir", "/", "some/dir", "valid root link with long relative path part"),
            ("~", "~", "", "valid home expansion with empty path part"),
            ("~/", "~", "", "valid home expansion with relative path part"),
            ("~name", "~name", "", "valid name expansion with empty path part"),
            ("~name/some", "~name", "some", "valid name expansion with short relative path part"),
            ("~name/some/dir", "~name", "some/dir", "valid name expansion with long path part"),
            ("~+/some/dir", "~+", "some/dir", "valid current link expansion with long relative path part"),
            ("~-/some/dir", "~-", "some/dir", "valid previous link expansion with long relative path part"),
            ("~0/some/dir", "~0", "some/dir", "valid root item expansion with long relative path part"),
            ("~10/some/dir", "~10", "some/dir", "valid 11th item expansion with long relative path part"),
            ("~999/some/dir", "~999", "some/dir", "valid 1000th item name expansion with long relative path part"),
            ("/~name/some/dir", "/", "~name/some/dir", "valid root link with tilde-name long relative path "
                                                       "part"),
        ]
    )
    def test_splitroot(self, path, root, part, msg):
        assert self.keychain_flavour.splitroot(path) == ("", root, part), f"failed for: {msg}"
    # end: test_splitroot

    # begin: test_splitroot_type_error
    @pytest.mark.parametrize(
        ("path", "sep", "msg"),
        [
            (None, "/", "invalid path type None"),
            ("", None, "invalid sep type None"),
            ([], "/", "invalid path type list"),
            ("", [], "invalid sep type list"),
            ({}, "/", "invalid path type dict"),
            ("", {}, "invalid sep type dict"),
            ((), "/", "invalid path type tuple"),
            ("", (), "invalid sep type tuple"),
            (b"", "/", "invalid path type bytes"),
            ("", b"", "invalid sep type bytes"),
            (0, "/", "invalid path type int"),
            ("", 0, "invalid sep type int"),
            (0.0, "/", "invalid path type float"),
            ("", 0.0, "invalid sep type float"),
        ]
    )
    def test_splitroot_type_error(self, path, sep, msg):
        with pytest.raises(TypeError, match=r"(path|sep): type str required \(got type"):
            self.keychain_flavour.splitroot(path, sep=sep)
            assert False, f'{msg}: type({path})="{type(path)}" and type({sep})="{type(sep)}"'
    # end: test_splitroot_type_error

    # begin: test_splitroot_value_error
    @pytest.mark.parametrize(
        ("path", "sep", "msg"),
        [
            ("", "\\", 'invalid sep value "\\"'),
            ("~1name", "/", "invalid expansion name"),
            ("~=", "/", "invalid expansion"),
            ("~~~~/some/dir", "/", "invalid name expansion"),
            ("~++", "/", "invalid current link expansion"),
            ("~--", "/", "invalid previous link expansion"),
        ]
    )
    def test_splitroot_value_error(self, path, sep, msg):
        with pytest.raises(ValueError, match=r'(path|sep): invalid "'):
            self.keychain_flavour.splitroot(path, sep=sep)
            assert False, f'{msg}: path="{path}" and sep="{sep}"'
    # end: test_splitroot_type_error
