import testinfra

def test_salt_minion_is_installed(Package):
    salt_minion = Package('salt-minion')
    assert salt_minion.is_installed
