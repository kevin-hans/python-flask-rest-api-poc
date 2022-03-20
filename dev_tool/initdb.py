from globalapp import db
from model.user import User
from model.photo import Photo

db.create_all()

db.session.add(User(lastName = 'Snow', firstName=  'Jon', age = 35))
db.session.add(User(lastName = 'Lannister', firstName = 'Cersei', age =  42))
db.session.add(User(lastName = 'Lannister', firstName = 'Jaime', age =  45))
db.session.add(User(lastName = 'Stark', firstName = 'Arya', age =  16))
db.session.add(User(lastName = 'Targaryen', firstName = 'Daenerys', age =  6))
db.session.add(User(lastName = 'Melisandre', firstName = 'test', age =  150))
db.session.add(User(lastName = 'Clifford', firstName = 'Ferrara', age =  44))
db.session.add(User(lastName = 'Frances', firstName = 'Rossini', age =  36))
db.session.add(User(lastName = 'Roxie', firstName = 'Harvey', age =  65))

db.session.add(Photo(img =  'https://images.unsplash.com/photo-1551963831-b3b1ca40c98e', \
                    title ='Breakfast',   \
                    rows = 2,  \
                    cols = 2))


db.session.add(Photo(   \
            img = 'https://images.unsplash.com/photo-1551782450-a2132b4ba21d', \
            title = 'Burger', \
          ))
db.session.add(Photo(   \
            img = 'https://images.unsplash.com/photo-1522770179533-24471fcdba45', \
            title = 'Camera', \
          ))
db.session.add(Photo(   \
            img = 'https://images.unsplash.com/photo-1444418776041-9c7e33cc5a9c', \
            title = 'Coffee', \
            cols =  2, \
          ))
db.session.add(Photo(   \
            img = 'https://images.unsplash.com/photo-1533827432537-70133748f5c8', \
            title = 'Hats', \
            cols =  2, \
          ))
db.session.add(Photo(   \
            img = 'https://images.unsplash.com/photo-1558642452-9d2a7deb7f62', \
            title = 'Honey', \
            author = '@arwinneil', \
            rows = 2, \
            cols =  2, \
          ))
db.session.add(Photo(   \
            img = 'https://images.unsplash.com/photo-1516802273409-68526ee1bdd6', \
            title = 'Basketball', \
          ))
db.session.add(Photo(   \
            img = 'https://images.unsplash.com/photo-1518756131217-31eb79b20e8f', \
            title = 'Fern', \
          ))
db.session.add(Photo(   \
            img = 'https://images.unsplash.com/photo-1597645587822-e99fa5d45d25', \
            title = 'Mushrooms', \
            rows = 2, \
            cols =  2, \
          ))
db.session.add(Photo(   \
            img = 'https://images.unsplash.com/photo-1567306301408-9b74779a11af', \
            title = 'Tomato basil', \
          ))
db.session.add(Photo(   \
            img = 'https://images.unsplash.com/photo-1471357674240-e1a485acb3e1', \
            title = 'Sea star', \
          ))
db.session.add(Photo(   \
            img = 'https://images.unsplash.com/photo-1589118949245-7d38baf380d6', \
            title = 'Bike', \
            cols =  2, \
          ))


db.session.commit()