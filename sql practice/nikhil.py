# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:00:32 2024

@author: Dixit
"""

import sqlalchemy as sql

metadata=sql.MetaData()

friends=sql.Table("friends", metadata, 
                 sql.Column("Friend_ID",sql.INTEGER(),index=True,primary_key=True) ,
                 sql.Column("Friend_Name",sql.String(),index=True), 
                 sql.Column("Friend_Phone_no",sql.INTEGER(),unique=True),
                 )

engine=sql.create_engine("sqlite:///friends.db")
connection=engine.connect()
metadata.create_all(engine)
 
ins=friends.insert().values(
    Friend_ID=1,
    Friend_Name="Nikhil Tiwari",
    Friend_Phone_no=6261201780,
    )
print(str(ins))

result=connection.execute(ins)

