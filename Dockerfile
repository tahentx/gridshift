FROM scratch
COPY . /hello.py
EXPOSE 80
RUN echo "hello world from run command"
CMD python hello.py