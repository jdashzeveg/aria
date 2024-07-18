import json
import os
from pathlib import Path
from copy import deepcopy
from typing import Callable, Iterable
from collections import defaultdict
from multiprocessing import Pool, get_start_method

from aria.config import load_config
from aria.tokenizer import Tokenizer, SeparatedAbsTokenizer
from aria.data.midi import MidiDict
from aria.data.datasets import MidiDataset

def midi_to_json(midi_folder_path, save_path):
	#store mididicts into one dict
	all_midi_dicts = []
	#loop through files and subdirs in mazurka /Users/chriskim/aria/tests/mazurkas-mid
	for root, _, files in os.walk(midi_folder_path):
		#for file in files
		for file in files:
			#get file_path of the file
			file_path = os.path.join(root, file)
			#make sure it's a mid file
			try:
				if os.path.isfile(file_path) and file_path.endswith('.mid'):
					midi_dict = MidiDict.from_midi(file_path)
					#append the file's midi_dict conversion result
					all_midi_dicts.append(midi_dict)
			except Exception as e:
				print(f"Error processing file {file_path}: {e}")
	#create a mididataset from the mididicts
	dataset = MidiDataset.__init__(all_midi_dicts)
	#save it to a json file
	MidiDataset.save(dataset, save_path)
