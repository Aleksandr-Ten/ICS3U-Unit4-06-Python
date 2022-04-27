#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: April 2022
# This program calculates all the possible RGB combinations


def main():
    # this function has nested loops
    red = 0
    green = 0
    blue = 0

    # process & output
    for red in range(255 + 1):
        for green in range(255 + 1):
            for blue in range(255 + 1):
                print("RGB ({0}, {1}, {2})".format(red, green, blue))

    print("\nDone.")


if __name__ == "__main__":
    main()
