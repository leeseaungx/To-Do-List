#!/usr/bin/env python
# -*- coding:utf-8 -*-
from app import db
import datetime
from flask_mongoengine.wtf import model_form

class Todo(db.Document):
    content = db.StringField()
    time = db.DateTimeField(default=datetime.datetime.now())
    status = db.IntField(default=0)

TodoForm = model_form(Todo)
