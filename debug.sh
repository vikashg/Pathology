docker build -t vikash/readpathoslides:0.1.0 .

app_dir=$(pwd)/app
#data_dir=<input_data_dir>
data_dir=/raid/Data/MayoClinicData/BloodPath
#Enter the name of the input_data_dir


NV_GPU=0, nvidia-docker run  --rm -it --shm-size=1g --ulimit memlock=-1 --ulimit stack=67108864 -v $data_dir:/workspace/data -v $app_dir:/workspace/app vikash/readpathoslides:0.1.0 /bin/bash

