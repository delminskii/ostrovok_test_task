#!/usr/bin/env python3

import re
from urllib.parse import urlparse
import os
import aiofiles


def is_resolution(parser, resolution_str, pattern=r'\d+x\d+'):
    """check whether resolution_str string fits good to normal image resolution

    :param parser: argparse parser object
    :param resolution_str: source string for resolution. Example: 1600x900
    :param pattern: regexp pattern whether to match resolution_str string
    """
    if re.match(pattern, resolution_str) is None:
        parser.error(
            f"`{resolution_str}` does not fit good to image resolution"
        )
    return resolution_str.lower()


def is_year(parser, year_str, pattern=r'[12]\d{3}'):
    """check whether year_str fits good to year pattern (format: YYYY)

    :param parser: argparse parser object
    :param year_str: source string for year. Example: 2012
    :param pattern: regexp pattern while to match year_str string
    """
    if re.match(pattern, year_str) is None:
        parser.error(f"`{year_str}` does not fit good to year in YYYY format")
    return year_str


def get_wallpapers_links(soup, resolution):
    """return `href` values of `a` tags for images with `resolution` resolution

    :param soup: BS4 object
    :param resolution: wallpaper resolution. Example: 1900x600
    """
    a_tags = soup.select('#article__content ul > li > a')
    a_tags = filter(lambda a: a.text.strip() == resolution, a_tags)

    hrefs = map(lambda a: a.get('href'), a_tags)
    hrefs = filter(bool, hrefs)
    return list(hrefs)


async def download_files(session, urls, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, url in enumerate(urls):
        parsed_url = urlparse(url)
        filename, ext = os.path.splitext(
            os.path.basename(parsed_url.path)
        )
        output_filename = os.path.join(
            output_dir, '%s.%s' % (filename, ext)
        )

        print(f"Downloadng {i}/{len(urls)}")
        async with session.get(url) as response:
            if response.status == 200:
                async with aiofiles.open(output_filename, 'wb') as writer:
                    await writer.write(await response.read())
            else:
                # TODO
                pass
