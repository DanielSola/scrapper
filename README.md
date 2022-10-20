# Discogs website scrapper 🎵

Discogs is a free online database and marketplace of music releases connecting collectors, sellers, and music fans around the world.

This repository implements a Scrapper to extract the list of Singles & EPs by Michael Jackson.

It scrapes the following url: https://www.discogs.com/es/artist/15885-Michael-Jackson

To run it, clone the repository and run file main.py located in src folder using Python 3.9.6

## Files

* parser/dataset_writer.py --> Handles dataset CSV creation and adding rows. 
* parser/row_parser.py     --> Extracts data from a result 
* parser/scrapper.py       --> Iterates over Discogs website for scrapping

## Dataset

Obtained dataset can be found at https://zenodo.org/record/7225553 

Made by Daniel Solá