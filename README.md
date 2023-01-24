# sierpmidi
A short toy program to generate music using Sierpinsky's triangles.

Inspired by https://mastodon.social/@acb/109567809376185861

## Setup

pip install -r requirements.txt

## Usage


    usage: sierpmidi [-h] [-g GASKETS] [-p PROB_FLIP] [-b BPM] [-k KEY]
                     [-m {ionian,dorian,phrygian,lydian,mixolydian,aeolian,locrian}] [-t TRACK_NAME]
                     filename


    positional arguments:
      filename              output filename

    optional arguments:
      -h, --help            show this help message and exit
      -g GASKETS, --gaskets GASKETS
                            number of gaskets to render
      -p PROB_FLIP, --prob-flip PROB_FLIP
                            probability of flipping a gasket
      -b BPM, --bpm BPM
      -k KEY, --key KEY     key as a midi note number
      -m {ionian,dorian,phrygian,lydian,mixolydian,aeolian,locrian}, --mode {ionian,dorian,phrygian,lydian,mixolydian,aeolian,locrian}
      -t TRACK_NAME, --track-name TRACK_NAME

[Sample - aeolian.mp3](./samples/aeolian.mp3)
[Sample - dorian.mp3](./samples/dorian.mp3)
