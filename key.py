import curses

li=["option 1","option 2","option 3","option 4"]

def cycle(a,b,n):
    if(n<a):
        return b
    if(n>b):
        return a
    return n
def menu(stdscr,p):
    for i,r in enumerate(li):
        x=0
        y=0+i
        h=len(r)
        if i==p:
            # stdscr.addstr(y,h,"<")
            stdscr.addstr(y,x,"> "+r)
        else:
            stdscr.addstr(y,x,"  "+r)


def fun(stdscr):
    curses.curs_set(0)
    p=0
    menu(stdscr,p)
    while 1:
        key= stdscr.getch()

        stdscr.addstr(10,0,str(key))

        if key == curses.KEY_UP:
            #stdscr.addstr(0,0,"up key pressed")
            p=p-1

        elif key ==curses.KEY_DOWN:
            #stdscr.addstr(0,0,"down key pressed")
            p=p+1
        elif key == curses.KEY_:
            p+=3

        p = cycle(0,len(li)-1, p)
        menu(stdscr,p)
        stdscr.refresh()
curses.wrapper(fun)