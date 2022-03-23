#input_dir=/workspace/data/svs/cardioembolic
input_dir=/workspace/data/tiff
out_dir=./out_dir

python main.py -t WSI -i $input_dir -ob patch_ -o $out_dir -s 256 
