def test_salt_minion_is_installed(host):
    pkg = host.package('salt-minion')
    assert pkg.is_installed
