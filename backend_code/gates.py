import ipywidgets as widgets
from IPython import display


def create_expanded_button(description, button_style):
    return widgets.ToggleButton(description=description, icon='close',
                                button_style=button_style,
                                layout=widgets.Layout(height='auto', width='auto'))


def gate(op, name):
    top_left_button = create_expanded_button("Input One", 'info')
    bottom_left_button = create_expanded_button("Input Two", 'danger')
    right_button = create_expanded_button("Output", 'warning')
    right_button.disabled = True

    def gate_op(x, y):
        if x:
            top_left_button.icon = 'bolt'
        else:
            top_left_button.icon = 'close'
        if y:
            bottom_left_button.icon = 'bolt'
        else:
            bottom_left_button.icon = 'close'
        out = op(x, y)
        right_button.value = out
        if out:
            right_button.icon = 'bolt' 
        else:
            right_button.icon = 'close'

    output = widgets.GridspecLayout(2,5, display='flex', align_items='stretch')
    output[0, 0] = top_left_button
    output[1, 0] = bottom_left_button
    output[0, 1] = widgets.Label('\u27A1\uFE0F', layout=widgets.Layout(display="flex",
                                                                   justify_content="center",
                                                                   align_items="center", width='auto'))
    output[1, 1] = widgets.Label('\u27A1\uFE0F', layout=widgets.Layout(display="flex",
                                                                   justify_content="center",
                                                                   align_items="center", width='auto'))
    output[:, 2] = widgets.Label(f'{name} gate ', layout=widgets.Layout(display="flex", justify_content="center", align_items="center", border="solid"))
    output[:, 3] = widgets.Label('\u27A1\uFE0F', layout=widgets.Layout(display="flex",
                                                                   justify_content="center",
                                                                   align_items="center", width='auto'))
    output[:, 4] = right_button
    widgets.interactive(gate_op, x=top_left_button, y=bottom_left_button)

    display.display(output)
