import xml.etree.ElementTree as ET
import shutil
import sys
import subprocess
from subprocess import run
from shlex import split
import os
import stat

class Single_ab_binding:
    example_AddChain_xml = "template_AddChain_FastRelax_Multi.xml"
    addChain_sh = "addChain.sh"
    def _init_(self, antigen_list: str, ab:str, ab_heavy_pdb:str, ab_light_pdb:str):

        self.antigen_list = antigen_list
        self.ab = ab
        self.ab_heavy_pdb = ab_heavy_pdb
        self.ab_light_pdb= ab_light_pdb



    def create_AddChain_xml(self):
        tree = ET.parse(Single_ab_binding.example_AddChain_xml)
        print(tree)
        root = tree.getroot()
        print(root)

        #heavy_chain_pdb = self.ab_heavy[self.ab]
        #light_chain_pdb = self.ab_light[self.ab]
        # Modify an element
        for addChain in root.iter('AddChain'):
            if addChain.get('name') == 'Aaa_H':
                addChain.set("file_name", self.ab_heavy_pdb)
            if addChain.get('name') == 'Aaa_L':
                addChain.set("file_name", self.ab_light_pdb)
                  
        # Write the changes back to the file
               
        addChain_xml_name = "AddChain_FastRelax_Multi_{ab}.xml".format(ab = self.ab)

        dst = addChain_xml_name
        
        tree.write(dst)

        return addChain_xml_name
    
    
    def run_addChain_cmd(self):

        addChain_xml_name = self.create_AddChain_xml()

        print("*****start of adding antibody chains")

        st = os.stat(Single_ab_binding.addChain_sh)
        os.chmod(Single_ab_binding.addChain_sh, st.st_mode | stat.S_IEXEC)

        #addChain_cmd = "./" + Single_pos_binding.addChain_sh
        #subprocess.call(addChain_cmd, shell = True)
        #subprocess.run(f"bash my_script.sh '{my_variable}'", shell=True)

        cmd = f"bash addChain.sh {self.antigen_list} {addChain_xml_name}"
        subprocess.run(cmd, shell = True)

        print("*****end of adding antibody chains")

        return 0
    
