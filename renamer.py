import os
import shutil
from pandas import read_csv, DataFrame
import datetime


def header_reader(df):
    if df.columns[0] != 'CPM':
        df = read_csv(args.filename, header=None)
        print(df.columns)
        df.columns = ['CPM', 'uSv/h', 'Vcc', 'Datetime']
        print(df.columns)
        return df
    else:
        print(df.columns)
        df.columns = ['CPM', 'uSv/h', 'Vcc', 'Datetime']
        print(df.columns)
        return df


def append_and_move(df, filename):
    with open('master.csv', 'a') as f:
        df.to_csv(f, header=False, index=False)
    df.to_csv(filename, mode='w', index=False)
    shutil.copyfile(filename, 'daily/%s' % filename)


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-f', '--filename', dest='filename', default=str(datetime.date.today())+'.csv')

    args = parser.parse_args()

    df = read_csv(args.filename)

    # header_reader(df)
    append_and_move(header_reader(df), args.filename)
