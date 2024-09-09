def add_attr(field: str, attr_name:str, attr_new_val:str, bootstrap_classes: bool = True) -> None:
    existing = field.widget.attrs.get(attr_name, '')
    if bootstrap_classes:
        field.widget.attrs['class'] = 'form-control'
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()

def add_many_attrs(field: str, attr: str, values: list) -> dict:
    for v in values:
        add_attr(field, attr, v)
    return field