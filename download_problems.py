# -*- coding: utf-8 -*-
"""
    Script to download the problems as separate text files.
"""

##### IMPORTS #####
# Standard imports
from pathlib import Path
from argparse import ArgumentParser

# Third party imports
import requests
import bs4
from tqdm import tqdm

##### FUNCTIONS #####
def parseProblemPage(page):
    """ Parse the html of a given Project Euler problem page.

    Parameters
    ----------
    page: str
        Html string of a problem page from Project Euler.

    Returns
    -------
    number: int
        The number of the problem.
    name: str
        The name of the problem.
    content: str
        The description of the problem.
    """
    parser = bs4.BeautifulSoup(page, 'html.parser')
    nm = parser.select('h2')[0].getText()

    # Get the number and convert to int
    num = parser.select('#problem_info')[0].getText()
    num = int(num.split()[1])

    # Get the content and format it for markdown output
    cont = parser.select('.problem_content')[0].getText()
    # Add blank line between each paragraph
    cont = cont.replace('\n', '\n\n').strip()

    return num, nm, cont

def requestProblems(start=1, end=None):
    """ Generator for requesting Project Euler problem pages.

    Parameters
    ----------
    start: int, optional
        The problem number to start at, default 1.
    end: int, optional
        The problem number to end at, default None (will end
        when there are no more problems)

    Yields
    ------
    page: requests.Response
        The problem page Response object.
    """
    num = start
    while True:
        if end is not None and num > end:
            return StopIteration

        # Request page and check the url is the same because the website redirects
        # to archives if problem doesn't exist
        url = PE_URL + f'problem={num}'
        req = requests.get(url)
        req.raise_for_status()
        if req.url != url:
            # Stop generator when problem doesn't exist
            return StopIteration

        yield req
        num += 1

def saveProblem(num, name, content, url):
    """ Saves the problem information to a markdown file in problems folder.

    Parameters
    ----------
    num: int
        The number of the problem.
    name: str
        The name of the problem.
    content: str
        The content text of the problem (markdown format).
    url: str
        The url for the problem page.
    """
    # Only include first 5 words of name
    try:
        filename = name.split()[:4]
    except IndexError:
        filename = name.split()
    filename = '_'.join(filename)

    # Exclude special characters from filenames
    for x in ('\\', '/', '?', '"', '\'', '...', ',',
              '..', '$', '<', '>', '|', ':', ';'):
        filename = filename.replace(x, '')
    # Add number to start
    filename = f'{num!s:0>3.3}-{filename}'

    # Paths for the md file and solution file
    problemPath = OUTPUT_FOLDER / (filename + '.md')
    scriptPath = OUTPUT_FOLDER / f'../solutions/{filename}.py'
    exist = '' if scriptPath.exists() else ' - not been created.'

    # Create markdown text and write to file
    text = (f"# Problem {num} - {name}"
            f"\n\n[Problem Page]({url})"
            f"\n\n[Solution Script]({scriptPath.relative_to(OUTPUT_FOLDER)}){exist}"
            f"\n\n{content}")
    with open(problemPath, 'wb') as f:
        f.write(text.encode('utf8'))

    return

def argParser():
    """ Creates the ArgumentParser to accept certain arguments. """
    parser = ArgumentParser(description=('Downloads problems from Project Euler'
                                         ' and saves copies locally.'))
    parser.add_argument('-s', '--start', type=int, default=1,
                        help='The problem number to start the downloads at, default 1.')
    parser.add_argument('-e', '--end', type=int, default=None,
                        help='The problem number to end the downloads at, default None.')
    return parser

##### CONSTANTS #####
PE_URL = "https://projecteuler.net/"
OUTPUT_FOLDER = Path('problems')

##### MAIN #####
if __name__ == '__main__':
    args = argParser().parse_args()

    if args.end is not None:
        print(f'Getting problems {args.start} - {args.end}')
        total = args.end - args.start + 1
    else:
        print(f'Getting all problems from {args.start}')
        total = None

    for probPage in tqdm(requestProblems(args.start, args.end), unit=' saved',
                         total=total, desc='Downloading and saving problems'):
        saveProblem(*parseProblemPage(probPage.text), probPage.url)

    print('Done problems are saved in:', OUTPUT_FOLDER.absolute().relative_to(Path.cwd()))
