#!/usr/bin/env python3

import argparse
import datetime
import os
import aiohttp
import asyncio
from bs4 import BeautifulSoup as BS4
import helpers


async def main():
    parser = argparse.ArgumentParser(
        description='Smashing Wallpaper Downloader'
    )

    curr_month = datetime.datetime.now().strftime('%b')
    curr_year = datetime.datetime.now().strftime('%Y')
    output_default_dir = './output'

    # 12 datetimes objects to retrieve months' information
    dates = [
        datetime.date(2019, numeric_month, 1)
        for numeric_month in range(1, 13)
    ]

    # key = month shortname,
    # value = tuple-pair (its numeric zero-padded value, month fullname)
    months = dict(
        (d.strftime('%b'), (d.strftime('%m'), d.strftime('%B'))) for d in dates
    )

    parser.add_argument(
        'resolution',
        type=lambda x: helpers.is_resolution(parser, x),
        help='Result resolution wallpapers. Example: `1024x768`'
    )
    parser.add_argument(
        '-m', '--month',
        type=str,
        default=curr_month,
        choices=months.keys(),
        help='A month to download wallpapers for. Example: `Jan` or `Dec`'
    )
    parser.add_argument(
        '-y', '--year',
        type=lambda x: helpers.is_year(parser, x),
        default=curr_year,
        help='A year to download wallpapers for. Example: `2012` or `2000`'
    )
    parser.add_argument(
        '-o', '--output',
        type=str,
        default=os.path.join(os.getcwd(), output_default_dir),
        help='''
        A directory to download wallpapers into.
        If ommited it will be created as `%s`
        ''' % output_default_dir
    )

    args = parser.parse_args()
    print(args)

    # form an url
    url_pattern = 'https://www.smashingmagazine.com/{year}/' \
        '{month_numeric}/desktop-wallpaper-calendars-{month_fullname}-{year}/'

    url = url_pattern.format(
        year=args.year,
        month_numeric=months.get(args.month)[0],
        month_fullname=months.get(args.month)[1]
    ).lower()

    print(f"Url: {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print('Response status code:', response.status)
            if response.status == 200:
                markup = await response.text()
                soup = BS4(markup, 'lxml')
                wallpapers_urls = helpers.get_wallpaper_links(
                    soup,
                    args.resolution
                )

                print(wallpapers_urls)
                print(len(wallpapers_urls))

                # if wallpaper_urls:

                # else:
                #     # TODO
            else:
                # TODO
                pass


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
