import win32api
import win32con
import time
from Pascal import run_transcription_loop_slave

        
def change_window():
    win32api.keybd_event(win32con.VK_LWIN, 0, 0, 0)# WIN button ON
    win32api.keybd_event(win32con.VK_TAB, 0, 0, 0)#TAB button ON
    win32api.keybd_event(win32con.VK_TAB, 0, win32con.KEYEVENTF_KEYUP, 0)#TAB button OFF
    run_transcription_loop_slave()
    rtls = run_transcription_loop_slave()
    print(format(rtls))
    for cognates in rtls:
        if rtls == 'стоп':
            win32api.keybd_event(win32con.VK_LWIN, 0, win32con.KEYEVENTF_KEYUP, 0)#WIN button OFF
            quit()
    
    
            
        

    

