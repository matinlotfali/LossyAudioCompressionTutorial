import mdct
import soundfile as sf
import numpy as np
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Decompresses npz file.')
    parser.add_argument('input', type=argparse.FileType('rb'), help='the path of an input npz file')
    parser.add_argument('output', type=argparse.FileType('wb'), help='the name of output wave files')
    args = parser.parse_args()

    npz = np.load(args.input)

    sig2 = mdct.imdct(npz['data'])
    sf.write(args.output, sig2, npz['rate'])
