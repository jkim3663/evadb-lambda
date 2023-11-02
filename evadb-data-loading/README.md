## Introduction

The topic being explored is fixing EvaDB’s data loading issues that originated from loading corrupted images or broken documents. One issue is when EvaDB’s executor is running, when there is a corrupted image encountered, the entire process is aborted rather than skipping the corrupted file’s load. Another similar issue happens when a corrupted PDF type file is loaded through EvaDB’s executor. The objective of this project is exploring various options to handle this situation, choose the optimal solution, and then implement it. 

This repository contains python scripts, sample images, and other documents that are related to 
the data loading improvement project. 

## Reference

### EvaDB LOAD query

https://evadb.readthedocs.io/en/stable/source/reference/evaql/load_image.html

### EvaDB Repository

https://github.com/georgia-tech-db/evadb

### EvaDB Image Loading Issue

https://github.com/georgia-tech-db/evadb/issues/721

### EvaDB PDF Loading Issue

https://github.com/georgia-tech-db/evadb/issues/1067

## Python Scripts 
### corrupt_image.py
Python script that intentionally corrupts an image file to analyze the loading issue. 
### load_image.py
Python script used to verify that the current issue is relevant and the loading functionality fails
with corrupted object files.