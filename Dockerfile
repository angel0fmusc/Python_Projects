FROM python:latest
LABEL maintainer="Victoria Rivas"
ADD MAC_Addr_Lookup.py /
RUN pip install requests
ENTRYPOINT [ "python", "./MAC_Addr_Lookup.py" ]
