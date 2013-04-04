# coding: utf-8
from templated_email import send_templated_mail as original_send


def get_message_template_kwargs(path):
    ext = path.split('.')[-1]
    parts = path.split('/')
    template_prefix = path.replace(parts[-1], '')
    template_name = parts[-1].replace(ext, '')[:-1]
    return {
        'template_prefix': template_prefix,
        'template_suffix': ext,
        'template_name': template_name,
    }


def send_templated_mail(**kwargs):
    email_template = kwargs.pop('email_template', None)
    if email_template:
        kwargs.update(get_message_template_kwargs(email_template))
    return original_send(**kwargs)
