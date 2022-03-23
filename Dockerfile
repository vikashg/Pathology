#Author: Vikash Gupta (gupta.vikash@mayo.edu)
#A dockerfile built on MONAI for extracting patches. Change the parameters in run.sh to run the program
FROM nvcr.io/nvidia/pytorch:21.12-py3
RUN pip install slideio 

RUN apt-get update
RUN DEBIAN_FRONTEND="noninteractive" TZ=Etc/UTC apt-get -y install tzdata
RUN apt-get install -y ffmpeg libsm6 libxext6
RUN pip install opencv-python 
RUN pip install cucim
RUN git clone https://github.com/Project-MONAI/MONAI.git
WORKDIR /workspace/MONAI
RUN python setup.py develop
RUN pip install tifffile
RUN pip install progressbar2
WORKDIR /workspace

WORKDIR /workspace/app
