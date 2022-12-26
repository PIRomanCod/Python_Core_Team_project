import pickle
from pathlib import Path
import os

class file_storage():
  def load_file(self):
      try:
          with open(Path.home().joinpath('PersonalAssistant').joinpath('AddressBookData.bin'), 'rb') as l_file:
              return pickle.load(l_file)
      except FileNotFoundError:
          if not os.path.exists(Path.home().joinpath('PersonalAssistant')):
              os.makedirs(Path.home().joinpath('PersonalAssistant'))
          with open(Path.home().joinpath('PersonalAssistant').joinpath('AddressBookData.bin'), 'w') as f:
              pass
          return {}
  
  def save_file(self, data):
      with open(Path.home().joinpath('PersonalAssistant').joinpath('AddressBookData.bin'), 'wb') as s_file:
          pickle.dump(data, s_file)