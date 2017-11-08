class Tree(object):
  def __init__(self, value):
    self.value = value
    self.children = []

  @classmethod
  def from_dict(cls, dataDict):
    root = cls(dataDict['value'])

    if dataDict.get('children'):
      root.children = list(map(lambda childDict: cls.from_dict(childDict),
                            dataDict['children']))

    return root

  def __str__(self):
    output = '(' + str(self.value)

    if len(self.children) > 0:
      output += ', ['
      output += ', '.join(map(lambda child: str(child), self.children))
      output += ']'

    return output + ')'

print(Tree.from_dict({
  'value': 3,
  'children': [
    {
      'value': 2
    },
    {
      'value': 4
    },
    {
      'value': 6,
      'children': [
        {'value': 10},
        {'value': 20},
        {'value': 30},
      ]
    },
    {
      'value': 8
    },
  ]
}))
