import ipywidgets as widgets
from IPython.display import display
from pathlib import Path
import logging

LOGPATH = None
ANALYSISPATH = None
TEMPLATEPATH = None

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers = [logging.StreamHandler()])

log_path_widget = widgets.Text(
    value='',
    placeholder='C:/Evidence/var/log',
    description='Path to Citrix Logs:', 
    style={'description_width': 'initial'},
    disabled=False,
    display='flex',
    flex_flow='column',
    align_items='stretch',
    layout = widgets.Layout(width='auto')
)

analysis_path_widget = widgets.Text(
    value='',
    placeholder='C:/Analysis',
    description='Path logs are extracted to and results are exported to:', 
    style={'description_width': 'initial'},
    disabled=False,
    display='flex',
    flex_flow='column',
    align_items='stretch',
    layout = widgets.Layout(width='auto')
)

template_path_checkbox = widgets.Checkbox(
    value=False,
    description='XML Templates present (/netscaler/portal/templates or /var/vpn/bookmark)',
    disabled=False,
    style={'description_width': 'initial'},
    display='flex',
    flex_flow='column',
    align_items='stretch',
    layout = widgets.Layout(width='auto')
)

template_path_widget = widgets.Text(
    value='',
    placeholder='C:/Evidence/netscaler/portal/templates',
    description='Path to Citrix templates:', 
    style={'description_width': 'initial'},
    disabled=True,
    display='flex',
    flex_flow='column',
    align_items='stretch',
    layout = widgets.Layout(width='auto'),
)

submit_widget = widgets.Button(
    description='Submit',
    disable=False,
    button_style='success',
    tooltip='Submit Config',
    icon='check'
)

def template_checkbox_eventhandler(obj):
    if obj['new']:
        template_path_widget.disabled = False
    else:
        template_path_widget.disabled = True

def submit_button_eventhandler(obj):
    LOGPATH = Path(log_path_widget.value)
    logging.info(f'LOGPATH set to {LOGPATH}')
    ANALYSISPATH = Path(analysis_path_widget.value)
    logging.info(f'ANALYSISPATH set to {ANALYSISPATH}')

    if template_path_widget.disabled == False:
        TEMPLATEPATH = template_path_widget.value
        logging.info(f'TEMPLATEPATH set to {TEMPLATEPATH}')
    else:
        logging.info('XML Templates not present, skipping TEMPLATEPATH')
    obj.disabled = True

template_path_checkbox.observe(template_checkbox_eventhandler, names='value')
submit_widget.on_click(submit_button_eventhandler)

display(log_path_widget)
display(analysis_path_widget)
display(template_path_checkbox)
display(template_path_widget)
display(submit_widget)