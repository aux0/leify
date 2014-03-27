from __future__ import print_function
import argparse

EPILOG = '''
examples:
  your hue a hue
    le your le hue le a le hue

  hello there world!
    le hello le there le world!
'''

def leify(text):
    return 'le ' + ' le '.join(text.split())

def main():
    parser = argparse.ArgumentParser(prog='leify', epilog=EPILOG, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('text', help='the text to be leified')
    args = parser.parse_args()

    print(leify(args.text))

if __name__ == '__main__':
    main()
