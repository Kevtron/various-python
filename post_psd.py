import pylab as plt
import numpy as np
import os
import netCDF4
import sys
import shutil
import subprocess


UMAX = 1.4
def plot_frame(n=-1):
    j=225 # z=10
    k=28 # x=1
    vis = netCDF4.Dataset('vis.nc')
    #values
    
    U = vis.variables['U'][n,0,:,:] 
    UHTS = vis.variables['U'][:,0,j,:]
    UVTS = vis.variables['U'][:,0,:j,k]
    #grid stuff
    x = vis.variables['x'][:]
    yf = vis.variables['yf'][:]
    t = vis.variables['t'][:]
    vis.close

    interpolation = 'nearest'
    aspect = 'auto'

    dt = np.mean(np.diff(t))
    plt.subplot(311)
    #plt.plot(k,y,'k-',linewidth=2)
    #plt.plot(x,j,'k-',linewidth=2)
    plt.axhline(y=yf[j])
    plt.axvline(x=x[k])
    #plot horizontal velocity
    plt.ylim(ymin=-7,ymax = 0)
    plt.imshow(U, origin='lower', aspect=aspect,
    interpolation=interpolation,
    vmin = -UMAX, vmax = UMAX, 
    extent=[x[0], x[-1], yf[0], yf[-1]])

    plt.colorbar()
    plt.title('U, frame %d' % n)
    plt.xlabel('x')
    plt.ylabel('z')

    #compute power spectral density x
    plt.subplot(312)
    plt.ylim(ymin=-230,ymax=10)
    plt.xlim(xmin=0,xmax=10)
    plt.psd(UHTS[n,:], NFFT=len(UHTS[n,:]), Fs=(2*np.pi)/(dt))        

    #compute power spectral density z
    plt.subplot(313)
    plt.ylim(ymin=-80,ymax=0)
    #plt.xlim(xmin=0,xmax=10)
    plt.psd(UVTS[n,:], NFFT=len(UVTS[n,:]), Fs=(2*np.pi)/(dt))        


def shifted_horizontal_psd(n=-1):
    j1 = 225
    j2 = 175
    j3 = 125
    
    vis = netCDF4.Dataset('vis.nc')

    U1 = vis.variables['U'][:,0,j1,:]
    U2 = vis.variables['U'][:,0,j2,:]
    U3 = vis.variables['U'][:,0,j3,:]
    x = vis.variables['x'][:]
    yf = vis.variables['yf'][:]
    t = vis.variables['t'][:]
    vis.close

    dt = np.mean(np.diff(t))
    plt.subplot(311)
    plt.ylim(ymin=-230,ymax=10)
    plt.xlim(xmin=0,xmax=10)    
    plt.psd(U1[n,:], NFFT = len(U1[n,:]), Fs=(2*np.pi)/(dt))
    
    plt.subplot(312)
    plt.ylim(ymin=-230,ymax=10)
    plt.xlim(xmin=0,xmax=10)    
    plt.psd(U2[n,:], NFFT = len(U2[n,:]), Fs=(2*np.pi)/(dt))
    
    plt.subplot(313)
    plt.ylim(ymin=-230,ymax=10)
    plt.xlim(xmin=0,xmax=10)    
    plt.psd(U3[n,:], NFFT = len(U3[n,:]), Fs=(2*np.pi)/(dt))

def make_movie():
    vis = netCDF4.Dataset('vis.nc')
    t = vis.variables['t'][:]
    vis.close

    num_frames = len(t)
    dt = np.mean(np.diff(t))
    fps = 5
    print 'fps = ' , fps
    print 'dt = ' , dt 

    if not os.path.exists('psdframes'):
        os.mkdir('psdframes')

#lets build a movie
    plt.figure(figsize=(12,8))
    for n in range(num_frames):
        frame = 'psdframes/frame_%04d.png' % n
        if not os.path.exists(frame):
            print 'Creating frame %d/%d' % (n+1, num_frames)
            try:
                plt.clf()
                plot_frame(n)
                plt.savefig(frame, dpi=100)
            except:
                break

    subprocess.call(['ffmpeg', 
                    '-r', '%.0f' % fps,
                    '-i', 'psdframes/frame_%04d.png',
                    #'-s', '1200x800',
                    '-b', '5000k',
                    '-bt', '5000k',
                    '-y',
                    'movie.mov'])


def make_timeseries_stack():
    vis = netCDF4.Dataset('vis.nc')
    t = vis.variables['t'][:]
    vis.close

    num_frames = len(t)
    dt = np.mean(np.diff(t))
    fps = 5
    print 'fps = ' , fps
    print 'dt = ' , dt 

    if not os.path.exists('psdframes1'):
        os.mkdir('psdframes1')

#lets build a movie
    plt.figure(figsize=(12,8))
    for n in range(num_frames):
        frame = 'psdframes1/frame_%04d.png' % n
        if not os.path.exists(frame):
            print 'Creating frame %d/%d' % (n+1, num_frames)
            try:
                plt.clf()
                shifted_horizontal_psd(n)
                plt.savefig(frame, dpi=100)
            except:
                break

    subprocess.call(['ffmpeg', 
                    '-r', '%.0f' % fps,
                    '-i', 'psdframes1/frame_%04d.png',
                    #'-s', '1200x800',
                    '-b', '5000k',
                    '-bt', '5000k',
                    '-y',
                    'psdmovie.mov'])
            
        
#Let's load some data
#U(t,z,y,x)

if __name__== '__main__':
    make_movie()
    make_timeseries_stack()
##subprocess.call(['opt/local/bin/ffmpeg', 
##                '-r', '%.0f' % fps,
##                '-i', './test/frame_%04d.png',
##            #   '-s', '1200x800',
##                '-b', '5000k',
##                '-bt', '5000k',
##                '-y',
##                'test/movie.mov'])

