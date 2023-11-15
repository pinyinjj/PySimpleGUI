import PySimpleGUI as sg


layout = [ 
    [sg.Text('复选框示例')],      
    [sg.Checkbox('显示窗口', key='checkbox')], 
    [sg.Text('', key='_OUTPUT_')],      
]   

window = sg.Window('示例', layout)    

while True:     

    event, values = window.read() 
    print(f"is {values}")
    if event in (None, '退出'):      
        break      
    if event == 'checkbox':
        popup_layout = [
            [sg.Text('输入值1'), sg.InputText(key='_input1_')],
            [sg.Text('输入值2'), sg.InputText(key='_input2_')],
            [sg.Text('输入值3'), sg.InputText(key='_input3_')], 
            [sg.Button('设置'), sg.Button('取消')]
        ]

        popup_window = sg.Window('弹出窗口', popup_layout)

        while True:
            event_popup, values_popup = popup_window.read()

            if event_popup in (None, '取消'):
                break
            if event_popup == '设置':
                window['_OUTPUT_'].update(f"输入值1: {values_popup['_input1_']}, 输入值2: {values_popup['_input2_']}, 输入值3: {values_popup['_input3_']}")
                popup_window.close()                

window.close()
