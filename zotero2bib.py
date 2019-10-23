#!/usr/bin/python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser as ap
import re, codecs


def convert_date_year(line):
  try:
    regex = re.search(ur'^\s*date = {(....)', line)
    year = regex.groups()[0]
    line = '        year = {{{}}},\n{}'.format(year, line)
    return line
  except:
    return line

def wrap_name_with_brace(line):
  if line.find('author = {') == -1:
    return line
  else:
    regex = re.search(ur'(.*author = {)(.*)(},?\s*)$', line)
    pre,authors,post = regex.groups()
    names = re.split(ur'\s+and\s+', authors)
    newnames = []
    for name in names:
      if name.find(',') > 0:
        newnames.append(name)
      else:
        newnames.append('{' + name + '}')
    return pre+' and '.join(newnames)+post

def convert_signs(line):
  line = line.replace(ur'¡', u'''{!`}''')
  line = line.replace(ur'¿', u'''{?`}''')
  line = line.replace(ur'ø', u'''{\\o}''')
  line = line.replace(ur'Ø', u'''{\\O}''')
  line = line.replace(ur'ñ', u'''{\\~n}''')
  line = line.replace(ur'Ñ', u'''{\\~N}''')
  line = line.replace(ur'č', u'''{\\v{c}}''')
  line = line.replace(ur'Č', u'''{\\v{C}}''')
  line = line.replace(ur'š', u'''{\\v{s}}''')
  line = line.replace(ur'Š', u'''{\\v{S}}''')
  line = line.replace(ur'ž', u'''{\\v{z}}''')
  line = line.replace(ur'Ž', u'''{\\v{Z}}''')
  line = line.replace(ur'¢', u'''{}''')
  line = line.replace(ur'\$', u'''{\\$}''')
  line = line.replace(ur'€', u'''{}''')
  line = line.replace(ur'ł', u'''{\\l}''')
  line = line.replace(ur'Ł', u'''{\\L}''')
  # line = line.replace(ur'%', u'''{\\%}''')
  line = line.replace(ur'ß', u'''{\\ss}''')
  line = line.replace(ur'⊙', u'''${_\\odot}$''')
  line = line.replace(ur'≥', u'''${\\ge}$''')
  line = line.replace(ur'≤', u'''${\\le}$''')
  line = line.replace(ur'∼', u'''{\\textasciitilde}''')
  line = line.replace(ur'Ø,', u'''{\O}''')
  line = line.replace(ur'ø', u'''{\o}''')
  return line

def convert_bar(line):
  line = line.replace(ur'ā', u'''{\\=a}''')
  line = line.replace(ur'ē', u'''{\\=e}''')
  line = line.replace(ur'ū', u'''{\\=u}''')
  line = line.replace(ur'ī', u'''{\\=i}''')
  line = line.replace(ur'ō', u'''{\\=o}''')
  line = line.replace(ur'Ā', u'''{\\=A}''')
  line = line.replace(ur'Ē', u'''{\\=E}''')
  line = line.replace(ur'Ū', u'''{\\=U}''')
  line = line.replace(ur'Ī', u'''{\\=I}''')
  line = line.replace(ur'Ō', u'''{\\=O}''')
  return line

def convert_acute(line):
  line = line.replace(ur'á', u'''{\\'a}''')
  line = line.replace(ur'é', u'''{\\'e}''')
  line = line.replace(ur'ú', u'''{\\'u}''')
  line = line.replace(ur'í', u'''{\\'i}''')
  line = line.replace(ur'ó', u'''{\\'o}''')
  line = line.replace(ur'Á', u'''{\\'A}''')
  line = line.replace(ur'É', u'''{\\'E}''')
  line = line.replace(ur'Ú', u'''{\\'U}''')
  line = line.replace(ur'Í', u'''{\\'I}''')
  line = line.replace(ur'Ó', u'''{\\'O}''')
  line = line.replace(ur'ć', u'''{\\'c}''')
  line = line.replace(ur'Ć', u'''{\\'C}''')
  line = line.replace(ur'ĺ', u'''{\\'l}''')
  line = line.replace(ur'Ĺ', u'''{\\'L}''')
  line = line.replace(ur'ń', u'''{\\'n}''')
  line = line.replace(ur'Ń', u'''{\\'N}''')
  line = line.replace(ur'ŕ', u'''{\\'r}''')
  line = line.replace(ur'Ŕ', u'''{\\'R}''')
  line = line.replace(ur'ś', u'''{\\'s}''')
  line = line.replace(ur'Ś', u'''{\\'S}''')
  line = line.replace(ur'ú', u'''{\\'u}''')
  line = line.replace(ur'Ú', u'''{\\'U}''')
  line = line.replace(ur'ý', u'''{\\'y}''')
  line = line.replace(ur'Ý', u'''{\\'Y}''')
  line = line.replace(ur'ź', u'''{\\'z}''')
  line = line.replace(ur'Ź', u'''{\\'Z}''')
  return line

def convert_uml(line):
  line = line.replace(ur'ä', u'''{\\"a}''')
  line = line.replace(ur'ë', u'''{\\"e}''')
  line = line.replace(ur'ü', u'''{\\"u}''')
  line = line.replace(ur'ï', u'''{\\"i}''')
  line = line.replace(ur'ö', u'''{\\"o}''')
  line = line.replace(ur'Ä', u'''{\\"A}''')
  line = line.replace(ur'Ë', u'''{\\"E}''')
  line = line.replace(ur'Ü', u'''{\\"U}''')
  line = line.replace(ur'Ï', u'''{\\"I}''')
  line = line.replace(ur'Ö', u'''{\\"O}''')
  return line

def convert_cedil(line):
  line = line.replace(ur'ą', u'''{\\c{a}}''')
  line = line.replace(ur'Ą', u'''{\\c{A}}''')
  line = line.replace(ur'ç', u'''{\\c{c}}''')
  line = line.replace(ur'Ç', u'''{\\c{C}}''')
  line = line.replace(ur'ę', u'''{\\c{e}}''')
  line = line.replace(ur'Ę', u'''{\\c{E}}''')
  line = line.replace(ur'ģ', u'''{\\c{g}}''')
  line = line.replace(ur'Ģ', u'''{\\c{G}}''')
  line = line.replace(ur'į', u'''{\\c{i}}''')
  line = line.replace(ur'Į', u'''{\\c{I}}''')
  line = line.replace(ur'ķ', u'''{\\c{k}}''')
  line = line.replace(ur'Ķ', u'''{\\c{K}}''')
  line = line.replace(ur'ļ', u'''{\\c{l}}''')
  line = line.replace(ur'Ļ', u'''{\\c{C}}''')
  line = line.replace(ur'ņ', u'''{\\c{n}}''')
  line = line.replace(ur'Ņ', u'''{\\c{C}}''')
  line = line.replace(ur'ŗ', u'''{\\c{r}}''')
  line = line.replace(ur'Ŗ', u'''{\\c{C}}''')
  line = line.replace(ur'ş', u'''{\\c{s}}''')
  line = line.replace(ur'Ş', u'''{\\c{C}}''')
  line = line.replace(ur'ţ', u'''{\\c{t}}''')
  line = line.replace(ur'Ţ', u'''{\\c{C}}''')
  line = line.replace(ur'ų', u'''{\\c{u}}''')
  line = line.replace(ur'Ų', u'''{\\c{C}}''')
  return line

def convert_grave(line):
  line = line.replace(ur'à', u'''{\\`a}''')
  line = line.replace(ur'è', u'''{\\`e}''')
  line = line.replace(ur'ù', u'''{\\`u}''')
  line = line.replace(ur'Ì', u'''{\\`i}''')
  line = line.replace(ur'ò', u'''{\\`o}''')
  line = line.replace(ur'À', u'''{\\`A}''')
  line = line.replace(ur'È', u'''{\\`E}''')
  line = line.replace(ur'Ū', u'''{\\`U}''')
  line = line.replace(ur'Ì', u'''{\\`I}''')
  line = line.replace(ur'Ù', u'''{\\`O}''')
  return line

def convert_greece(line):
  line = line.replace(ur'Α', u'''${A}$''')
  line = line.replace(ur'Β', u'''${B}$''')
  line = line.replace(ur'Γ', u'''${\\Gamma}$''')
  line = line.replace(ur'Δ', u'''${\\Delta}$''')
  line = line.replace(ur'Ε', u'''${E}$''')
  line = line.replace(ur'Ζ', u'''${Z}$''')
  line = line.replace(ur'Η', u'''${H}$''')
  line = line.replace(ur'Θ', u'''${\\Theta}$''')
  line = line.replace(ur'Ι', u'''${I}$''')
  line = line.replace(ur'Κ', u'''${K}$''')
  line = line.replace(ur'Λ', u'''${\\Lambda}$''')
  line = line.replace(ur'Μ', u'''${M}$''')
  line = line.replace(ur'Ν', u'''${N}$''')
  line = line.replace(ur'Ξ', u'''${\\Xi}$''')
  line = line.replace(ur'Ο', u'''${O}$''')
  line = line.replace(ur'Π', u'''${\\Pi}$''')
  line = line.replace(ur'Ρ', u'''${P}$''')
  line = line.replace(ur'Σ', u'''${\\Sigma}$''')
  line = line.replace(ur'Τ', u'''${T}$''')
  line = line.replace(ur'Υ', u'''${\\Upsilon}$''')
  line = line.replace(ur'Φ', u'''${\\Phi}$''')
  line = line.replace(ur'Χ', u'''${\\Chi}$''')
  line = line.replace(ur'Ψ', u'''${\\Psi}$''')
  line = line.replace(ur'Ω', u'''${\\Omega}$''')
  line = line.replace(ur'α', u'''${\\alpha}$''')
  line = line.replace(ur'β', u'''${\\beta}$''')
  line = line.replace(ur'γ', u'''${\\gamma}$''')
  line = line.replace(ur'δ', u'''${\\delta}$''')
  line = line.replace(ur'ε', u'''${\\varepsilon}$''')
  line = line.replace(ur'ζ', u'''${\\zeta}$''')
  line = line.replace(ur'η', u'''${\\eta}$''')
  line = line.replace(ur'θ', u'''${\\theta}$''')
  line = line.replace(ur'ι', u'''${\\iota}$''')
  line = line.replace(ur'κ', u'''${\\kappa}$''')
  line = line.replace(ur'λ', u'''${\\lambda}$''')
  line = line.replace(ur'μ', u'''${\\mu}$''')
  line = line.replace(ur'ν', u'''${\\nu}$''')
  line = line.replace(ur'ξ', u'''${\\xi}$''')
  line = line.replace(ur'ο', u'''${o}$''')
  line = line.replace(ur'π', u'''${\\pi}$''')
  line = line.replace(ur'ρ', u'''${\\rho}$''')
  line = line.replace(ur'σ', u'''${\\sigma}$''')
  line = line.replace(ur'τ', u'''${\\tau}$''')
  line = line.replace(ur'υ', u'''${\\upsilon}$''')
  line = line.replace(ur'φ', u'''${\\phi}$''')
  line = line.replace(ur'χ', u'''${\\chi}$''')
  line = line.replace(ur'ψ', u'''${\\psi}$''')
  line = line.replace(ur'ω', u'''${\\omega}$''')
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
      writeln = ur''
      for line in fin:
        line = convert_bar(line)
        line = convert_uml(line)
        line = convert_grave(line)
        line = convert_cedil(line)
        line = convert_acute(line)
        line = convert_greece(line)
        line = convert_signs(line)
        inside_elem += line.count(ur'{')
        inside_elem -= line.count(ur'}')
        line = re.sub(ur'\n','',line)
        line = convert_date_year(line)
        writeln += line
        if inside_elem==1:
          writeln = wrap_name_with_brace(writeln)
          fout.write(writeln)
          fout.write('\n')
          writeln = ur''
        if inside_elem==0:
          fout.write(writeln)
          fout.write('\n')
          writeln = ur''
