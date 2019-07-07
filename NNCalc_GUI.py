# =============================================================================
# IMPORT MODULES
# =============================================================================

# GUI KIVY
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# WINDOW SIZING
from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '550')

# MY FUNCTIONS
from func import functions as fcs

# =============================================================================
# MAIN SCREEN CLASS
# =============================================================================

class MainScreen(GridLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        # ==========
        # PREPEARING
        # ==========
        
        # Get models
        self.models = fcs.pickled(filename='pickle/models.pickle', 
                             mode='load')
        # Cols of app interface
        self.cols = 2
        
        # ======================
        # MAIN INTERFACE OBJECTS
        # ======================
        
        # ANS Labels
        self.lbl_left = Label(text='Input\ntwo\nnumbers'.upper(), 
                              font_size=20)
        
        self.lbl_right = Label(text='And\npress\nbutton\nyou\nwant'.upper(), 
                               font_size=20)
        
        # TextInputs
        self.inp1 = TextInput(text='2', 
                              font_size=99)

        self.inp2 = TextInput(text='2', 
                              font_size=99)        
        
        # Buttons
        self.btn_sum = Button(text='+', 
                              font_size=99, 
                              background_color=[155.,1.,1.,1.], 
                              on_press=self.get_sum)
        
        self.btn_sub = Button(text='-', 
                              font_size=99, 
                              background_color=[1.,155.,1.,1.], 
                              on_press=self.get_sub)
        
        self.btn_mul = Button(text='×', 
                              font_size=99, 
                              background_color=[1.,1.,155.,1.], 
                              on_press=self.get_mul)
        
        self.btn_div = Button(text='÷', 
                              font_size=99, 
                              background_color=[155.,1.,155.,1.], 
                              on_press=self.get_div)
        
        # ==============
        # ADDING WIDGETS
        # ==============
        
        # Labels
        self.add_widget(self.lbl_left)
        self.add_widget(self.lbl_right)
        
        #Inputs
        self.add_widget(self.inp1)
        self.add_widget(self.inp2)
        
        # Buttons
        self.add_widget(self.btn_sum)
        self.add_widget(self.btn_sub)
        self.add_widget(self.btn_mul)
        self.add_widget(self.btn_div) 
    
    # =========    
    # FUNCTIONS
    # =========
    
    # +
    def get_sum(self, event):
        try:
            self.var1 = int(self.inp1.text)
            self.var2 = int(self.inp2.text)

            self.ans_hash = fcs.get_answer(self.models, 
                                      values=[self.var1, 
                                              self.var2], 
                                      operation=0)  
    
            self.lbl_left.text = '\
            BASH says: {}\n\
            IVAN says: {}\n\
            ALBA says: {}\n\n\
            Winner: {}'.format( self.ans_hash['bans'], 
                                    self.ans_hash['ians'], 
                                    self.ans_hash['aans'], 
                                    self.ans_hash['nwin'])
            
            self.lbl_right.text = '\
            Action: +\n\n\
            Summary: {}\n\n\
            True Answer: {}'.format( self.ans_hash['ans'], 
                        self.ans_hash['tans'])
            
        except ValueError:
            self.lbl_left.text = 'Only INT number!'
            self.lbl_right.text = 'Only INT number!'
    
    # –
    def get_sub(self, event):
        try:
            self.var1 = int(self.inp1.text)
            self.var2 = int(self.inp2.text)

            self.ans_hash = fcs.get_answer(self.models, 
                                      values=[self.var1, 
                                              self.var2], 
                                      operation=1)  
    
            self.lbl_left.text = '\
            BASH says: {}\n\
            IVAN says: {}\n\
            ALBA says: {}\n\n\
            Winner: {}'.format( self.ans_hash['bans'], 
                                    self.ans_hash['ians'], 
                                    self.ans_hash['aans'], 
                                    self.ans_hash['nwin'])
            
            self.lbl_right.text = '\
            Action: –\n\n\
            Summary: {}\n\n\
            True Answer: {}'.format( self.ans_hash['ans'], 
                        self.ans_hash['tans'])
            
        except ValueError:
            self.lbl_left.text = 'Only INT number!'
            self.lbl_right.text = 'Only INT number!'
    
    # ×        
    def get_mul(self, event):
        try:
            self.var1 = int(self.inp1.text)
            self.var2 = int(self.inp2.text)

            self.ans_hash = fcs.get_answer(self.models, 
                                      values=[self.var1, 
                                              self.var2], 
                                      operation=2)  
    
            self.lbl_left.text = '\
            BASH says: {}\n\
            IVAN says: {}\n\
            ALBA says: {}\n\n\
            Winner: {}'.format( self.ans_hash['bans'], 
                                    self.ans_hash['ians'], 
                                    self.ans_hash['aans'], 
                                    self.ans_hash['nwin'])
            
            self.lbl_right.text = '\
            Action: ×\n\n\
            Summary: {}\n\n\
            True Answer: {}'.format( self.ans_hash['ans'], 
                        self.ans_hash['tans'])
            
        except ValueError:
            self.lbl_left.text = 'Only INT number!'
            self.lbl_right.text = 'Only INT number!'
    
    # ÷        
    def get_div(self, event):
        try:
            self.var1 = int(self.inp1.text)
            self.var2 = int(self.inp2.text)

            self.ans_hash = fcs.get_answer(self.models, 
                                      values=[self.var1, 
                                              self.var2], 
                                      operation=3)  
    
            self.lbl_left.text = '\
            BASH says: {}\n\
            IVAN says: {}\n\
            ALBA says: {}\n\n\
            Winner: {}'.format( self.ans_hash['bans'], 
                                    self.ans_hash['ians'], 
                                    self.ans_hash['aans'], 
                                    self.ans_hash['nwin'])
            
            self.lbl_right.text = '\
            Action: ÷\n\n\
            Summary: {}\n\n\
            True Answer: {}'.format( self.ans_hash['ans'], 
                        self.ans_hash['tans'])
            
        except ValueError:
            self.lbl_left.text = 'Only INT number!'
            self.lbl_right.text = 'Only INT number!'

# =============================================================================
# BUILDING APP
# =============================================================================
        
class NNCalculatorApp(App):
    def build(self):
        return MainScreen()

# =============================================================================
# RUNNING
# =============================================================================

NNCalculatorApp().run()