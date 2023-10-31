from run_DRYP import run_DRYP
from timing import script_timer

# Display the runtime of the script at the end:
timer = script_timer()

# Define a working directory:
import os
os.chdir('/home/ivanovn/ws_local/projects/ffews/DRYP/')

# Define the model test function:
def test_dryp():

	"""
	Runs the DRYP model with the test input file.
	"""

	# Run the model:
	run_DRYP('test/input_test_AP.dmp')

if __name__ == '__main__':
	test_dryp()