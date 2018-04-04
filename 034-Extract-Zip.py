import os
import zipfile
import sys


def main(path='C:/Users/Leonardo/PycharmProjects/python-first-steps/saida.zip'):
    if not os.path.exists(path):
        print('Arquivo {} não existe'.format(path))
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall()
        print('Arquivo(s) extraído(s)')


if __name__ == "__main__":
    main()
