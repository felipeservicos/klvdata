#!/usr/bin/env python
import sys, klvdata;
for packet in klvdata.StreamParser(sys.stdin.buffer.read()): packet.structure()
