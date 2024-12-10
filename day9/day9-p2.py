# this thing took wayyyyy too much to implement
# guess i'm stupid


def expand(m: list[tuple[int, int, bool]]) -> list[int, str]:
    blocks = []
    for t in m:
        if t[2]:
            for _ in range(0, t[1]):
                blocks.append(t[0])
        else:
            for _ in range(0, t[1]):
                blocks.append('.')
    return blocks

def merge_blocks(m: list[tuple[int, int, bool]]) -> list[int, str]:
    i, j = 0, 1
    while j < len(m):
        if m[i][2] == m[j][2] == False:
            m = m[:i] + [(0, m[i][1]+m[j][1], False)] + m[j+1:]
        i += 1
        j += 1

    return m


def find_index(m: list[tuple[int, int, bool]], id: int) -> int:
    i = 0
    for t in m:
        if t[0] == id:
            return i
        else:
            i += 1
    return -1


def main():
    with open("input.txt", "r") as f:
        disk_map = list(map(int, list(f.read().strip())))

        imap = []
        max_id = 0

        for i, n in enumerate(disk_map):
            imap.append((i//2 if i%2==0 else 0, n, i%2==0))
            if i%2==0:
                max_id = i//2

        r_index = find_index(imap, max_id)
        while r_index > 0:
            if imap[r_index][2]:
                l_index = 0
                while l_index < len(imap):
                    l_index += 1
                    if l_index < len(imap) and not imap[l_index][2] and imap[l_index][1] >= imap[r_index][1] and l_index < r_index:
                        e = imap.pop(r_index)
                        imap = imap[:r_index] + [(0, e[1], False)] + imap[r_index:]
                        imap = imap[:l_index] + [e] + [(0, imap[l_index][1]-e[1], False)] + imap[l_index+1:]
                        imap = merge_blocks(imap)
                        break
                max_id -= 1
                r_index = find_index(imap, max_id)
            else:
                r_index-=1
                

        blocks = expand(imap)

        checksum = 0

        for i, n in enumerate(blocks):
            if n != '.':
                checksum += i*n

        print(checksum)

if __name__ == "__main__":
    main()