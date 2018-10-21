#!/usr/bin/python

import collections
import io
import sys
import yaml

filename = str(sys.argv[1])
snippet = yaml.load(sys.argv[2])

with io.open(filename, 'r', encoding='utf8') as f:
   yaml_dict = yaml.load(f) or {}

def deep_update(source, overrides):
    for key, value in overrides.iteritems():
        if isinstance(value, collections.Mapping) and value:
            returned = deep_update(source.get(key, {}), value)
            source[key] = returned
        else:
            source[key] = overrides[key]
    return source   

deep_update(yaml_dict, snippet)

with io.open(filename, 'w', encoding='utf8') as f:
   yaml.dump(yaml_dict, f, default_flow_style=False, allow_unicode=True)    
