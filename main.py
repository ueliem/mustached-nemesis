#####################################
import GAME.core
import config
#####################################

def main():
	game = GAME.core.Game(config.Config())
	game.start()

if __name__ == "__main__":
	main()
