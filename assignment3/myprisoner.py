#By Eric Timmerman
#I'm using a list as a queue which isn't very efficient, cause you can't exactly save a queue in json
#Strategy is what I've decided to call "disproportionate retribution"
import json
import argparse
import queue as q
import io



def init(moves):
    moves.append("silent")
    moves.append("silent")
    moves.append("silent")
    moves.append("confess")
    return

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')

    args = parser.parse_args()

    moves = []

    if args.init == 'true':
        init(moves)
    else:
        read = io.open("data.json", "r")
        moves = json.load(read)

        if args.last_opponent_move == "confess":
            moves.append("confess")
            moves.append("confess")
        elif args.last_opponent_move == "silent":
            moves.append("silent")
    
    move = moves.pop(0)

    save = io.open("data.json", "w")
    json.dump(moves, save)

    print(move)
    return


if __name__ == "__main__":
    main()
