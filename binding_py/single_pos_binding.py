import single_ab_binding as sab
import sys
import subprocess
from subprocess import run
from shlex import split
import os
import stat
import csv

class Single_pos_binding:
    def _init_(self,pos: int, antigen_list: str, abs_csv: str):
        self.pos = pos
        self.antigen_list = antigen_list
        self.abs_csv = abs_csv


    def run_binding_for_allAbs(self):
        with open(self.abs_csv, mode ='r') as file: 
            csvFile = csv.DictReader(file)
            for lines in csvFile:
                    ab = lines['antibody']
                    ab_heavy_pdb = lines['antibody_heavy_chain_pdb']
                    ab_light_pdb= lines['antibody_light_chain_pdb']

                    single_ab_binding = sab.Single_ab_binding(antigen_list = self.antigen_list, ab = ab, ab_heavy_pdb = ab_heavy_pdb, ab_light_pdb = ab_light_pdb)

                    single_ab_binding.run_addChain_cmd()
