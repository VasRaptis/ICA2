#!/usr/bin/python3

# import modules
import os, subprocess, sys, re
import pandas as pd

# import my functions 
import functions as fun

# ask user if he wants to change working directory
fun.give_dir()

# ask user to define the protein family and taxonomic group (function outputs a dictionary)
prot_taxon = fun.give_prot_taxon()

# pyruvate dehydrogenase
# ascomycete fungi
# 

# if user provided a taxon name:
if (list(prot_taxon.keys())[1] == "taxon_name"):
  print("You want to search for a taxonmic group name:")
  print("Starting searching NCBI protein database for " + prot_taxon["protein"] + " in " + prot_taxon["taxon_name"] + ": ...\n")
  protein = prot_taxon["protein"]
  beast   = prot_taxon["taxon_name"]
  query   = protein + " [PROT] AND " + beast + " [organism]"     # get query string
  output  = protein.replace(" ", "_") + "_" + beast.replace(" ", "_") # output name (replace whitespace witj "_")
  esearch = 'esearch -db protein -query ' + '\"' + query + '\"'  # get esearch string ~ maybe give option to change database??
  # get fasta sequences:
  output_fasta = output + ".fa"                                  # fasta file output name (used later)
  format  = 'fasta'
  efetch  = 'efetch -format ' + format + " > " + output_fasta    # get efetch string 
  full_search_cmd = esearch + " | " + efetch                     # get full cmd string
  print("Getting fasta sequences ...")
  print("Your esearch | efetch command:\n" + full_search_cmd)
  os.system(full_search_cmd)
  print("Done. Your fasta sequences are stored in: " + output_fasta)
  # get accession numbers:
  output_acc = output + ".acc"                                 # accessions file output name (used later)
  format  = 'acc'
  efetch  = 'efetch -format ' + format + " > " + output_acc    # get efetch string 
  full_search_cmd = esearch + " | " + efetch                   # get full cmd string
  print("Getting accession numbers of sequences ...")
  print("Your esearch | efetch command:\n" + full_search_cmd)
  os.system(full_search_cmd)
  print("Done. Your sequences's accession numbers are stored in: " + output_acc)

  
  
  
  
  
  
#elif (list(prot_taxon.keys())[1] == "taxonid"):
#  print("You want to search for a taxonid:"
#  print("Starting searching NCBI protein database for " + prot_taxon["protein"] + " in " + prot_taxon["taxonid"] + ":")


# esearch -db protein -query "pyruvate dehydrogenase [PROT] AND ascomycete fungi [organism]" | efetch -format fasta > test-set.fa


