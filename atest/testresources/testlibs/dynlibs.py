class _BaseDynamicLibrary:

    def get_keyword_names(self):
        return []

    def run_keyword(self, name, *args):
        return None

class StaticDocsLib(_BaseDynamicLibrary):
    """This is lib intro."""
    def __init__(self, some=None, args=[]):
        """Init doc."""

class DynamicDocsLib(_BaseDynamicLibrary):
    def __init__(self, *args): pass

    def get_keyword_documentation(self, name):
        if name == '__intro__':
            return 'Dynamic intro doc.'
        return 'Dynamic init doc.' if name == '__init__' else ''

class StaticAndDynamicDocsLib(_BaseDynamicLibrary):
    """This is static doc."""
    def __init__(self, an_arg=None):
        """This is static doc."""
    def get_keyword_documentation(self, name):
        if name == '__intro__':
            return 'dynamic override'
        return 'dynamic override' if name == '__init__' else ''

class FailingDynamicDocLib(_BaseDynamicLibrary):
    """intro-o-o"""
    def __init__(self):
        """initoo-o-o"""
    def get_keyword_documentation(self, name):
        raise RuntimeError('Failing in get_keyword_documentation')

