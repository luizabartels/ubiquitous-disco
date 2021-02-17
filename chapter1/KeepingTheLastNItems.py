# Keep limited history of the last few items seen during iteration or
# during some other kind of processing

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines # yield é semelhante ao return, porém retorna um generator
        previous_lines.append(line)
        
if __name__ == '__main__':
    with open('chapter1/somefile.txt') as f:
        for line, prevlines in search(f,'python', 10):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)