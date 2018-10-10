FROM retr0h/molecule:latest
LABEL maintainer "Khardix <khardix@gmail.com>"

ENV PYTHON3_APK_PACKAGES="python3 python3-dev py3-cffi" \
    PYTHON3_PIP_PACKAGES="docker ansible molecule"

RUN sudo apk add --update --no-cache ${PYTHON3_APK_PACKAGES} && sudo rm -rf /var/cache/apk/* \
    && sudo python3 -m pip install --upgrade pip \
    && sudo python3 -m pip install --no-cache-dir --upgrade ${PYTHON3_PIP_PACKAGES} \
    && sudo rm -rf /root/.cache
