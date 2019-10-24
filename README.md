easyrsa
=========

[![Build Status](https://travis-ci.org/vduseev/ansible-role-easyrsa.svg?branch=master)](https://travis-ci.org/vduseev/ansible-role-easyrsa)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/bf3aa1d48f0e4e55b6620d9e198540f4)](https://www.codacy.com/manual/vduseev/ansible-role-easyrsa?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vduseev/ansible-role-easyrsa&amp;utm_campaign=Badge_Grade)

This role manages easyrsa 3.x installation on Ubuntu 18.04 bionic servers.

All installation tasks are tagged with the `install` tag. All uninstalling tags are tagged with `never` tag.

By default the role installs the latest release of easyrsa 3.x, creates a symlink in a standard `PATH` location and initializes a PKI if not done so already.

Role Variables
--------------

  - `easyrsa_release_url` is commented out by default. Use it when you want to download from a specific URL rather than the latest tag from official repo.
  - `easyrsa: /opt/easyrsa` specifies easyrsa installation dir.
  - `easyrsa_pki: /etc/pki` specifies PKI location.
  - `easyrsa_requirements: [openssl]` lists additional required packages.
  - `easyrsa_tmp_package: /tmp/easyrsa.tgz` sets temporary download location for the release package.
  - `easyrsa_symlink: /usr/local/bin/easyrsa` sets symlink location. Ideally available from $PATH.

Example Playbook
----------------

```yaml
---
- hosts: all
  roles:
    - vduseev.easyrsa
```

Installation
------------

```console
ansible-playbook -i hosts -b playbook.yml
```

Uninstall
---------

```console
ansible-playbook -i hosts -b playbook.yml --skip-tags install --tags never
```
