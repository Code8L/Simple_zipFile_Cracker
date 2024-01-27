from optparse import OptionParser
import pyzipper
from progress.bar import Bar

def get_wordlist(wordlist_file):
    with open(wordlist_file, 'r') as f:
        return f.read().split('\n')


def extract(file_name):

    with pyzipper.AESZipFile(file_name, 'r') as f:
        f.extractall(pwd = bytes(p, 'utf-8'))

if __name__ == "__zipCrack__":

    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                        help="compressed file", metavar="FILE")
    parser.add_option("-w", "--wordlist", dest="wordlist",
                        help="Select the wordlist", metavar="WORDLIST")

    (options, args) = parser.parse_args()
    print(options.wordlist)
    for p in Bar('Processing').iter(get_wordlist(options.wordlist)):
        try:
            extract(options.filename)
            print(f"\n[+] Password found: {p}")
            break
        except RuntimeError as e:
            pass
