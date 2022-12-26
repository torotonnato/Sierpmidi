from math import comb
from random import randint, random
from midiutil.MidiFile import MIDIFile
import argparse

def sierpinsky_col(x, h, scale=1):
	'''Computes a column of the Sierpinsky's triangle of height h'''
	'''and returns a list of the points' y-coord in that column. '''
	'''Optional keyword argument:'''
	'''scale: scale factor (mainly used to flip the sign of the ys)'''

	s = []
	for n in range(abs(x - h + 1), h):
		k2 = x - h + 1 + n
		if not k2 & 1 and comb(n, k2 // 2) & 1:
			s.append((h - n - 1) * scale)
	return s

modes = {
	'ionian'    : 0,
	'dorian'    : 1,
	'phrygian'  : 2,
	'lydian'    : 3,
	'mixolydian': 4,
	'aeolian'   : 5,
	'locrian'   : 6
}

def degree_to_pitch(key, deg, mode=0):
	'''Returns the pitch using the degree of a diatonic scale in a'''
	'''given mode.'''

	#Diatonic intervals: WHOLE_STEP = 2, HALF_STEP = 1
	diatonic_ints = [2, 2, 1, 2, 2, 2, 1]

	#Inefficient but straightforward
	pitch = key
	if deg > 0:
		#Forward
		for it in range(deg):
			pitch += diatonic_ints[(it + mode) % 7]
	else:
		#Backward
		it = 6
		for _ in range(-deg):
			pitch -= diatonic_ints[(it + mode) % 7]
			it -= 1

	return pitch

def create_midi(args):
	'''Creates a midi file.'''
	'''Parameters in opts dict:'''
	'''gaskets: number of sierpinsky gaskets to render'''
	'''track-name: midi track name'''
	'''bpm: midi bpm'''
	'''key: midi note number representing the key'''
	'''mode: see "modes"'''
	'''prob-flip: the probability that a gasket is flipped'''
	'''fname: midi file name'''

	time     = 0   #Global midi time
	track    = 0   #Midi track
	channel  = 0   #Midi channel
	volume   = 100 #Midi notes volume
	duration = .25 #Sixteenth notes

	#One track
	mf = MIDIFile(1)
	mf.addTrackName(track, time, args.track_name)
	mf.addTempo(track, time, args.bpm)

	mode = modes[args.mode]

	for _ in range(args.gaskets):
		h   = 2 ** randint(0, 4)
		dir = -1 if random() >= args.prob_flip else +1
		for x in range(h * 2):
			deg = sierpinsky_col(x, h, dir)
			pitches = [degree_to_pitch(args.key, d, mode) for d in deg]
			for pitch in pitches:
				mf.addNote(track, channel, pitch, time, duration, volume)

			#Next note after one eighth
			time += .5

	with open(args.filename, 'wb') as outf:
	    mf.writeFile(outf)




if __name__ == "__main__":
	parser = argparse.ArgumentParser(
	                    prog = 'sierpmidi',
	                    description = 'Renders a midi file using the Sierpinsky triangle.',
	                    epilog = 'Inspired by https://mastodon.social/@acb/109567809376185861')


	parser.add_argument('-g', '--gaskets', default=100, help='number of gaskets to render')
	parser.add_argument('-p', '--prob-flip', type=float, default=.5, help='probability of flipping a gasket')
	parser.add_argument('-b', '--bpm', type=int, default=120)
	parser.add_argument('-k', '--key', type=int, default=60, help='key as a midi note number')
	parser.add_argument('-m', '--mode', default='ionian', choices=['ionian', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'aeolian', 'locrian'])
	parser.add_argument('-t', '--track-name', default='Sierpinsky')
	parser.add_argument('filename', help='output filename')
	args = parser.parse_args()

	create_midi(args)
