import os
from os.path import join, dirname

from mako.template import Template
from mako.lookup import TemplateLookup

import click

def render_html(fig_id, dataset):
    here = dirname(os.path.abspath(__file__))
    template_path = join(here, "templates/template.mako")
    template_dir = dirname(template_path)
    lookup = TemplateLookup(directories=[template_dir],
                            input_encoding='utf-8',
                            output_encoding='utf-8',
                            encoding_errors='replace')
    template = Template(filename=template_path, lookup=lookup)

    def to_js_obj(dataset):
        return str(dataset)

    content = template.render(fig_id=fig_id, dataset=to_js_obj(dataset))
    return content

def parse_line(line):
    items = line.strip().split('\t')
    obj = {
        'term': items[0],
        'log2Pvalue': float(items[1]),
        'GOType': items[2],
        'count': int(items[3]),
        'ratio': float(items[4]),
        'log2fc': float(items[5]),
    }
    return obj

def load_dataset(tsv_path):
    dataset = []
    with open(tsv_path) as f:
        for line in f:
            obj = parse_line(line)
            dataset.append(obj)
    return dataset

@click.command("render_bubble")
@click.argument("input_tsv")
@click.argument("output")
@click.option("--fig-id",
    default="",
    type=str)
def main(input_tsv, output, fig_id):
    dataset = load_dataset(input_tsv)
    content = render_html(fig_id, dataset)
    with open(output, 'w') as f:
        f.write(content)


if __name__ == "__main__":
    main()