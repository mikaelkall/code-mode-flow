# flow.py

## Description

This script is written for Code.Mode contest.

[ http://www.sweclockers.com/artikel/21924-skripta-med-nackademin-och-vinn-presentkort-pa-webhallen ]

## Summary

Script will wake up my stationary pc (Wake-on-LAN) from my laptop. 
Stream Youtube video to all connected chromecasts devices in the network and 
browse same youtube video on my laptop.  

### Compliance 

Follows pep257 and pep8 style recommendations.

    nighter@devbox:~/dev/code-mode-flow (master)$ pep257 ./flow.py && pep8 ./flow.py
    nighter@devbox:~/dev/code-mode-flow (master)$ 

## Usage

    ./flow.py

### Installation

Install dependencies.

[Mac] 

1. sudo easy_install pip
2. sudo pip install -r requirements.txt
3. sudo easy_install -U six

[Ubuntu] 

1. sudo apt-get install python-pip
2. sudo pip install --upgrade pip
3. sudo pip install -r requirements.txt
