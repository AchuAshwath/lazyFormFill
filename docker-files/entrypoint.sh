#!/bin/bash
apt-get update && apt-get install -y build-essential cmake git
pip install llama-cpp-python 
python whisper.py

