from flexx import flx


class NN_Calc(flx.Widget):
    
    counter = flx.IntProp(27, settable=True)
    
    def init(self):
        super().init()
        with flx.VSplit():
            self.label = flx.Label(text='')
            with flx.HSplit():
                self.line_edit = flx.LineEdit(flex=1)
            with flx.HSplit():
                self.but_sum = flx.Button(text='+', flex=1)
                self.but_sub = flx.Button(text='–', flex=1)                
            with flx.HSplit():
                flx.Button(text='×', flex=1)
                flx.Button(text='÷', flex=1)   
    
    @flx.reaction('line_edit.text')
    def enter_text(self, *events):
        self.label.set_text('DON\'T TOUCH THIS FIELD!')
    
    @flx.action
    def plus_one(self):
        self._mutate_counter(self.counter + 1)
        
    @flx.action
    def minus_one(self):
        self._mutate_counter(self.counter - 1)
        
    @flx.reaction('but_sum.pointer_click')
    def but_sum_clicked(self, *events):
        self.plus_one()        
        
    @flx.reaction('but_sub.pointer_click')
    def nut_sud_clicked(self, *events):
        self.minus_one()
        
    @flx.reaction
    def update(self, *events):
        self.label.set_text('count is {}'.format(self.counter))
        


app = flx.App(NN_Calc)
app.launch('app')
flx.run()