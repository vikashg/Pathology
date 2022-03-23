input_dir=/workspace/data/svs/cardioembolic
out_dir=./out_dir

python ExtractPatches.py -t WSI -i $input_dir -ob patch_ -o $out_dir -s 256 -n 10
