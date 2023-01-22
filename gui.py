import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_appearance_mode("Dark")

class App(customtkinter.CTk):

    WIDTH = 800
    HEIGHT = 480

    load=""
    detergent=""
    softner="off"

    def __init__(self):
        super().__init__()

        self.title("GUI")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)

        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        #label
        self.label_level = customtkinter.CTkLabel(master=self.frame_left,
                                             text="Levels",
                                              text_font=("Roboto Medium", -30))  # font name and size in px
        self.label_level.grid(row=1, column=0,columnspan=4, pady=20, padx=0)
    
        #progress bar
        #B
        self.progressbar_B=customtkinter.CTkProgressBar(master=self.frame_left,orient='vertical',height=250)
        self.progressbar_B.grid(row=2, column=0, sticky="ew", padx=15, pady=0)
        
        self.label_B = customtkinter.CTkLabel(master=self.frame_left,width=8,
                                             text="B",text_font=("Roboto Medium", -20))
                                        
        self.label_B.grid(row=3, column=0,columnspan=1, pady=0, padx=0)
        #W
        self.progressbar_W=customtkinter.CTkProgressBar(master=self.frame_left,orient='vertical',height=250)
        self.progressbar_W.grid(row=2, column=1, sticky="ew", padx=15, pady=0)
        
        self.label_B = customtkinter.CTkLabel(master=self.frame_left,width=8,
                                             text="W",text_font=("Roboto Medium", -20))
                                    
        self.label_B.grid(row=3, column=1, pady=0, padx=0)
        #C
        self.progressbar_C=customtkinter.CTkProgressBar(master=self.frame_left,orient='vertical',height=250)
        self.progressbar_C.grid(row=2, column=2, sticky="ew", padx=15, pady=0)
        
        self.label_C = customtkinter.CTkLabel(master=self.frame_left,width=8,
                                             text="C",text_font=("Roboto Medium", -20))
                                    
        self.label_C.grid(row=3, column=2, pady=0, padx=0)
        #D
        self.progressbar_D=customtkinter.CTkProgressBar(master=self.frame_left,orient='vertical',height=250)
        self.progressbar_D.grid(row=2, column=3, sticky="ew", padx=15, pady=0)
        
        self.label_D = customtkinter.CTkLabel(master=self.frame_left,width=8,
                                             text="D",text_font=("Roboto Medium", -20))
                                    
        self.label_D.grid(row=3, column=3, pady=0, padx=0)
      
        #setting button
        self.button_setting = customtkinter.CTkButton(master=self.frame_left,
                                                text="Settings",
                                                text_font=("Roboto Medium", -20),
                                              fg_color='#1931df',
                                              command=self.button_event)
        self.button_setting.grid(row=7, column=0,columnspan=4, pady=10, padx=0) 
  

        # ============ frame_right ============

 
        self.frame_right.grid_columnconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, minsize=0)   # empty row with minsize as spacing
        self.frame_right.grid_rowconfigure(4, minsize=20)  # empty row as spacing
        self.frame_right.grid_rowconfigure(7, minsize=20)    # empty row with minsize as spacing
        self.frame_right.grid_rowconfigure(9, minsize=50)  # empty row with minsize as spacing
        #load lavel
        self.label_load = customtkinter.CTkLabel(master=self.frame_right,
                                              text="Load",
                                              anchor="nw",   
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.label_load.grid(row=1, column=0, pady=10, padx=0)

        #small button
        self.button_samll = customtkinter.CTkButton(master=self.frame_right,
                                                text="Small",
                                                text_font=("Roboto Medium", -20),
                                                fg_color='#1931df',
                                                command=lambda:self.button_event1("Small"))
        self.button_samll.grid(row=2, column=0, pady=0, padx=20)

        self.label_small = customtkinter.CTkLabel(master=self.frame_right,
                                              text="4-5KG",
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.label_small.grid(row=3, column=0, pady=0, padx=0)

        #medium button
        self.button_medium = customtkinter.CTkButton(master=self.frame_right,
                                                text="Medium",
                                                text_font=("Roboto Medium", -20),
                                                fg_color='#1931df',
                                                command=lambda:self.button_event1("Medium"))
        self.button_medium.grid(row=2, column=1, pady=0, padx=20)

        self.label_medium = customtkinter.CTkLabel(master=self.frame_right,
                                              text="6-8KG",
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.label_medium.grid(row=3, column=1, pady=0, padx=0)
        

        #heavy button
        self.button_heavy = customtkinter.CTkButton(master=self.frame_right,
                                                text="Heavy",
                                                text_font=("Roboto Medium", -20),
                                                fg_color='#1931df',
                                                command=lambda:self.button_event1("Heavy"))
        self.button_heavy.grid(row=2, column=2, pady=0, padx=20)

        self.label_heavy = customtkinter.CTkLabel(master=self.frame_right,
                                              text="9+KG",
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.label_heavy.grid(row=3, column=2, pady=0, padx=0)
        
        #detergent lavel
        self.label_load = customtkinter.CTkLabel(master=self.frame_right,
                                              text="Detergent",
                                              anchor="nw",
                                              text_font=("Roboto Medium", -20))  # font name and size in px
        self.label_load.grid(row=5, column=0, pady=10, padx=0)
        
        #black button
        self.button_black = customtkinter.CTkButton(master=self.frame_right,
                                                text="Black",
                                                text_font=("Roboto Medium", -20),
                                                fg_color='#1931df',
                                                command=lambda:self.button_event2("Black"))
        self.button_black.grid(row=6, column=0, pady=0, padx=20)


        #white button
        self.button_white = customtkinter.CTkButton(master=self.frame_right,
                                                text="White",
                                                text_font=("Roboto Medium", -20),
                                                fg_color='#1931df',
                                                command=lambda:self.button_event2("White"))
        self.button_white.grid(row=6, column=1, pady=0, padx=20)      

        #color button
        self.button_color = customtkinter.CTkButton(master=self.frame_right,
                                                text="Color",
                                                text_font=("Roboto Medium", -20),
                                                fg_color='#1931df',
                                                command=lambda:self.button_event2("Color"))
        self.button_color.grid(row=6, column=2, pady=0, padx=20)
        
        #softner switch
      
        self.switch_softner = customtkinter.CTkSwitch(master=self.frame_right,
                                                text="Softner",
                                                command=self.switch_event,
                                                onvalue="on",
                                                offvalue="off",
                                                text_font=("Roboto Medium", -17),)
        self.switch_softner.grid(row=8, column=0, columnspan=1, pady=10, padx=20, sticky="we")

        #start button
        self.button_start = customtkinter.CTkButton(master=self.frame_right,
                                                text="Start",
                                                width=200,
                                                height=70,
                                                text_font=("Roboto Medium", -25),
                                                fg_color='#1931df',
                                                state="disabled",
                                                command=self.button_start)
        self.button_start.grid(row=10, column=0,columnspan=3, pady=0, padx=0)
        
        # set default values

    

    def button_event(self):
      
        print("This is setting button")

 
    
    def button_event1(self,text):
        #clear button background
        self.button_samll.configure(fg_color='#1931df',text_color="white")
        self.button_medium.configure(fg_color='#1931df',text_color="white")
        self.button_heavy.configure(fg_color='#1931df',text_color="white")
        
        target=None
        
        if text=="Small":
            target=self.button_samll
        elif text=="Medium":
            target=self.button_medium
        elif text=="Heavy":
            target=self.button_heavy
            
        self.load=text
        if self.load!="" and self.detergent!="":
            self.button_start.configure(state="normal")
        target.configure(fg_color='white',text_color="#1931df")
    
        
    def button_event2(self,text):
        #clear button background
        self.button_black.configure(fg_color='#1931df',text_color="white")
        self.button_white.configure(fg_color='#1931df',text_color="white")
        self.button_color.configure(fg_color='#1931df',text_color="white")

        target=None
        
        if text=="White":
            target=self.button_white
        elif text=="Black":
            target=self.button_black
        elif text=="Color":
            target=self.button_color
            
        self.detergent=text
        if self.load!="" and self.detergent!="":
            self.button_start.configure(state="normal")
        target.configure(fg_color='white',text_color="#1931df")

    def switch_event(self):
        self.softner=self.switch_softner.get()

    def button_start(self):
        print("before:load:",self.load,"------ detergent:",self.detergent,"------ softner:",self.softner)
        #clear all button
        self.button_samll.configure(fg_color='#1931df',text_color="white")
        self.button_medium.configure(fg_color='#1931df',text_color="white")
        self.button_heavy.configure(fg_color='#1931df',text_color="white")
        self.button_black.configure(fg_color='#1931df',text_color="white")
        self.button_white.configure(fg_color='#1931df',text_color="white")
        self.button_color.configure(fg_color='#1931df',text_color="white")
        self.load=""
        self.detergent=""
        self.softner="off"
        print("After:load:",self.load,"------ detergent:",self.detergent,"------ softner:",self.softner)
        self.button_start.configure(state="disabled")
    def on_closing(self, event=0):
        self.destroy()    

if __name__ == "__main__":
    app = App()
    app.attributes('-fullscreen', True)
    app.mainloop()
