import os
from inflection import camelize


def _import_models():
    exports = []
    package_path = os.path.dirname(__file__)
    glob_vars, loc_vars = globals(), locals()

    for module_file in os.listdir(package_path):
        module_file_name = module_file.split('.')

        if module_file_name[0][0] != '_' and len(module_file_name) > 1 and module_file_name[1] == 'py':
            module_name = module_file_name[0]
            subpackage = 'apps.APPNAME.models'
            module = __import__(subpackage, glob_vars, loc_vars, [module_name])
            submodule = module.__dict__.get(module_name)
            model_name = camelize(module_name)
            model = submodule.__dict__.get(model_name)

            glob_vars.update({model_name: model})
            exports.append(model_name)

    return exports

if __name__ != '__main__':
    __all__ = _import_models()
