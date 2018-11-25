import sys

import xmltodict

f = sys.argv[1]


def toKMLFormat(doc):
  result = {
    'kml': {
      '@xmlns': 'http://www.opengis.net/kml/2.2',
      'Document': {
        'Folder': {
          'name': 'export',
          'Placemark': []
        }
      }
    }
  }

  placemarks = result['kml']['Document']['Folder']['Placemark']

  for v in doc['markers']['marker']:
    placemarks.append({
      'name': v['label'].replace('<br>', ' '),
      'Point': {
        'coordinates': '{0},{1}'.format(v['@lng'], v['@lat'])
      }
    })

  return result


with open(f, 'r') as file:
  text = file.read()
  doc = xmltodict.parse(text)

  print(xmltodict.unparse(toKMLFormat(doc)))
