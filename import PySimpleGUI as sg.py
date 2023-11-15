import PySimpleGUI as sg

# 创建两个元素，一个靠左一个靠右
left_element = sg.Text('靠左', justification='left')
right_element = sg.Text('靠右', justification='right')

# 创建Column内的布局，将左右两个元素放入一行
column_layout = [
    [left_element, right_element]
]

# 创建Column
column = sg.Column(column_layout, element_justification='left')  # 设置Column的element_justification为'left'

# 创建窗口并将Column放入其中
window = sg.Window('Column示例', [[column]])

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
