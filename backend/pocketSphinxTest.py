from os import path
import pocketsphinx
from pocketsphinx import Pocketsphinx, get_model_path, get_data_path


# Adjust the paths according to your PocketSphinx model locations
MODELDIR = "/usr/local/lib/python3.7/site-packages/pocketsphinx/model"
DATADIR = "/usr/local/lib/python3.7/site-packages/pocketsphinx/data"

# Get the model and data directories
model_path = get_model_path()
data_path = get_data_path()

config = pocketsphinx.Decoder.default_config()
config.set_string('-hmm', model_path + '/en-us')
config.set_string('-lm', model_path + '/en-us.lm.bin')
config.set_string('-dict', model_path + '/cmudict-en-us.dict')

decoder = pocketsphinx.Decoder(config)

decoder.start_utt()
stream = open(path.join(DATADIR, 'goforward.raw'), 'rb')
while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
    else:
        break
decoder.end_utt()

print([seg.word for seg in decoder.seg()])
