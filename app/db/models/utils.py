from .medium import Medium


def getUrls(mediaUrlIds):
  urls = []
  if mediaUrlIds:
    for mediumId in mediaUrlIds:
      medium = Medium.query.get(mediumId)
      if medium: 
        url = medium.url
        if url.startswith('/resources'):
          url = 'https://tripcamp.s3.amazonaws.com' + url
        urls.append(url)
  return urls

def utils_to_dict(classInstance, *args):
  dct = {attr: getattr(classInstance, attr) \
    for attr in dir(classInstance) \
    if not callable(getattr(classInstance, attr)) \
    and not attr.startswith("_")  \
    and not attr.startswith("__") \
    and attr not in args  }
  
  if 'mediaUrlIds' in args:
    dct['urls'] = getUrls(getattr(classInstance,'mediaUrlIds'))

  return dict(dct)

def attrs(classInstance, *args):
  lst = [attr \
    for attr in dir(classInstance) \
    if not callable(getattr(classInstance, attr)) \
    and not attr.startswith("_")  \
    and not attr.startswith("__") \
    and attr not in args  ]
  

  return lst

  '''
  type ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
  '''

