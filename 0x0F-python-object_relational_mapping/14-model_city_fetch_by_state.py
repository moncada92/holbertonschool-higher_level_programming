#!/usr/bin/python3
"""
select all table cities
"""

if __name__ == "__main__":

    from model_state import Base, State
    from model_city import City
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                            sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City, State).filter(
            State.id == City.state_id).order_by(City.id).all()

    for c, s in query:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
    session.close()
