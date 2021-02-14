#pip install tqdm
from tqdm import tqdm
import time

for i in tqdm(range(15)):
    time.sleep(.9)
