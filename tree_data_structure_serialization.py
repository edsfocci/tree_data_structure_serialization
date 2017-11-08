import re

def jsonify_str(text):
  result_text = re.compile(r'\\?\"').sub(r'\\"', text)
  result_text = re.compile(r"\\?'").sub(r"'", result_text)

  return '"{}"'.format(result_text)

class Tree(object):
  def __init__(self, value):
    if type(value) == str:
      value = jsonify_str(value)

    self.value = value
    self.children = []

  @classmethod
  def from_dict(cls, dataDict):
    root = cls(dataDict['value'])

    if dataDict.get('children'):
      root.children = list(map(lambda childDict: cls.from_dict(childDict),
                            dataDict['children']))

    return root

  # First value of lists become the value of the Tree,
  # and the rest of the values become children of the Tree.
  @classmethod
  def from_list(cls, dataList):
    root = cls(dataList[0])

    def convert_to_child(item):
      if type(item) is list:
        return cls.from_list(item)
      else:
        return cls(item)

    root.children = list(map(convert_to_child, dataList[1:]))

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
        {'value': 'Drake'},
        {'value': 30},
      ]
    },
    {
      'value': 8,
      'children': []
    },
  ]
}))
print(Tree.from_list([3, 2, [4], [6, 10, 'drake', 30], 8]))
