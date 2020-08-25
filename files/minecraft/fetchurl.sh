#!/bin/sh
set -o errexit

readonly projectID="${1:?Missing project ID}"; shift
readonly fileID="${1:?Missing file ID}"; shift

curl "https://addons-ecs.forgesvc.net/api/v2/addon/${projectID}/file/${fileID}/download-url" && echo
