import os
import argparse


def main(database: str, url_list_file: str):
    print(f'we are going to work with {database}')
    print(f'we are going to scan {url_list_file}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-db', '--database', help='SQLite File Name')
    parser.add_argument('-i', '--input', help='File containing URLs to read')
    args = parser.parse_args()
    main(args.database, args.input)
