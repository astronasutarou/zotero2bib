#!/usr/bin/python
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
  line = line.replace(r'¡', u'''{!`}''')
  line = line.replace(r'¿', u'''{?`}''')
  line = line.replace(r'ø', u'''{\\o}''')
  line = line.replace(r'Ø', u'''{\\O}''')
  line = line.replace(r'ñ', u'''{\\~n}''')
  line = line.replace(r'Ñ', u'''{\\~N}''')
  line = line.replace(r'č', u'''{\\v{c}}''')
  line = line.replace(r'Č', u'''{\\v{C}}''')
  line = line.replace(r'š', u'''{\\v{s}}''')
  line = line.replace(r'Š', u'''{\\v{S}}''')
  line = line.replace(r'ž', u'''{\\v{z}}''')
  line = line.replace(r'Ž', u'''{\\v{Z}}''')
  line = line.replace(r'¢', u'''{}''')
  line = line.replace(r'\$', u'''{\\$}''')
  line = line.replace(r'€', u'''{}''')
  line = line.replace(r'ł', u'''{\\l}''')
  line = line.replace(r'Ł', u'''{\\L}''')
  # line = line.replace(r'%', u'''{\\%}''')
  line = line.replace(r'ß', u'''{\\ss}''')
  line = line.replace(r'⊙', u'''${_\\odot}$''')
  line = line.replace(r'≥', u'''${\\ge}$''')
  line = line.replace(r'≤', u'''${\\le}$''')
  line = line.replace(r'∼', u'''{\\textasciitilde}''')
  line = line.replace(r'Ø,', u'''{\O}''')
  line = line.replace(r'ø', u'''{\o}''')
  return line

def convert_bar(line):
  line = line.replace(r'ā', u'''{\\=a}''')
  line = line.replace(r'ē', u'''{\\=e}''')
  line = line.replace(r'ū', u'''{\\=u}''')
  line = line.replace(r'ī', u'''{\\=i}''')
  line = line.replace(r'ō', u'''{\\=o}''')
  line = line.replace(r'Ā', u'''{\\=A}''')
  line = line.replace(r'Ē', u'''{\\=E}''')
  line = line.replace(r'Ū', u'''{\\=U}''')
  line = line.replace(r'Ī', u'''{\\=I}''')
  line = line.replace(r'Ō', u'''{\\=O}''')
  return line

def convert_acute(line):
  line = line.replace(r'á', u'''{\\'a}''')
  line = line.replace(r'é', u'''{\\'e}''')
  line = line.replace(r'ú', u'''{\\'u}''')
  line = line.replace(r'í', u'''{\\'i}''')
  line = line.replace(r'ó', u'''{\\'o}''')
  line = line.replace(r'Á', u'''{\\'A}''')
  line = line.replace(r'É', u'''{\\'E}''')
  line = line.replace(r'Ú', u'''{\\'U}''')
  line = line.replace(r'Í', u'''{\\'I}''')
  line = line.replace(r'Ó', u'''{\\'O}''')
  line = line.replace(r'ć', u'''{\\'c}''')
  line = line.replace(r'Ć', u'''{\\'C}''')
  line = line.replace(r'ĺ', u'''{\\'l}''')
  line = line.replace(r'Ĺ', u'''{\\'L}''')
  line = line.replace(r'ń', u'''{\\'n}''')
  line = line.replace(r'Ń', u'''{\\'N}''')
  line = line.replace(r'ŕ', u'''{\\'r}''')
  line = line.replace(r'Ŕ', u'''{\\'R}''')
  line = line.replace(r'ś', u'''{\\'s}''')
  line = line.replace(r'Ś', u'''{\\'S}''')
  line = line.replace(r'ú', u'''{\\'u}''')
  line = line.replace(r'Ú', u'''{\\'U}''')
  line = line.replace(r'ý', u'''{\\'y}''')
  line = line.replace(r'Ý', u'''{\\'Y}''')
  line = line.replace(r'ź', u'''{\\'z}''')
  line = line.replace(r'Ź', u'''{\\'Z}''')
  return line

def convert_uml(line):
  line = line.replace(r'ä', u'''{\\"a}''')
  line = line.replace(r'ë', u'''{\\"e}''')
  line = line.replace(r'ü', u'''{\\"u}''')
  line = line.replace(r'ï', u'''{\\"i}''')
  line = line.replace(r'ö', u'''{\\"o}''')
  line = line.replace(r'Ä', u'''{\\"A}''')
  line = line.replace(r'Ë', u'''{\\"E}''')
  line = line.replace(r'Ü', u'''{\\"U}''')
  line = line.replace(r'Ï', u'''{\\"I}''')
  line = line.replace(r'Ö', u'''{\\"O}''')
  return line

def convert_cedil(line):
  line = line.replace(r'ą', u'''{\\c{a}}''')
  line = line.replace(r'Ą', u'''{\\c{A}}''')
  line = line.replace(r'ç', u'''{\\c{c}}''')
  line = line.replace(r'Ç', u'''{\\c{C}}''')
  line = line.replace(r'ę', u'''{\\c{e}}''')
  line = line.replace(r'Ę', u'''{\\c{E}}''')
  line = line.replace(r'ģ', u'''{\\c{g}}''')
  line = line.replace(r'Ģ', u'''{\\c{G}}''')
  line = line.replace(r'į', u'''{\\c{i}}''')
  line = line.replace(r'Į', u'''{\\c{I}}''')
  line = line.replace(r'ķ', u'''{\\c{k}}''')
  line = line.replace(r'Ķ', u'''{\\c{K}}''')
  line = line.replace(r'ļ', u'''{\\c{l}}''')
  line = line.replace(r'Ļ', u'''{\\c{C}}''')
  line = line.replace(r'ņ', u'''{\\c{n}}''')
  line = line.replace(r'Ņ', u'''{\\c{C}}''')
  line = line.replace(r'ŗ', u'''{\\c{r}}''')
  line = line.replace(r'Ŗ', u'''{\\c{C}}''')
  line = line.replace(r'ş', u'''{\\c{s}}''')
  line = line.replace(r'Ş', u'''{\\c{C}}''')
  line = line.replace(r'ţ', u'''{\\c{t}}''')
  line = line.replace(r'Ţ', u'''{\\c{C}}''')
  line = line.replace(r'ų', u'''{\\c{u}}''')
  line = line.replace(r'Ų', u'''{\\c{C}}''')
  return line

def convert_grave(line):
  line = line.replace(r'à', u'''{\\`a}''')
  line = line.replace(r'è', u'''{\\`e}''')
  line = line.replace(r'ù', u'''{\\`u}''')
  line = line.replace(r'Ì', u'''{\\`i}''')
  line = line.replace(r'ò', u'''{\\`o}''')
  line = line.replace(r'À', u'''{\\`A}''')
  line = line.replace(r'È', u'''{\\`E}''')
  line = line.replace(r'Ū', u'''{\\`U}''')
  line = line.replace(r'Ì', u'''{\\`I}''')
  line = line.replace(r'Ù', u'''{\\`O}''')
  return line

def convert_greece(line):
  line = line.replace(r'Α', u'''${A}$''')
  line = line.replace(r'Β', u'''${B}$''')
  line = line.replace(r'Γ', u'''${\\Gamma}$''')
  line = line.replace(r'Δ', u'''${\\Delta}$''')
  line = line.replace(r'Ε', u'''${E}$''')
  line = line.replace(r'Ζ', u'''${Z}$''')
  line = line.replace(r'Η', u'''${H}$''')
  line = line.replace(r'Θ', u'''${\\Theta}$''')
  line = line.replace(r'Ι', u'''${I}$''')
  line = line.replace(r'Κ', u'''${K}$''')
  line = line.replace(r'Λ', u'''${\\Lambda}$''')
  line = line.replace(r'Μ', u'''${M}$''')
  line = line.replace(r'Ν', u'''${N}$''')
  line = line.replace(r'Ξ', u'''${\\Xi}$''')
  line = line.replace(r'Ο', u'''${O}$''')
  line = line.replace(r'Π', u'''${\\Pi}$''')
  line = line.replace(r'Ρ', u'''${P}$''')
  line = line.replace(r'Σ', u'''${\\Sigma}$''')
  line = line.replace(r'Τ', u'''${T}$''')
  line = line.replace(r'Υ', u'''${\\Upsilon}$''')
  line = line.replace(r'Φ', u'''${\\Phi}$''')
  line = line.replace(r'Χ', u'''${\\Chi}$''')
  line = line.replace(r'Ψ', u'''${\\Psi}$''')
  line = line.replace(r'Ω', u'''${\\Omega}$''')
  line = line.replace(r'α', u'''${\\alpha}$''')
  line = line.replace(r'β', u'''${\\beta}$''')
  line = line.replace(r'γ', u'''${\\gamma}$''')
  line = line.replace(r'δ', u'''${\\delta}$''')
  line = line.replace(r'ε', u'''${\\varepsilon}$''')
  line = line.replace(r'ζ', u'''${\\zeta}$''')
  line = line.replace(r'η', u'''${\\eta}$''')
  line = line.replace(r'θ', u'''${\\theta}$''')
  line = line.replace(r'ι', u'''${\\iota}$''')
  line = line.replace(r'κ', u'''${\\kappa}$''')
  line = line.replace(r'λ', u'''${\\lambda}$''')
  line = line.replace(r'μ', u'''${\\mu}$''')
  line = line.replace(r'ν', u'''${\\nu}$''')
  line = line.replace(r'ξ', u'''${\\xi}$''')
  line = line.replace(r'ο', u'''${o}$''')
  line = line.replace(r'π', u'''${\\pi}$''')
  line = line.replace(r'ρ', u'''${\\rho}$''')
  line = line.replace(r'σ', u'''${\\sigma}$''')
  line = line.replace(r'τ', u'''${\\tau}$''')
  line = line.replace(r'υ', u'''${\\upsilon}$''')
  line = line.replace(r'φ', u'''${\\phi}$''')
  line = line.replace(r'χ', u'''${\\chi}$''')
  line = line.replace(r'ψ', u'''${\\psi}$''')
  line = line.replace(r'ω', u'''${\\omega}$''')
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
