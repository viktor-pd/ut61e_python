import sys
import os
import subprocess

def mm_readout_simple(*args):
    """Prints the Python version into the current document"""
#get the doc from the scripting context which is made available to all scripts
    desktop = XSCRIPTCONTEXT.getDesktop()
    model = desktop.getCurrentComponent()
#check whether there's already an opened document. Otherwise, create a new one
    if not hasattr(model, "Sheets"):
        model = desktop.loadComponentFromURL(
            "private:factory/scalc","_blank", 0, () )
#get the XText interface
    #sheet = model.Sheets.getByIndex(0)
#create an XTextRange at the end of the document
    #tRange = sheet.getCellRangeByName("C4")
    tRange = model.getCurrentSelection()
#and set the string
    if hasattr(tRange,'String'):
        data = subprocess.check_output(['bash','-c','he2325u_pyusb | es51922 -m baresingle'],timeout=3)
        # ps = subprocess.Popen('bash -c "he2325u_pyusb | es51922 -m baresingle"',stdout=subprocess.PIPE)
        # data = ps.communicate(timeout=3)[0]
        # data = os.popen('he2325u_pyusb | es51922 -m baresingle').read()
        # data = subprocess.check_output('ls')
        tRange.Value = float(data)
#do the same for the python executable path
    # tRange = sheet.getCellRangeByName("C5")
    # tRange.String = sys.executable
    return None
