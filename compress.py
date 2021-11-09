import mdct
import soundfile as sf
import numpy as np
import argparse
from tqdm.auto import tqdm

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compresses wav file.')
    parser.add_argument('input', type=argparse.FileType('rb'), help='the path of an input wave file')
    parser.add_argument('output', type=str, help='the name of output npz files')
    parser.add_argument('--generate-steps', action='store_true',
                        help='if you want to generate multiple npz files for each compression stage')
    args = parser.parse_args()

    t = tqdm(total=6)
    data, rate = sf.read(args.input)

    t.update()
    r = mdct.mdct(data)
    if args.generate_steps: np.savez_compressed(f'{args.output}0.npz', rate=rate, data=r)

    t.update()
    r[150:511, :] = 0
    if args.generate_steps: np.savez_compressed(f'{args.output}1.npz', rate=rate, data=r)

    t.update()
    r = np.float16(r)
    if args.generate_steps: np.savez_compressed(f'{args.output}2.npz', rate=rate, data=r)

    t.update()
    r = np.round(r, decimals=2)
    if args.generate_steps: np.savez_compressed(f'{args.output}3.npz', rate=rate, data=r)

    t.update()
    r = np.where(abs(r) < 0.1, 0, r)
    np.savez_compressed(f'{args.output}4.npz', rate=rate, data=r)

    t.update()
    t.close()
