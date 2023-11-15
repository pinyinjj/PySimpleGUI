import PySimpleGUI as sg

normal_globals = [
    [sg.Frame('Choose your Sauces', [[sg.Text('ViewMode'), sg.Combo(values=('FlyWithMe', 'SpringArmChase'), default_value='FlyWithMe', readonly=True, k='-COMBO-'), sg.Text('ClockType'), sg.Combo(values=('SteppableClock', 'ScalableClock'), default_value='SteppableClock', readonly=True, k='-COMBO-')], 
    [sg.Text('SimMode'), sg.Combo(values=('Multirotor', 'Car', 'ComputerVision'), default_value='Multirotor', readonly=True, k='-COMBO-')], 
    [sg.Text('ClockSpeed'), sg.Slider(range=(0.1, 2), orientation='h', size=(10, 10), resolution=0.1, default_value=1, key='-SKIDER-'),], ],title_color='yellow', border_width=3)],
    
]

cols = [[sg.Column(choices, element_justification='l'), 
         sg.Column(items_chosen, element_justification='l'),
         sg.Column(items_chosen, element_justification='l'),
         sg.Column(items_chosen, element_justification='l'),
         sg.Column(items_chosen, element_justification='l')]]