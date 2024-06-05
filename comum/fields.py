from django import forms
from unfold.widgets import SELECT_CLASSES, INPUT_CLASSES, BASE_CLASSES, TEXTAREA_CLASSES


class CustomModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.ModelChoiceField):
                field.widget.attrs.update({"class": " ".join([*SELECT_CLASSES, "w-72"])})
            if isinstance(field, forms.CharField):
                field.widget.attrs.update({"class": " ".join(INPUT_CLASSES)})
            if isinstance(field, forms.ModelMultipleChoiceField):
                field.widget.attrs.update({"class": " ".join([*SELECT_CLASSES, "w-72"])})

            if isinstance(field, forms.ChoiceField):
                field.widget.attrs.update({"class": " ".join([*SELECT_CLASSES, "w-72"])})
            if isinstance(field, forms.Textarea):
                field.widget.attrs.update({"class": " ".join([TEXTAREA_CLASSES])})

    def add_classes_to_widget(self, field_name, classes_to_add):
        field = self.fields.get(field_name)
        if field:
            widget = field.widget
            existing_classes = widget.attrs.get('class', '').split()
            new_classes = existing_classes + classes_to_add
            widget.attrs['class'] = ' '.join(new_classes)


class CustomForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.ChoiceField):
                field.widget.attrs.update({"class": " ".join([*SELECT_CLASSES, "w-72"])})
            if isinstance(field, forms.CharField):
                field.widget.attrs.update({"class": " ".join(INPUT_CLASSES)})
            if isinstance(field, forms.MultipleChoiceField):
                field.widget.attrs.update({"class": " ".join([*SELECT_CLASSES, "w-72"])})
            if isinstance(field, forms.Textarea):
                field.widget.attrs.update({"class": " ".join(TEXTAREA_CLASSES)})
