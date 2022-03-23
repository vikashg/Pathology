from monai.apps.pathology.transforms import TileOnGrid
from monai.data.image_reader import WSIReader
#from monai.data import WSIReader
from monai.transforms import Transform, Compose, LoadImage
import os
from monai.apps.pathology.transforms import TileOnGrid
import cv2
import numpy as np
import argparse
import sys
import progressbar
from tqdm import tqdm

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


def save_patches(patch_array, out_dir, root_filename):
	num_patches = patch_array.shape[0]
	for i in tqdm(range(num_patches), desc='Creating Patchs...', ascii=False, ncols=100):
		out_filename = os.path.join(out_dir, root_filename + str(i) + '.png')
		img = np.transpose(patch_array[i,:], [2, 1, 0])
		cv2.imwrite(out_filename, img)

def createTiles(filename, out_dir, patch_name = 'patch_', backend='cuCIM', num_tiles=None, tile_size=256):
	"""
	Extract patches from a whole slide image and saves the patches to a given dictionary 
	:param filename: absolute filepath 
	:param out_dir: Output location path 
	:param backend: 'cuCIM' for svs file and 'TiffFile' for tiff images 
	:param num_tiles: number of tiles to be extracted. default is None No tile will be extracted 
	"""
	extract_transform = Compose([LoadImage(image_only=True,reader=WSIReader, backend=backend), 
				TileOnGrid(tile_count=num_tiles, tile_size=tile_size)])
	try: 
		X = extract_transform(filename)

		_root_filename = filename.split('/')[-1].split('.')[0]
		save_patches(X, out_dir, _root_filename+ '_'  + patch_name )
	except:
		print('Couldnot extract file: ', filename)


