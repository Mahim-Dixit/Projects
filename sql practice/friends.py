# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:33:09 2024

@author: Dixit
"""
from sqlalchemy import Table,Column,create_engine,MetaData,INTEGER,String,NUMERIC,Index
metadata=MetaData()
friends=Table("friends", metadata, 
              Column("Friend_id",INTEGER(),index=True,primary_key=True),
              Column("Friend_name",String(25),index=True),
              Column("Friend_phone_no",INTEGER(),unique=True),
              )


engine=create_engine("sqlite:///Friends.db")
connection=engine.connect()

metadata.create_all(engine)
