FROM scratch
COPY . /hello.py
EXPOSE 80
RUN make /hello.py
CMD python hello.py