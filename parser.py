import pathlib
from psd_tools import PSDImage

def parse_layer(layer):

    if layer.kind == 'group':
        return [parse_layer(sub_layer) for sub_layer in layer]
    else:
        layer.composite().save(f'data/{layer.kind}_{layer.name}.png')

psd = PSDImage.open('input.psd')

res = [parse_layer(layer) for layer in psd]
# print(res)