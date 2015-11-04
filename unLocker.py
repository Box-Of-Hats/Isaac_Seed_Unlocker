from pyautogui import keyDown, keyUp
from time import sleep

def pressKey(key):
	keyDown(key)
	keyUp(key)

def enterSeeds(seedList):
	for seed in seedList:
		pressKey('up')
		pressKey('enter')
		pressKey('tab')
		print('Entering Seed: {}'.format(seed))
		for letter in seed:
			pressKey(letter)
		pressKey('enter')
		sleep(5)
		pressKey('esc')
		pressKey('down')
		pressKey('enter')
		sleep(1.0)

def readMeText(currentVer,seedFile,countdown=10):
	with open(seedFile) as seedFileTemp:
		numOfSeeds = len([str(seed) for seed in seedFileTemp])
	timeElapsed  = (numOfSeeds*7.5)
	timeElapsedMins = (timeElapsed/60)
	print("__-===  Isaac Easter Egg Seed Unlocker   ver{}  ===-__".format(currentVer))
	print("")
	print("Originally created by Jake:  github.com/Box-Of-Hats")
	print("This program is open-source and can be redistributed indefinitely.")
	print('')
	print("Using seed file:\t{}".format(seedFile))
	print("Number of seeds:\t{}".format(numOfSeeds))
	print("Approx Time to finish:\t{0}s ({1:0.2f}mins)".format(timeElapsed,timeElapsedMins))
	input('Press ENTER to begin entering seeds ({} second countdown)\n>'.format(countdown))
	for i in range(1,countdown+1)[::-1]:
		print('Starting in: {}'.format(i))
		sleep(1)

def finish(numOfSeeds):
	pressKey('up')
	pressKey('enter')
	pressKey('q')
	print('All {} easter eggs unlocked.'.format(numOfSeeds))
	print('Thankyou for using Isaac Easter Egg Seed Unlocker!')
	print('Support me by checking out my other projects: gitHub.com/Box-Of-Hats')

def main():
	currentVer = '1.0'
	seedFilePath = "seedList.txt"
	countdown = 6

	try:
		seedFile = open(seedFilePath)
		seedList = [str(seed) for seed in seedFile]
		readMeText(currentVer=currentVer,
			seedFile=seedFilePath,
			countdown=countdown)
		sleep(1)
		enterSeeds(seedList)
		finish(len(seedList))
	except:
		print('Missing seed file: {}'.format(seedFilePath))
	
	
	
if __name__ == '__main__':
	main()