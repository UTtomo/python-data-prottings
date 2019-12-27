import eel

def main():
    # load web file
    eel.init("web")
    eel.start("main.html")


"""script when link1 pushed"""
# @eel.expose enables to be recognized by js
@eel.expose
def link1_click():
    null = 1
    print("link11_clicked%s" % null)

"""script when link1 pushed"""
@eel.expose
def link2_click(args):
    null = 2
    print(args)
    print("%s" % null)
    return "link2_clicked"

if __name__ == '__main__':
     main()