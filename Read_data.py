



import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred=credentials.Certificate('/home/sahil/Desktop/testapp-10f69-firebase-adminsdk-84avv-136ea6e1b7.json')
firebase_admin.initialize_app(cred)

db=firestore.client()





class City(object):
    def __init__(self, name, state, country, capital=False, population=0,
                 regions=[]):
        self.name = name
        self.state = state
        self.country = country
        self.capital = capital
        self.population = population
        self.regions = regions

    @staticmethod
    def from_dict(source):
       pass

    def to_dict(self):
       pass

    def __repr__(self):
        return(
            f'City(\
                name={self.name}, \
                country={self.country}, \
                population={self.population}, \
                capital={self.capital}, \
                regions={self.regions}\
            )'
        )
# make the collection
cities_ref = db.collection(u'cities')

#Add documents to the collection
cities_ref.document(u'BJ').set(City(u'Beijing', None, u'China', True, 21500000, [u'hebei']).to_dict())
cities_ref.document(u'SF').set(City(u'San Francisco', u'CA', u'USA', False, 860000,[u'west_coast', u'norcal']).to_dict())
cities_ref.document(u'LA').set(City(u'Los Angeles', u'CA', u'USA', False, 3900000,[u'west_coast', u'socal']).to_dict())
cities_ref.document(u'DC').set(City(u'Washington D.C.', None, u'USA', True, 680000,[u'east_coast']).to_dict())
cities_ref.document(u'TOK').set(City(u'Tokyo', None, u'Japan', True, 9000000,[u'kanto', u'honshu']).to_dict())

# Read the data

doc_ref=cities_ref.document(u'SF')
doc=doc_ref.get()

if doc.exists:
    print('Document data:')
    # for ele in doc:
    #     print(ele)
    # doc is not iterable. Its just an object

    city=City.from_dict(doc.to_dict())
    print(city)
else:
    print('No such document')

# Get multiple documents from a collection

# Note: Use of CollectionRef stream() is prefered to get()

docs = db.collection(u'cities').where(u'capital', u'==', True).stream()

# Streams are high-level async/await-ready primitives to work with network connections.
# Streams allow sending and receiving data without using callbacks or low-level protocols and
# transports.

for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')