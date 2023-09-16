def coletaveis2(stdscr):
    colet2 = [[5, 11], [29, 25], [14,125], [10,65], [28,50]]
    for i in range(len(colet2)):
        stdscr.addch(colet2[i][0], colet2[i][1], curses.ACS_DIAMOND)

def coletaveis1(stdscr):
    colet1 = [[11,21],[29,20], [13,125], [9,65], [17,30], [31,35], [26,92]]
    for i in range(len(colet1)):
        stdscr.addch(colet1[i][0], colet1[i][1], curses.ACS_DIAMOND)