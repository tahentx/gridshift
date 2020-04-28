FROM scratch
ADD amzn2-container-raw-2.0.20200406.0-x86_64.tar.xz /
COPY src/ /hello.py
EXPOSE 80
