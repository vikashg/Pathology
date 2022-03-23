import numpy as np
import argparse
import sys
import progressbar
import os
from ExtractPatches import createTiles

def get_arguments():
	parser = argparse.ArgumentParser(description='Enter the parameters')
	parser.add_argument('-t', help='Enter the filetype default=WSI', required=False, default='WSI', dest='ftype')
	parser.add_argument('-i', help='Enter the input dat dir', required=True, default='/workspace/data', dest='data_dir')
	parser.add_argument('-ob', help='Enter the output base_string default=patch', default='patch', dest='patch_name')
	parser.add_argument('-o', help='Enter the output_dir', default='out_dir', dest='out_dir')
	parser.add_argument('-s', help='Enter the patch size default=256', default=256, dest='patch_size')
	parser.add_argument('-n', help='Enter the number of tiles to be extracted default=None', default=None, dest='num')
	args = parser.parse_args()
	return args


def main():
	args = get_arguments()
	file_type = args.ftype
	data_dir = args.data_dir
	out_dir = args.out_dir
	patch_name = args.patch_name
	tile_size = int(args.patch_size)
	if args.num is None:
		num_tiles = None
	else:
		num_tiles = int(args.num)
	if args.ftype == 'tiff':
		backend='TiffFile'
		level=0
	elif args.ftype == 'WSI':
		backend='cuCIM'
		level=3

	list_files = os.listdir(data_dir)	
	all_list_files = [os.path.join(data_dir, _) for _ in list_files]
	data_dict={"image": all_list_files}
	pb = progressbar.ProgressBar(max_value=len(all_list_files))
	count = 0 
	if not os.path.exists(out_dir): 
		os.makedirs(out_dir)
	for filename in all_list_files:
		createTiles(filename, out_dir = out_dir, patch_name=patch_name, backend=backend, num_tiles=num_tiles, tile_size=tile_size)
		pb.update(count)
		count += 1

if __name__ == '__main__':
	main()
