#my code goes here, this is the base file
import json
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--init', help='called when new game')
    parser.add_argument('--iterations', help='number of iterations in game')
    parser.add_argument('--last_opponent_move', help='last opponent move')

    args = parser.parse_args()
    return


if __name__ == "__main__":
    main()
