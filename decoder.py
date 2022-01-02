from scipy.io import wavfile
from scipy.fft import fft, fftfreq

import matplotlib.pyplot as plt
import numpy as np
import math
def roundup(x):
    x=x/100
    x=round(x)
    return x *100
    
all = {
    'a':[100,400,800,1600],
    'A':[200,400,800,1600],

    'b':[100,400,800,2400],
    'B':[200,400,800,2400],

    'c':[100,400,800,4000],
    'C':[200,400,800,4000],

    'd':[100,400,1200,1600],
    'D':[200,400,1200,1600],

    'e':[100,400,1200,2400],
    'E':[200,400,1200,2400],

    'f':[100,400,1200,4000],
    'F':[200,400,1200,4000],

    'g':[100,400,1600,2000],
    'G':[100,400,1600,2000],

    'h':[100,400,2000,2400],
    'H':[200,400,2000,2400],

    'i':[100,400,2000,4000],
    'I':[200,400,2000,4000],

    'j':[100,600,800,1600],
    'J':[200,600,800,1600],

    'k':[100,600,800,2400],
    'K':[200,600,800,2400],

    'l':[100,600,800,4000],
    'L':[200,600,800,4000],

    'm':[100,600,1200,1600],
    'M':[200,600,1200,1600],

    'n':[100,600,1200,2400],
    'N':[200,600,1200,2400],

    'o':[100,600,1200,4000],
    'O':[200,600,1200,4000],

    'p':[100,600,1600,2000],
    'P':[200,600,1600,2000],

    'q':[100,600,2000,2400],
    'Q':[200,600,2000,2400],
    
    'r':[100,600,2000,4000],
    'R':[200,600,2000,4000],

    's':[100,800,1000,1600],
    'S':[200,800,1000,1600],

    't':[100,800,1000,2400],
    'T':[200,800,1000,2400],

    'u':[100,800,1000,4000],
    'U':[200,800,1000,4000],

    'v':[100,1000,1200,1600],
    'V':[200,1000,1200,1600],

    'w':[100,1000,1200,2400],
    'W':[200,1000,1200,2400],

    'x':[100,1000,1200,4000],
    'X':[200,1000,1200,4000],

    'y':[100,1000,1600,2000],
    'Y':[200,1000,1600,2000],

    'z':[100,1000,2000,2400],
    'Z':[200,1000,2000,2400],

    ' ':[1000,2000,4000,100]
     
}


samplerate, data = wavfile.read('C:\\Users\\User\\Desktop\\DSP\\Project\\gogo.wav')
#C:\\Users\\User\\Desktop\\dspProj-main\\out1.wav
print(len(data))
print(samplerate)
loops = len(data)/320   
print(loops)
i1 = 0
i2 = 320
from scipy.fft import rfft, rfftfreq

max = [0,0,0,0]
'''
for i in range(len(xf)):
        if(yf[i] > max[0]):
            max[1]= max[0]
            max[0]=xf[i]
        elif(yf[i] > max[1]):
            max[2]=max[1]
            max[1]=xf[i]
        elif(yf[i] > max[2]):
            max[3]=max[2]
            max[2]=xf[i]
        elif(yf[i] > max[3]):
            max[3]=xf[i]
            
max=sorted(max)
print(max)
'''
#plt.plot(out)
#plt.show()

output =''
for k in range(int(loops)):
    seg = data[i1:i2]
    print(i1)
    print(i2)
    '''
    yf = fft(seg)
    N = 320
    T=1/8000
    xf =  fftfreq(N, T)[:N//2]
    threshold = 0
    yf[np.abs(yf)<threshold] = 0
   '''


  
    N=320
    yf = rfft(data[i1:i2])
    xf = rfftfreq(N, 1 / 8000)

    plt.plot(xf, np.abs(yf))
    plt.show()


    #plt.plot(xf, 2.0/N * np.abs(yf[0:N//2]))
    #plt.grid()
   # plt.show()
    max1=0
    max2=0
    max3=0
    max4=0
    max = [0,0,0,0]
    



    index = [0,0,0,0]
    for i in range(len(xf)):
        if(yf[i] > max[0]):
            max[3]= max[2]
            max[2] = max[1]
            max[1] = max[0]
            max[0]=yf[i]
            
            index[3]= index[2]
            index[2] = index[1]
            index[1] = index[0]
            index[0]=xf[i]
        elif(yf[i] > max[1]):
            max[3] = max[2]
            max[2] = max[1]
            max[1]=yf[i]
            
            index[3] = index[2]
            index[2] = index[1]
            index[1]=xf[i]
        elif(yf[i] > max[2]):
            max[3] = max[2]
            max[2]=yf[i]
            
            index[3] = index[2]
            index[2]=xf[i]
        elif(yf[i] > max[3]):
            max[3]=yf[i]
            
            index[3]=xf[i]
    print(sorted(index))

    index = sorted(index)
    print("------------------------")
    
    if(index[3] > 3900):
        index[3]=4000
   # print(max)
    key_list = list(all.keys())
    val_list = list(all.values())
    
    if(val_list.__contains__(index)):
        index  = val_list.index(index)
        output = output+key_list[index]      
    else:
        output = output+' '
        
    i1=i1+320
    i2=i2+320
    print(output)

print(output)
