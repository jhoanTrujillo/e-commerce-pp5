from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('remove')
    initial_text = _('Current Image')
    input_text = _('No image selected')
    template_name = (
        'products/custom_widgets_template/custom_clearable_file_input.html'
    )
