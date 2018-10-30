#!/usr/bin/bash
set -o errexit

dehydrated_deploy_cert() {
    local -r domain="$1" key="$2" fullchain="$4"  # others are ignored

    local -r target="/etc/pki/https/${domain}"
    install -Dm 0644 -g https "$key"         "$target/privkey.pem"
    install -Dm 0644 -g https "$fullchain"   "$target/fullchain.pem"
}

# Call appropriate handler if defined
readonly handler="${1}"; shift
if declare -fF "dehydrated_$handler" >/dev/null; then
    "dehydrated_$handler" "$@"
fi
