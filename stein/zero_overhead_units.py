from os import path
resources_dir = path.join(path.dirname(__file__), 'data')
def define_units(filename, ureg):
    prefixes = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('#') or line.isspace() or line == '':
                continue
            elif line.startswith('@import'):
                filename = line.split()[1]
                # split into name and filetype
                name, filetype = filename.split('.')
                define_units(resources_dir + '/' + name+'.'+filetype, ureg)
            else:
                line = line.split('#')[0]
                equality_list = line.split('=')
                definition = equality_list[1]
                equality_list.remove(definition)

                if '-' in equality_list[0]:
                    for name in equality_list:
                        name = name.strip()
                        name=name.split('-')[0]
                        value = ureg.Quantity(name+'meter').to_base_units().magnitude/ureg.Quantity('meter').to_base_units().magnitude
                        prefixes[name] = value
                else:
                    for name in equality_list:
                        name = name.strip()
                        value = ureg.Quantity(name).to_base_units().magnitude
                        globals().update({name: value})
                        for prefix in prefixes:
                            if prefix+name not in globals():
                                value = prefixes[prefix]*globals()[name]
                                globals().update({prefix + name: value})
