from core.linkedin import *

if not os.path.exists(CSVFILENAME) or not os.path.exists(TEXTFILENAME):
    print(
        f"Please put '{CSVFILENAME}' and '{TEXTFILENAME}' in current folder before running the program!!!")
else:
    newtest = LinkedIn()
    time.sleep(5)
    newtest.msgSending()
    time.sleep(2)
    newtest.closeWindow()
    deleteCSVFile(CSVFILENAME)
    print(f"{CSVFILENAME} has been deleted")
