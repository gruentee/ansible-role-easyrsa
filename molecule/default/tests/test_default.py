import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    if not f.exists:
        raise AssertionError()
    if not f.user == 'root':
        raise AssertionError()
    if not f.group == 'root':
        raise AssertionError()
