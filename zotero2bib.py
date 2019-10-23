#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser as ap
import re, codecs


def convert_date_year(line):
  try:
    regex = re.search(r'^\s*date = {(....)', line)
    year = regex.groups()[0]
    line = '        year = {{{}}},\n{}'.format(year, line)
    return line
  except:
    return line

def wrap_name_with_brace(line):
  if line.find('author = {') == -1:
    return line
  else:
    regex = re.search(r'(.*author = {)(.*)(},?\s*)$', line)
    pre,authors,post = regex.groups()
    names = re.split(r'\s+and\s+', authors)
    newnames = []
    for name in names:
      if name.find(',') > 0:
        newnames.append(name)
      else:
        newnames.append('{' + name + '}')
    return pre+' and '.join(newnames)+post

def convert_signs(line):
  line = line.replace(r'¡', '''{!`}''')
  line = line.replace(r'¿', '''{?`}''')
  line = line.replace(r'ø', '''{\\o}''')
  line = line.replace(r'Ø', '''{\\O}''')
  line = line.replace(r'ñ', '''{\\~n}''')
  line = line.replace(r'Ñ', '''{\\~N}''')
  line = line.replace(r'č', '''{\\v{c}}''')
  line = line.replace(r'Č', '''{\\v{C}}''')
  line = line.replace(r'š', '''{\\v{s}}''')
  line = line.replace(r'Š', '''{\\v{S}}''')
  line = line.replace(r'ž', '''{\\v{z}}''')
  line = line.replace(r'Ž', '''{\\v{Z}}''')
  line = line.replace(r'¢', '''{}''')
  line = line.replace(r'\$', '''{\\$}''')
  line = line.replace(r'€', '''{}''')
  line = line.replace(r'ł', '''{\\l}''')
  line = line.replace(r'Ł', '''{\\L}''')
  # line = line.replace(r'%', '''{\\%}''')
  line = line.replace(r'ß', '''{\\ss}''')
  line = line.replace(r'⊙', '''${_\\odot}$''')
  line = line.replace(r'≥', '''${\\ge}$''')
  line = line.replace(r'≤', '''${\\le}$''')
  line = line.replace(r'∼', '''{\\textasciitilde}''')
  line = line.replace(r'Ø,', '''{\O}''')
  line = line.replace(r'ø', '''{\o}''')
  return line

def convert_bar(line):
  line = line.replace(r'ā', '''{\\=a}''')
  line = line.replace(r'ē', '''{\\=e}''')
  line = line.replace(r'ū', '''{\\=u}''')
  line = line.replace(r'ī', '''{\\=i}''')
  line = line.replace(r'ō', '''{\\=o}''')
  line = line.replace(r'Ā', '''{\\=A}''')
  line = line.replace(r'Ē', '''{\\=E}''')
  line = line.replace(r'Ū', '''{\\=U}''')
  line = line.replace(r'Ī', '''{\\=I}''')
  line = line.replace(r'Ō', '''{\\=O}''')
  return line

def convert_acute(line):
  line = line.replace(r'á', '''{\\'a}''')
  line = line.replace(r'é', '''{\\'e}''')
  line = line.replace(r'ú', '''{\\'u}''')
  line = line.replace(r'í', '''{\\'i}''')
  line = line.replace(r'ó', '''{\\'o}''')
  line = line.replace(r'Á', '''{\\'A}''')
  line = line.replace(r'É', '''{\\'E}''')
  line = line.replace(r'Ú', '''{\\'U}''')
  line = line.replace(r'Í', '''{\\'I}''')
  line = line.replace(r'Ó', '''{\\'O}''')
  line = line.replace(r'ć', '''{\\'c}''')
  line = line.replace(r'Ć', '''{\\'C}''')
  line = line.replace(r'ĺ', '''{\\'l}''')
  line = line.replace(r'Ĺ', '''{\\'L}''')
  line = line.replace(r'ń', '''{\\'n}''')
  line = line.replace(r'Ń', '''{\\'N}''')
  line = line.replace(r'ŕ', '''{\\'r}''')
  line = line.replace(r'Ŕ', '''{\\'R}''')
  line = line.replace(r'ś', '''{\\'s}''')
  line = line.replace(r'Ś', '''{\\'S}''')
  line = line.replace(r'ú', '''{\\'u}''')
  line = line.replace(r'Ú', '''{\\'U}''')
  line = line.replace(r'ý', '''{\\'y}''')
  line = line.replace(r'Ý', '''{\\'Y}''')
  line = line.replace(r'ź', '''{\\'z}''')
  line = line.replace(r'Ź', '''{\\'Z}''')
  return line

def convert_uml(line):
  line = line.replace(r'ä', '''{\\"a}''')
  line = line.replace(r'ë', '''{\\"e}''')
  line = line.replace(r'ü', '''{\\"u}''')
  line = line.replace(r'ï', '''{\\"i}''')
  line = line.replace(r'ö', '''{\\"o}''')
  line = line.replace(r'Ä', '''{\\"A}''')
  line = line.replace(r'Ë', '''{\\"E}''')
  line = line.replace(r'Ü', '''{\\"U}''')
  line = line.replace(r'Ï', '''{\\"I}''')
  line = line.replace(r'Ö', '''{\\"O}''')
  return line

def convert_cedil(line):
  line = line.replace(r'ą', '''{\\c{a}}''')
  line = line.replace(r'Ą', '''{\\c{A}}''')
  line = line.replace(r'ç', '''{\\c{c}}''')
  line = line.replace(r'Ç', '''{\\c{C}}''')
  line = line.replace(r'ę', '''{\\c{e}}''')
  line = line.replace(r'Ę', '''{\\c{E}}''')
  line = line.replace(r'ģ', '''{\\c{g}}''')
  line = line.replace(r'Ģ', '''{\\c{G}}''')
  line = line.replace(r'į', '''{\\c{i}}''')
  line = line.replace(r'Į', '''{\\c{I}}''')
  line = line.replace(r'ķ', '''{\\c{k}}''')
  line = line.replace(r'Ķ', '''{\\c{K}}''')
  line = line.replace(r'ļ', '''{\\c{l}}''')
  line = line.replace(r'Ļ', '''{\\c{C}}''')
  line = line.replace(r'ņ', '''{\\c{n}}''')
  line = line.replace(r'Ņ', '''{\\c{C}}''')
  line = line.replace(r'ŗ', '''{\\c{r}}''')
  line = line.replace(r'Ŗ', '''{\\c{C}}''')
  line = line.replace(r'ş', '''{\\c{s}}''')
  line = line.replace(r'Ş', '''{\\c{C}}''')
  line = line.replace(r'ţ', '''{\\c{t}}''')
  line = line.replace(r'Ţ', '''{\\c{C}}''')
  line = line.replace(r'ų', '''{\\c{u}}''')
  line = line.replace(r'Ų', '''{\\c{C}}''')
  return line

def convert_grave(line):
  line = line.replace(r'à', '''{\\`a}''')
  line = line.replace(r'è', '''{\\`e}''')
  line = line.replace(r'ù', '''{\\`u}''')
  line = line.replace(r'Ì', '''{\\`i}''')
  line = line.replace(r'ò', '''{\\`o}''')
  line = line.replace(r'À', '''{\\`A}''')
  line = line.replace(r'È', '''{\\`E}''')
  line = line.replace(r'Ū', '''{\\`U}''')
  line = line.replace(r'Ì', '''{\\`I}''')
  line = line.replace(r'Ù', '''{\\`O}''')
  return line

def convert_greece(line):
  line = line.replace(r'Α', '''${A}$''')
  line = line.replace(r'Β', '''${B}$''')
  line = line.replace(r'Γ', '''${\\Gamma}$''')
  line = line.replace(r'Δ', '''${\\Delta}$''')
  line = line.replace(r'Ε', '''${E}$''')
  line = line.replace(r'Ζ', '''${Z}$''')
  line = line.replace(r'Η', '''${H}$''')
  line = line.replace(r'Θ', '''${\\Theta}$''')
  line = line.replace(r'Ι', '''${I}$''')
  line = line.replace(r'Κ', '''${K}$''')
  line = line.replace(r'Λ', '''${\\Lambda}$''')
  line = line.replace(r'Μ', '''${M}$''')
  line = line.replace(r'Ν', '''${N}$''')
  line = line.replace(r'Ξ', '''${\\Xi}$''')
  line = line.replace(r'Ο', '''${O}$''')
  line = line.replace(r'Π', '''${\\Pi}$''')
  line = line.replace(r'Ρ', '''${P}$''')
  line = line.replace(r'Σ', '''${\\Sigma}$''')
  line = line.replace(r'Τ', '''${T}$''')
  line = line.replace(r'Υ', '''${\\Upsilon}$''')
  line = line.replace(r'Φ', '''${\\Phi}$''')
  line = line.replace(r'Χ', '''${\\Chi}$''')
  line = line.replace(r'Ψ', '''${\\Psi}$''')
  line = line.replace(r'Ω', '''${\\Omega}$''')
  line = line.replace(r'α', '''${\\alpha}$''')
  line = line.replace(r'β', '''${\\beta}$''')
  line = line.replace(r'γ', '''${\\gamma}$''')
  line = line.replace(r'δ', '''${\\delta}$''')
  line = line.replace(r'ε', '''${\\varepsilon}$''')
  line = line.replace(r'ζ', '''${\\zeta}$''')
  line = line.replace(r'η', '''${\\eta}$''')
  line = line.replace(r'θ', '''${\\theta}$''')
  line = line.replace(r'ι', '''${\\iota}$''')
  line = line.replace(r'κ', '''${\\kappa}$''')
  line = line.replace(r'λ', '''${\\lambda}$''')
  line = line.replace(r'μ', '''${\\mu}$''')
  line = line.replace(r'ν', '''${\\nu}$''')
  line = line.replace(r'ξ', '''${\\xi}$''')
  line = line.replace(r'ο', '''${o}$''')
  line = line.replace(r'π', '''${\\pi}$''')
  line = line.replace(r'ρ', '''${\\rho}$''')
  line = line.replace(r'σ', '''${\\sigma}$''')
  line = line.replace(r'τ', '''${\\tau}$''')
  line = line.replace(r'υ', '''${\\upsilon}$''')
  line = line.replace(r'φ', '''${\\phi}$''')
  line = line.replace(r'χ', '''${\\chi}$''')
  line = line.replace(r'ψ', '''${\\psi}$''')
  line = line.replace(r'ω', '''${\\omega}$''')
  return line


if __name__ == '__main__':
  parser = ap(description='Convert Zotero .bib file.')
  parser.add_argument(
    'input_bib', metavar='src', type=str,
    help='source .bib file to be converted.')
  parser.add_argument(
    'output_bib', metavar='output', type=str,
    help='output .bib file for bibtex.')


  args = parser.parse_args()

  inside_elem = 0
  with codecs.open(args.input_bib, 'r', 'utf-8') as fin:
    with codecs.open(args.output_bib, 'w', 'utf-8') as fout:
      writeln = r''
      for line in fin:
        line = convert_bar(line)
        line = convert_uml(line)
        line = convert_grave(line)
        line = convert_cedil(line)
        line = convert_acute(line)
        line = convert_greece(line)
        line = convert_signs(line)
        inside_elem += line.count(r'{')
        inside_elem -= line.count(r'}')
        line = re.sub(r'\n','',line)
        line = convert_date_year(line)
        writeln += line
        if inside_elem==1:
          writeln = wrap_name_with_brace(writeln)
          fout.write(writeln)
          fout.write('\n')
          writeln = r''
        if inside_elem==0:
          fout.write(writeln)
          fout.write('\n')
          writeln = r''
