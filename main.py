#####################################
import GAME.core
import TILEED.core
import config
import getopt, sys, os
#####################################

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hev", ["help"])
	except getopt.GetoptError as err:
		print(err)
		sys.exit(2)
	verbose = False
	starteditor = False
	for o, a in opts:
		if o == "-v":
			verbose = True
		elif o in ("-h", "--help"):
			sys.exit()
		elif o in ("-e"):
			starteditor = True
		else:
			assert False, "unhandled option"
	if not starteditor:
		game = GAME.core.Game(config.Config())
		game.start()
	else: 
		editor = TILEED.core.TileEditor(config.Config())
		editor.start()
if __name__ == "__main__":
	main()
