from Bio import SeqIO
from Bio.Alphabet import generic_protein
import ttk, tkFileDialog, ntpath
from Tkinter import *
from tkFileDialog import askopenfilename

def Conversion(input_file,input_format,output_format):
	if (input_format == output_format):
		z.set("File already in " + input_format + " format")
	else:
		SeqIO.convert(input_file,input_format,("output."+output_format),output_format)
		z.set("Resulting file saved to Output."+output_format)
		root.update_idletasks()



def file_check():
	root.fileName = askopenfilename()
        if not root.fileName:
            print("You didn't select a file")
        else:
				z.set(ntpath.basename(root.fileName) + " selected")
				root.update_idletasks()
class myGUI:
    def __init__(self, master):
		#variables
		optionlist = ('fasta','fasta','clustal','stockholm','fastq','pir','nexus','tab')
		global var, var2, z
		self.var = StringVar()
		self.var.set(optionlist[0])
		self.var2 = StringVar()
		self.var2.set(optionlist[0])  
		z = StringVar()
		z.set("                           ")
		#frames
		global MainFrame
		MainFrame = Frame(master)
		MainFrame.pack()     
		#labels
		self.label_1 = Label(MainFrame, text ="Input Format:")
		self.label_1.grid(row=1,column=0)
		self.label_2 = Label(MainFrame, text ="Output Format:")
		self.label_2.grid(row=2,column=0)
		self.label_3 = Label(MainFrame, textvariable = z)
		self.label_3.grid(row=0,column=4,sticky=W+E+N+S,columnspan=2)		
		#buttons
		self.button_1 = ttk.Button(MainFrame, text="Select File to Convert", command=lambda: file_check())
		self.button_1.grid(row=0,sticky=W,columnspan=4)
		self.button_2 = ttk.Button(MainFrame, text="Convert", command=lambda: Conversion(root.fileName,self.var.get(),self.var2.get()))
		self.button_2.grid(row=3,sticky=W+E,columnspan=6)
		#checkbuttons
		self.dropdown1 = ttk.OptionMenu(MainFrame, self.var, *optionlist)
		self.dropdown1.grid(row=1,column=1)  
		self.dropdown2 = ttk.OptionMenu(MainFrame, self.var2, *optionlist)
		self.dropdown2.grid(row=2,column=1)           
		master.resizable(0,0)
		master.title("Quick Conversion v1.0")


def main():
    global root
    root = Tk()
    window = myGUI(root)
    root.mainloop()
    
if __name__ == '__main__': main()
