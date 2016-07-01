import os


def get_template_path(path):
    file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), path)
    if not os.path.isfile(file_path):
        raise Exception("This is not a valid template path %s"%(file_path))
    return file_path


def get_template(path):
    file_path = get_template_path(path)
    return open(file_path).read()


def render_context(template_string, context):
    return template_string.format(**context)


