import main

def test_10_lines():
  lines = [
    '{ "name": "Stokes Baker", "value": 954832 }',
    '{ "name": "Joseph Solomon", "value": 279836 }',
    '{ "name": "Gonzalez Koch", "value": 140431 }',
    '{ "name": "Parrish Waters", "value": 490411 }',
    '{ "name": "Sharlene Nunez", "value": 889667 }',
    '{ "name": "Meadows David", "value": 892040 }',
    '{ "name": "Whitley Mendoza", "value": 965462 }',
    '{ "name": "Santiago Hood", "value": 280041 }',
    '{ "name": "Carver Caldwell", "value": 632926 }',
    '{ "name": "Tara Patterson", "value": 678175 }',
  ]

  assert main.sum(lines) == 6203958