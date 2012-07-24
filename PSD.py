from optparse import OptionParser
import glob
import os
import sys

usage = """ %prog [options] FILE """
parser = OptionParser(usage=usage, version = "%prog")

parser.add_option("-r", help = "run")
parser.add_option("-m", "--movie", action='store_true')
options, args = parser.parse_args()

modelruns = glob.glob('igwturbgen_*')
modelruns.sort()

# identify most recent run
last_model_run = modelruns[-1]

if options.r == None:
    model_run = last_model_run
else:
    model_run = 'igwturbgen_' + options.r

os.chdir(model_run)
os.system('python ../post_process/python/psd.py')
os.chdir('..')
