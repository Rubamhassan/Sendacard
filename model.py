# """Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can
# find the `session` object, where we do most of our interactions
# (like committing, etc.)

db = SQLAlchemy()


####################################################################


class Background(db.Model):
    """Categories which users can choose from"""

    __tablename__="backgrounds"

    background_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    background_name = db.Column(db.String(35), nullable=True)
    

    def __repr__(self):
       


        """Show category and associated id """

        return "<Category ID=%d Category=%s>" % (self.background_id,self.background_name)



class UserBackground(db.Model):
    """A table to link users and their interests"""


    __tablename__ = 'users_backgrounds'

    user_background_id = db.Column(db.Integer,
                     autoincrement=True,
                     primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    background_id = db.Column(db.Integer, db.ForeignKey('backgrounds.background_id'))
    

    def __repr__(self):
        """Table to associate user_id and category_id's...each have their own association id"""

        return "UserCategory=%d User=%d Category=%d" %(self.user_background_id,self.user_id,self.background_id)




def make_test_data():
    """populate a db with test data; used in testing"""
    
    # # make a couple users
    # lori = User(firstname='lori', lastname='bard', email='lori@bardfamily.org', password = "lori")
    # junior = User(firstname='junior', lastname='bard', email='ls@fmail.com', password = 'junior')
    # rusty = User(firstname='rusty', lastname='cat', email='rusty@bardfamiy.org', password='rusty')

    # We need to add to the session or it won't ever be stored
    db.session.add_all([lori, junior, rusty])

    # make a couple categories
    white_christmas = Background(background_name='White_Christmas', background = "/static/white_christmas_baubles_187316 2.jpg", color = '#990000', font = 'Papyrus' )
    tree_christmas = Background(background_name='Christmas_tree', background = "/static/christmas_tree_182821.jpg", color = 'FFD7000', font = "Monaco")
    # We need to add to the session or it won't ever be stored
    db.session.add_all([white_christmas,tree_christmas])

    db.session.flush()

    # # make a couple association table enries
    # lori_white_christmas = UserCategory(user_id=lori.user_id, background_id=white_christmas.background_id)
    # rusty_tree_christmas = UserCategory(user_id=rusty.user_id, background_id=tree_christmas.background_id)
    # junior_tree_christmas = UserCategory(user_id=junior.user_id, category_id=tree_christmas.background_id)

    # We need to add to the session or it won't ever be stored
    db.session.add_all([lori_white_christmas,rusty_tree_christmas,junior_tree_christmas])

    db.session.commit()
        

#####################################################################
# Helper functions

def connect_to_db(app, db_uri=None 

    ):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri or 'postgresql:///backgrounds'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    

    connect_to_db(app)
    
    print "Connected to DB"
