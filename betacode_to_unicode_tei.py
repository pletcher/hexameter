#!/usr/bin/env python3

import sys
from xml.etree import ElementTree
from betacode import betacode_to_unicode

if __name__ == '__main__':
    with open(sys.argv[1]) as in_f:
        in_s = in_f.read()
    in_s = in_s.replace('&responsibility;', '')
    in_s = in_s.replace('&fund.AnnCPB;', '')
    in_s = in_s.replace('&Perseus.publish;', '')
    in_s = in_s.replace('&lsqb;', '[')
    in_s = in_s.replace('&rsqb;', ']')
    in_s = in_s.replace('&lsquo;', '"')
    in_s = in_s.replace('&rsquo;', '"')
    in_s = in_s.replace('&ldquo;', '"')
    in_s = in_s.replace('&rdquo;', '"')
    in_s = in_s.replace('&mdash;', '—')
    tei = ElementTree.XML(in_s)
    text = tei.find('text')
    for node in text.iter():
        if node.text:
            node.text = betacode_to_unicode(node.text)
        if node.tail:
            node.tail = betacode_to_unicode(node.tail)
    out_s = ElementTree.tostring(tei, encoding='unicode')
    sys.stdout.write(out_s)
