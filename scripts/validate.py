import sys
import yaml

def parse_pada_urai(pada_urai_filename: str):
    pada_urai_file = open(pada_urai_filename, "r")
    words = yaml.load(pada_urai_file, Loader=yaml.FullLoader)
    pada_urai_file.close()
    # Return a dictionary of words.
    return words.keys()

def read_verse(verse_filename: str):
    with open(verse_filename, "r") as file:
        # Return entire file as a string.
        s = file.read()
        # Replace pause markers.
        s_new = s.replace(" *", "").replace("\n","")
        #print(s_new)
        return s_new


def main(args):
    words = parse_pada_urai(args[0])
    # print(words)
    verse = read_verse(args[1])
    found = dict()
    extents = []
    for w in words:
        pos = verse.find(w)
        extents.append((pos, len(w)))
    extents.sort()
    for i, e in enumerate(extents):
        #print(e)
        if i > 0:
            prev = extents[i-1]
            prev_end = prev[0] + prev[1]
            s = verse[prev_end:e[0]].strip()
            if len(s) and s not in ['க்', 'ச்', 'ப்']:
                    #print(prev_end, e[0])
                    #print(repr(s))
                    print(s)


if __name__ == "__main__":
    args = sys.argv[1:]
    #print(args[0])
    main(args)







