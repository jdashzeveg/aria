import json
import os
import copy
import re
import mmap
import jsonlines
import logging
import random
import torch
import functools
import shutil
from pathlib import Path
from copy import deepcopy
from typing import Callable, Iterable
from collections import defaultdict
from multiprocessing import Pool, get_start_method

from aria.config import load_config
from aria.tokenizer import Tokenizer, SeparatedAbsTokenizer
from aria.data.midi import MidiDict

def midi_to_json(midi_folder_path, save_path):
    all_midi_dicts = []
    for root, _, files in os.walk(mazurka):
	for file in files:
	    file_path = os.path.join(root, file)
	    try:
	       If os.path.isfile(file_path):
	          midi_dict = MidiDict.from_midi(file_path)
	    except Exception as e:
	       print(f"Error processing file {file_path}: {e}")
	all_midi_dicts.append(midi_dict)
      dataset = MidiDataset.__init__(all_midi_dicts)
      MidiDataset.save(dataset, save_path)
