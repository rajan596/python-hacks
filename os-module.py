# python3

import os
import time

print(os.getcwd())
os.mkdir('demoo_dir')

time.sleep(2)
os.rename('demoo_dir','new_dir')

time.sleep(2)
os.rmdir('new_dir')
