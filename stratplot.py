import numpy as np
import pylab as plt
import os
from Tkinter import *
from time import strftime

class Calc( Frame ):
   def __init__( self):
      Frame.__init__( self , bd=2, relief = SUNKEN, bg = 'light grey')
      self.master.title( "Stratification Frequency Calculator" )

      self.master.rowconfigure( 0, weight = 1 )
      self.master.columnconfigure( 0, weight = 1 )
      self.grid( sticky = W+E+N+S )

        #create the labels
      self.label1 = Label( self, text="Density (g/cm^2)" )
      self.label1.grid(row=0, column = 0, sticky = W+E+N+S )

      self.label2 = Label( self, text="Depth (cm)")
      self.label2.grid(row=0, column = 1, sticky = W+E+N+S )

      self.filename = StringVar()
      self.entry = Entry( self, textvariable = self.filename )
      self.entry.grid( row = 7, column = 2, sticky = W+E+N+S )
      self.entry.insert( INSERT, "Filename")

      self.title = StringVar()
      self.entrytitle = Entry( self, textvariable = self.title )
      self.entrytitle.grid( row = 8, column = 2, sticky = W+E+N+S )
      self.entrytitle.insert( INSERT, "Title")
      
        # density fields
      self.dens1 = DoubleVar()
      self.entry1 = Entry( self, textvariable = self.dens1 )
      self.entry1.grid( row = 1, column = 0, sticky = W+E+N+S )

      self.dens2 = DoubleVar()
      self.entry2 = Entry( self, textvariable = self.dens2 )
      self.entry2.grid( row = 2, column = 0, sticky = W+E+N+S )

      self.dens3 = DoubleVar()
      self.entry3 = Entry( self, textvariable = self.dens3 )
      self.entry3.grid( row = 3, column = 0, sticky = W+E+N+S )

      self.dens4 = DoubleVar()
      self.entry4 = Entry( self, textvariable = self.dens4 )
      self.entry4.grid( row = 4, column = 0, sticky = W+E+N+S )

      self.dens5 = DoubleVar()      
      self.entry5 = Entry( self, textvariable = self.dens5 )
      self.entry5.grid( row = 5, column = 0, sticky = W+E+N+S )

      self.dens6 = DoubleVar()      
      self.entry6 = Entry( self, textvariable = self.dens6 )
      self.entry6.grid( row = 6, column = 0, sticky = W+E+N+S )
      
      self.dens7 = DoubleVar()
      self.entry7 = Entry( self, textvariable = self.dens7 )
      self.entry7.grid( row = 7, column = 0, sticky = W+E+N+S )

      self.dens8 = DoubleVar()
      self.entry8 = Entry( self, textvariable = self.dens8 )
      self.entry8.grid( row = 8, column = 0, sticky = W+E+N+S )
      
        #Depth fields

      self.depth1 = DoubleVar()
      self.entry9 = Entry( self, textvariable = self.depth1 )
      self.entry9.grid( row = 1, column = 1, sticky = W+E+N+S )

      self.depth2 = DoubleVar()      
      self.entry10 = Entry( self, textvariable = self.depth2 )
      self.entry10.grid( row = 2, column = 1, sticky = W+E+N+S )

      self.depth3 = DoubleVar()      
      self.entry11 = Entry( self, textvariable = self.depth3 )
      self.entry11.grid( row = 3, column = 1, sticky = W+E+N+S )

      self.depth4 = DoubleVar()      
      self.entry12 = Entry( self, textvariable = self.depth4 )
      self.entry12.grid( row = 4, column = 1, sticky = W+E+N+S )

      self.depth5 = DoubleVar()      
      self.entry13 = Entry( self, textvariable = self.depth5 )
      self.entry13.grid( row = 5, column = 1, sticky = W+E+N+S )

      self.depth6 = DoubleVar()      
      self.entry14 = Entry( self, textvariable = self.depth6 )
      self.entry14.grid( row = 6, column = 1, sticky = W+E+N+S )

      self.depth7 = DoubleVar()      
      self.entry15 = Entry( self, textvariable = self.depth7 )
      self.entry15.grid( row = 7, column = 1, sticky = W+E+N+S )

      self.depth8 = DoubleVar()      
      self.entry16 = Entry( self, textvariable = self.depth8 )
      self.entry16.grid( row = 8, column = 1, sticky = W+E+N+S )
      
        # create the buttons 
      self.button1 = Button( self, text = "Plot Data", width = 25, command = self.plot )
      self.button1.grid( row = 0, column = 2, rowspan = 2, sticky = W+E+N+S )

      self.button2 = Button( self, text = "Plot Line of Best Fit", command = self.fit )
      self.button2.grid( row = 2, column = 2, rowspan = 2, sticky = W+E+N+S )

      self.button3 = Button( self, text = "Calculate N", command = self.showN )
      self.button3.grid( row = 4, column = 2, rowspan = 2 ,sticky = W+E+N+S )

      self.button4 = Button( self, text = "Save Plot", command = self.save )
      self.button4.grid( row = 6, column = 2, rowspan = 1 ,sticky = W+E+N+S )
      
      self.button4 = Button( self, text = "Get Data", command = self.getVal )
      self.button4.grid( row = 9, column = 0, columnspan = 3 ,sticky = W+E+N+S )

      self.rowconfigure( 1, weight = 1 )
      self.columnconfigure( 1, weight = 1 )

   def getVal(self):
       global x
       global y
       try:
           x=np.array([float(self.entry1.get()),float(self.entry2.get()),float(self.entry3.get()),float(self.entry4.get()),float(self.entry5.get()),float(self.entry6.get()),float(self.entry7.get()),float(self.entry8.get())])
           y=np.array([float(self.entry9.get()),float(self.entry10.get()),float(self.entry11.get()),float(self.entry12.get()),float(self.entry13.get()),float(self.entry14.get()),float(self.entry15.get()),float(self.entry16.get())])
       except ValueError:
           tkMessageBox.showerror(message = "Value must be a number")

   def fit(self):
       global x
       global y
       global m
       A=np.vstack([y,np.ones(len(y))]).T
       m,c = np.linalg.lstsq(A,x)[0]
       plt.plot(m*y+c,y,'r',label='Fitted line')
       plt.draw()

   def plot(self):
       global x
       global y
       plt.xlabel('Density (g/cm^3)')
       plt.ylabel('Depth (cm)')
       plt.title('%s %s ' % (self.entrytitle.get(), strftime("%Y-%m-%d %H:%M:%S")))
       plt.plot(x,y,'ro', label='Original Data')
       plt.show()
    
   def showN(self):
       global m
       plt.text(float(self.entry2.get()),float(self.entry15.get()),'N=%0.2f $s^{-1}$'%  np.sqrt(-980*m))
       plt.draw()


   def save(self):
       plt.savefig('%s-%s.png' % (self.entry.get(), strftime("%a-%h-%d")))
       #on linux, change to xpdf
       os.system('open %s-%s.png' % (self.entry.get(), strftime("%a-%h-%d")))
       plt.clf()

#-----------#
# Main Stuff#
#-----------#
def main():
    Calc().mainloop()   

if __name__ == "__main__":
   main()                  
