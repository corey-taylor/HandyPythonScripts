#	Script for extracting good docking recs from multi-pdb using tab-separated list of graded poses
#	Written by Corey Taylor
#	Date: 10.10.17

#	NOTE: Ensure input list has two tabs separating fields or script won't work!

import os
import sys
import argparse
import csv


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--list', required=True, help='List of graded poses')
    parser.add_argument('--pdb', required=True, help='pdb file')
    opts = parser.parse_args()
    return opts


def main():
    opts = parse_args()

    #	Open list input file

    with open(opts.list, 'r') as f:
        c = csv.reader(f, delimiter='\t')
        for row in c:  # read in rows
            if row[2] != '':  # only keep those with grade
                posenum = find_pose(row[1])

    print 'List file is "', opts.list
    print 'Input file file is "', opts.pdb


def find_pose(posenum):
    #	Open sdf

    opts = parse_args()

    with open(opts.pdb, 'r') as pdb:
        p = csv.reader(pdb, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
        for row in p:  # read in rows
	  fh = open("GoodRecs.pdb", "a")
	  posewriter = csv.writer(fh, delimiter=' ', quoting=csv.QUOTE_MINIMAL)
	  for row in p:  # read in rows
	    if posenum in row:
	      posewriter.writerow(row)
	      for row in p:  # read in rows
		posewriter.writerow(row)
		if len(row) == 1 and row[0] == 'ENDMDL':  # break at end of pose
		  break
	      else:
		  break
        fh.close()

    return posenum


if __name__ == "__main__":
    main()
