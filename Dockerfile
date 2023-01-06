FROM ubuntu:latest
ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update && apt-get install -y python3-pip

RUN pip install numpy==1.21.5
RUN pip install pandas
RUN pip install scikit-learn==1.0.2
RUN pip install category-encoders==2.5.1.post0
RUN pip install gradio==3.12.0
RUN pip install altair

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*



