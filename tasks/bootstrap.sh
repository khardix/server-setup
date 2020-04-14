#!/bin/sh
# dependencies: apk/yum/dnf
# Bootstrap the machine to be able to run ansible modules
set -o errexit

if command -v apk; then
    apk add python3
elif command -v dnf; then
    dnf -y install python
elif command -v yum; then
    yum -y install python
fi
