from os import path
resources_dir = path.join(path.dirname(__file__), 'data')
def define_units(filename):
    prefixes = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('#') or line.isspace() or line == '':
                continue
            elif line.startswith('@import'):
                filename = line.split()[1]
                # split into name and filetype
                name, filetype = filename.split('.')
                define_units(resources_dir + '/' + name+'_zero_overhead'+'.'+filetype)
            else:
                line = line.split('#')[0]
                equality_list = line.split('=')
                definition = equality_list[1]
                equality_list.remove(definition)
                definition = definition.strip()
                if definition.startswith('['):
                    value = 1
                else:
                    if 'offset' in definition:
                        definition = definition.split(';')[0]
                    value = eval(definition)

                if '-' in equality_list[0]:
                    for name in equality_list:
                        name = name.strip()
                        prefixes[name[:-1]] = value
                else:
                    for name in equality_list:
                        name = name.strip()
                        globals().update({name: value})
                        for prefix in prefixes:
                            if prefix+name not in globals():
                                globals().update({prefix + name: value * prefixes[prefix]})
