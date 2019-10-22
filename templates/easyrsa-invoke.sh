#!/bin/bash

export EASYRSA_VARS_FILE="{{ easyrsa }}/vars"

{{ easyrsa }}/easyrsa "$@"
