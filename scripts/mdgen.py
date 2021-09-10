"""This script will help convert documentation in csv format to md format."""

import csv


def gen():
    with open('function.csv') as function_csv, open('function.md', 'w+') as function_md:
        reader = csv.DictReader(function_csv)

        for row in reader:
            func_str = ''
            func_str += f'## {row["emql name"]}\n\n'
            func_str += f'{row["emql description"]}\n\n'
            func_str += (
                f'Link to MongoDB [{row["mongo name"]}]({row["mongo link"]}).\n\n'
            )
            func_str += f'### Syntax\n\n```EasyMQL\n{row["emql syntax"]}\n```\n\n'
            if row["example"] != '':
                func_str += f'### Example\n\n```EasyMQL\n{row["example"]}\n```\n\n'
            func_str += '----\n\n'

            function_md.write(func_str)


if __name__ == '__main__':
    gen()
