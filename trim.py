import sys
from pathlib import Path

def trim_title(txt):
    spl = txt.split("INTRODUCTION")
    if len(spl) == 2:
        return spl[1]
    return txt

def trim_reference(txt):
    spl = txt.split("REFERENCES")
    if len(spl) == 2:
        return spl[0]
    return txt

if __name__ == '__main__':
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    txt = Path(input_path).read_text()
    txt = trim_title(txt)
    txt = trim_reference(txt)

    with open(output_path, 'w') as f:
        f.write(txt)
