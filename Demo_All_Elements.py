#!/usr/bin/env python

import PySimpleGUI as sg

def make_window():
    # sg.theme()
    menu_def = [['&Application', ['E&xit']],
                ['&Help', ['&About']] ]
    right_click_menu_def = [[], ['Edit Me', 'Versions', 'Nothing','More Nothing','Exit']]
    graph_right_click_menu_def = [[], ['Erase','Draw Line', 'Draw',['Circle', 'Rectangle', 'Image'], 'Exit']]

    # Table Data
    data = [["John", 10], ["Jen", 5]]
    headings = ["Name", "Score"]


    

    global_layout =  [

                # [sg.Menu(menu_def, key='-MENU-')],
                [sg.Text('ViewMode'), sg.Combo(values=('FlyWithMe', 'SpringArmChase'), default_value='FlyWithMe', readonly=True, k='-COMBO-'), sg.Text('ClockType'), sg.Combo(values=('SteppableClock', 'ScalableClock'), default_value='SteppableClock', readonly=True, k='-COMBO-')], 

                [sg.Text('SimMode'), sg.Combo(values=('Multirotor', 'Car', 'ComputerVision'), default_value='Multirotor', readonly=True, k='-COMBO-')], 
                 
                [sg.Text('ClockSpeed'), sg.Slider(range=(0.1, 2), orientation='h', size=(10, 10), resolution=0.1, default_value=1, key='-SKIDER-'),], 
                # [sg.Image(data=sg.DEFAULT_BASE64_LOADING_GIF, enable_events=True, key='-GIF-IMAGE-'),],

                [sg.HorizontalSeparator(pad=(0, 20), color=sg.theme_background_color()), sg.Checkbox('OriginGeopoint', default=False, k='-CB-', enable_events=True), sg.HorizontalSeparator(pad=(0, 20), color=sg.theme_background_color())],

                [
                    sg.Text('N'), sg.Input(key='_INPUT_', size=(9, 1)), 
                    sg.Text('E'), sg.Input(key='_INPUT_', size=(9, 1)), 
                    sg.Text('D'), sg.Input(key='_INPUT_', size=(9, 1)), 
                ],

                [sg.HorizontalSeparator(pad=(0, 20), color=sg.theme_background_color()), sg.Checkbox('TimeOfDay', default=False, k='-CB-', enable_events=True), sg.HorizontalSeparator(pad=(0, 20), color=sg.theme_background_color())],
                [sg.Text('CelestialClockSpeed'), sg.Slider(range=(1, 500), orientation='h', size=(10, 10), resolution=1, default_value=60, key='-SKIDER-'), sg.Text('UpdateIntervalSecs'), sg.Slider(range=(1, 60), orientation='h', size=(10, 10), resolution=1, default_value=1, key='-SKIDER-'),],
                [sg.Checkbox('StartDateTimeDst', default=False, k='-CB-'),],
                [sg.HorizontalSeparator(pad=(0, 20), color=sg.theme_background_color()), sg.Checkbox('Wind', default=False, k='-CB-', enable_events=True), sg.HorizontalSeparator(pad=(0, 20), color=sg.theme_background_color())],
                [
                    sg.Text('N'), sg.Input(key='_INPUT_', size=(9, 1)), 
                    sg.Text('E'), sg.Input(key='_INPUT_', size=(9, 1)), 
                    sg.Text('D'), sg.Input(key='_INPUT_', size=(9, 1)), 
                ],

                [sg.HorizontalSeparator(pad=(0, 20), color=sg.theme_background_color()), sg.Checkbox('Recording', default=False, k='-CB-', enable_events=True), sg.HorizontalSeparator(pad=(0, 20), color=sg.theme_background_color())],
                [sg.Checkbox('RecordUIVisible', default=False, k='-CB-')], 
                [sg.Checkbox('RecordOnMove', default=False, k='-CB-')],

                [sg.Text('RecordInterval'), sg.Slider(range=(0.01, 2), orientation='h', size=(10, 10), resolution=0.01, default_value=1, key='-SKIDER-'),], 

                [sg.HorizontalSeparator(pad=(0, 20), color=sg.theme_background_color()), sg.Checkbox('CameraDefaults', default=False, k='-CB-', enable_events=True), sg.HorizontalSeparator(pad=(0, 20), color=sg.theme_background_color())],
                    ]

    recording_layout = [
                        [sg.Checkbox('Enabled', default=False, k='-CB-')], 

                        
                        [sg.Image(data=sg.DEFAULT_BASE64_ICON,  k='-IMAGE-')],
                        [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS BAR-'), sg.Button('Test Progress bar')]
                        ]

    vehicles_layout = [
        [sg.Text("Anything printed will display here!")],
        [sg.Multiline(size=(60,15), font='Courier 8', expand_x=True, expand_y=True, write_only=True,
                                    reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)]
                      # [sg.Output(size=(60,15), font='Courier 8', expand_x=True, expand_y=True)]
                      ]
    
    # camera_layout = [[sg.Text("Anything you would use to graph will display here!")],
    #                   [sg.Graph((200,200), (0,0),(200,200),background_color="black", key='-GRAPH-', enable_events=True,
    #                             right_click_menu=graph_right_click_menu_def)],
    #                   [sg.T('Click anywhere on graph to draw a circle')],
    #                   [sg.Table(values=data, headings=headings, max_col_width=25,
    #                             background_color='black',
    #                             auto_size_columns=True,
    #                             display_row_numbers=True,
    #                             justification='right',
    #                             num_rows=2,
    #                             alternating_row_color='black',
    #                             key='-TABLE-',
    #                             row_height=25)]]



    cameras_layout = [
        [sg.Text("Popup Testing")],
        [sg.Button("Open Folder")],
        [sg.Button("Open File")]
                    ]
    
    load_layout = [[sg.Text("Load and analyze settings file here. ")],
                    [sg.Listbox(values = sg.theme_list(), 
                      size =(20, 12), 
                      key ='-THEME LISTBOX-',
                      enable_events = True)],
                      [sg.Button("Set Theme")]]
    
    layout = [ [sg.MenubarCustom(menu_def, key='-MENU-', font='Courier 15', tearoff=True)],
                [sg.Text('Demo Of (Almost) All Elements', size=(38, 1), justification='center', font=("Helvetica", 16), relief=sg.RELIEF_RIDGE, k='-TEXT HEADING-', enable_events=True)]]
    layout +=[[sg.TabGroup([[  sg.Tab('Global Settings', global_layout),
                               sg.Tab('Recording', recording_layout),
                               sg.Tab('Camera Settings', cameras_layout),
                               sg.Tab('Load From..', load_layout),
                               sg.Tab('Vehicles', vehicles_layout)]], key='-TAB GROUP-', expand_x=True, expand_y=True),

               ]]
    layout[-1].append(sg.Sizegrip())
    window = sg.Window('All Elements Demo', layout, right_click_menu=right_click_menu_def, right_click_menu_tearoff=True, grab_anywhere=True, resizable=True, margins=(0,0), use_custom_titlebar=True, finalize=True, keep_on_top=True)
    window.set_min_size(window.size)
    return window

def main():
    window = make_window()

    # This is an Event Loop 
    while True:
        event, values = window.read(timeout=100)
        # keep an animation running so show things are happening
        if event not in (sg.TIMEOUT_EVENT, sg.WIN_CLOSED):
            print('============ Event = ', event, ' ==============')
            print('-------- Values Dictionary (key=value) --------')
            for key in values:
                print(key, ' = ',values[key])
        if event in (None, 'Exit'):
            print("[LOG] Clicked Exit!")
            break

        # window['-GIF-IMAGE-'].update_animation(sg.DEFAULT_BASE64_LOADING_GIF, time_between_frames=100)
        if event == 'About':
            print("[LOG] Clicked About!")
            sg.popup('PySimpleGUI Demo All Elements',
                     'Right click anywhere to see right click menu',
                     'Visit each of the tabs to see available elements',
                     'Output of event and values can be see in Output tab',
                     'The event and values dictionary is printed after every event', keep_on_top=True)
        elif event == 'Popup':
            print("[LOG] Clicked Popup Button!")
            sg.popup("You pressed a button!", keep_on_top=True)
            print("[LOG] Dismissing Popup!")
        elif event == 'Test Progress bar':
            print("[LOG] Clicked Test Progress Bar!")
            progress_bar = window['-PROGRESS BAR-']
            for i in range(100):
                print("[LOG] Updating progress bar by 1 step ("+str(i)+")")
                progress_bar.update(current_count=i + 1)
            print("[LOG] Progress bar complete!")
        elif event == "-GRAPH-":
            graph = window['-GRAPH-']       # type: sg.Graph
            graph.draw_circle(values['-GRAPH-'], fill_color='yellow', radius=20)
            print("[LOG] Circle drawn at: " + str(values['-GRAPH-']))
        elif event == "Open Folder":
            print("[LOG] Clicked Open Folder!")
            folder_or_file = sg.popup_get_folder('Choose your folder', keep_on_top=True)
            sg.popup("You chose: " + str(folder_or_file), keep_on_top=True)
            print("[LOG] User chose folder: " + str(folder_or_file))
        elif event == "Open File":
            print("[LOG] Clicked Open File!")
            folder_or_file = sg.popup_get_file('Choose your file', keep_on_top=True)
            sg.popup("You chose: " + str(folder_or_file), keep_on_top=True)
            print("[LOG] User chose file: " + str(folder_or_file))
        elif event == "Set Theme":
            print("[LOG] Clicked Set Theme!")
            theme_chosen = values['-THEME LISTBOX-'][0]
            print("[LOG] User Chose Theme: " + str(theme_chosen))
            window.close()
            window = make_window(theme_chosen)
        elif event == 'Edit Me':
            sg.execute_editor(__file__)
        elif event == 'Versions':
            sg.popup_scrolled(__file__, sg.get_versions(), keep_on_top=True, non_blocking=True)

    window.close()
    exit(0)

if __name__ == '__main__':
    sg.theme('black')
    sg.theme('dark red')
    sg.theme('dark green 7')
    # sg.theme('DefaultNoMoreNagging')
    main()