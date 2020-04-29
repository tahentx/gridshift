FROM scratch
COPY . /hello.py
EXPOSE 80
RUN /hello.py
CMD python hello.py