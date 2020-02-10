FROM quay.io/ansible/molecule:latest
LABEL maintainer "Khardix <khardix@gmail.com>"

ENV PYTHON3_APK_PACKAGES="python3 python3-dev py3-cffi" \
    PYTHON3_PIP_PACKAGES="docker ansible molecule"

RUN apk add --update --no-cache ${PYTHON3_APK_PACKAGES} && rm -rf /var/cache/apk/* \
    && python3 -m pip install --upgrade pip \
    && python3 -m pip install --no-cache-dir --upgrade ${PYTHON3_PIP_PACKAGES} \
    && rm -rf /root/.cache

COPY .flake8    $HOME/.flake8
