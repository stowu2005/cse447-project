#!/usr/bin/env python
from argparse import ArgumentParser


parser = ArgumentParser()
parser.add_argument('fpred')
parser.add_argument('fgold')
parser.add_argument('--verbose', action='store_true')
args = parser.parse_args()


def load_pred(fname):
    with open(fname) as f:
        return [l[:-1].lower() for l in f]


pred = load_pred(args.fpred)
gold = load_pred(args.fgold)

if len(pred) < len(gold):
    pred.extend([''] * (len(gold) - len(pred)))

correct = 0
for i, (p, g) in enumerate(zip(pred, gold)):
    right = g in p
    correct += right
    if args.verbose:
        print('Input {}: {}, {} is {} in {}'.format(i, 'right' if right else 'wrong', g, 'in' if right else 'not in', p))
print('Success rate: {}'.format(correct/len(gold)))