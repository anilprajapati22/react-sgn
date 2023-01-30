FROM ubuntu

WORKDIR /sgn-api
RUN apt update -y
RUN apt install python3 python3-pip -y
COPY requirements.txt .
COPY app.py .
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD [ "flask" , "run", "-h" , "0.0.0.0" , "-p" , "8080" ]
