#!/bin/bash

rm -rf data.db
touch data.db
python3 api_tester.py
