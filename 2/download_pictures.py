#!/usr/bin/env python3

import argparse
import helpers


def main():
    parser = argparse.ArgumentParser(description='A wallpaper downloader for smashingmagazine.com')
    parser.add_argument(
        'resolution',
        type=lambda x: helpers.is_resolution(parser, x),
        action='store',
        help='Result resolution wallpaper. Example: `1024x768`'
    )
    parser.add_argument(
        '-m', '--month',
        type=lambda x: helpers.is_month(parser, x),
        action='store',
        required=True,
        help='A month to download wallpaper for. Example: `Jan` or `Dec`'
    )
    parser.add_argument(
        '-y', '--year',
        type=lambda x: helpers.is_year(parser, x),
        action='store',
        required=True,
        help='A year to download wallpaper for. Example: `2012` or `2000`'
    )

    # --help, -h TODO

if __name__ == '__main__':
    main()
