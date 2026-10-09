"""Build only the requested manuscript style-trial version.
Usage: python assemble_reading_copies.py v0.2
Inputs and frozen hashes are validated before output generation.
"""
import argparse, importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def main():
 p=argparse.ArgumentParser(); p.add_argument("version",choices=("v0.2",)); p.parse_args()
 spec=importlib.util.spec_from_file_location("build_v0_2",ROOT/"build_v0_2.py")
 mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); mod.main()
if __name__=="__main__": main()
