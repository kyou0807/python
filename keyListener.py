
import time
import threading
from pynput import keyboard
from loopMain import *
from stopThread import *
from myButtonObj import *
t = None  
beginTime=None

#奥元素0-4s开 满勾玉循环-黑人起手 (两发陨石)
fullLoopBtn=keyboard.Key.f2
# 火2s-电1.5s 0勾玉不满-黑人起手 (两发陨石)
zeroLoopBtn=keyboard.Key.f3
# 火3.5-电3开 满勾玉循环-陨石起手 (两发陨石)
meteorite_fullLoopBtn=keyboard.Key.f4


# 棒棒糖模式  一键黑人+开罩子+0.6s一次一技能
Lollipop=keyboard.Key.f2



class keyListener(object):

    def __init__(self, myButtonObj):
        self.myButtonObj=myButtonObj

    def on_press(self,key):
        pass
    def on_release(self,key):
        lm=loopMain(self.myButtonObj)
        st=stopThread()
        global t

        if not self.myButtonObj.modeFlag:
            if key==fullLoopBtn:
                if t is not None:
                    try:
                        st.stop_thread(t)
                    except:
                        print("宏已关闭")
                        print("线程已结束")
                        t = None
                    else:
                        print("宏已关闭")
                        t = None
                else:
                    t = threading.Thread(target=lm.fullLoop, args=([30]))
                    t.start()
            elif key==zeroLoopBtn:
                if t is not None:
                    try:
                        st.stop_thread(t)
                    except:
                        print("宏已关闭")
                        print("线程已结束")
                        t = None
                    else:
                        print("宏已关闭")
                        t = None
                else:
                    t = threading.Thread(target=lm.zeroLoop, args=([30]))
                    t.start()
            elif key==meteorite_fullLoopBtn:
                if t is not None:
                    try:
                        st.stop_thread(t)
                    except:
                        print("宏已关闭")
                        print("线程已结束")
                        t = None
                    else:
                        print("宏已关闭")
                        t = None
                else:
                    t = threading.Thread(target=lm.meteorite_fullLoop, args=([30]))
                    t.start()
        else:   
           # 棒棒糖模式
            if key==Lollipop:
                global beginTime
                if beginTime is not None:
                    print(time.time()-beginTime)
                    if time.time()-beginTime>21:
                       t = None
                       beginTime=time.time()
                    else:
                        beginTime = None
                else:
                    beginTime=time.time()
                
                if t is not None:
                    try:
                        st.stop_thread(t)
                    except:
                        print("宏已关闭")
                        print("线程已结束")
                        t = None
                    else:
                        print("宏已关闭")
                        t = None
                else:
                    t = threading.Thread(target=lm.Lollipop)
                    t.start()
        
        if key==keyboard.Key.f11:
            if t is not None:
                try:
                   st.stop_thread(t)
                except:
                    print("宏已关闭")
                    print("线程已结束")
                    t = None
                else:
                    print("宏已关闭")
                    t = None
        elif key==keyboard.Key.f12:
            return False
    
    def onListener(self):
        print('开启监听....')
        with keyboard.Listener(on_press=self.on_press,on_release=self.on_release) as listener:
            listener.join()