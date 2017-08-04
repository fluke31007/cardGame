import sys
import getpass
if not "C:/Users/"+getpass.getuser()+"/Documents/gitfolder/CardGame"in sys.path:
    sys.path.append("C:/Users/"+getpass.getuser()+"/Documents/gitfolder/CardGame")
import CardGame.Gui as Gui_Card
reload(Gui_Card)