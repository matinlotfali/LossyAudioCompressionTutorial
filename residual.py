import soundfile as sf
import numpy as np
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Decompresses npz file.')
    parser.add_argument('input1', type=argparse.FileType('rb'), help='the path of an input wave file')
    parser.add_argument('input2', type=argparse.FileType('rb'), help='the path of an input wave file')
    parser.add_argument('output', type=str, help='the name of output wave and npz files')
    args = parser.parse_args()

    data1, rate = sf.read(args.input1)
    data2, rate = sf.read(args.input2)
    minlen = min(len(data1), len(data2))

    residual = data1[:minlen] - data2[:minlen]
    sf.write(f'{args.output}.wav', residual, rate)
    np.savez_compressed(f'{args.output}.npz', data=residual, rate=rate)
