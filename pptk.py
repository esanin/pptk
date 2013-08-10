from pptx import Presentation
from os import listdir
from os.path import join


def main():
    path = "tests"
    files = listdir(path)
    presentations = []
    for pres in files:
        if pres.endswith('.pptx'):
            presentations.append(join(path,pres))

    for ppt in presentations:
        prs = Presentation(ppt)
        print len(prs.slides)

if __name__ == "__main__":
  main()