from os import listdir
from os.path import isfile, join
import os, requests

currentdir = os.path.dirname(__file__)

def main(path):
    # retrieve list of files from path given
    onlyfiles = [ f for f in listdir(path) if isfile(join(path,f)) ]
    # split files and cut off extension
    filenames = [ fn.split('_')[1][:-4] for fn in onlyfiles]
    for app in filenames:
        # set up url from Steam database using AppID
        url = "http://cdn.akamai.steamstatic.com/steam/apps/%s/header.jpg" % app
        # retrieve path of soon-to-be-made file
        path = os.path.join(currentdir, app + '.jpg')
        # open file to add/replace
        file = open(path, 'wb')
        # retrieve data
        fp = requests.get(url)
        # write data to file
        for block in fp.iter_content(1024):
            if not block:
                break

            file.write(block)
        # close file
        file.close()
        print 'Banner downloaded for app: ' + app
if __name__ == '__main__':
    path = raw_input('Steam Library Path: ')
    main(path)