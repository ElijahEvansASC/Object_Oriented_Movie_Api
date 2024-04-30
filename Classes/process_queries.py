from __future__ import annotations
from abc import ABC, abstractmethod
from Classes.create_and_query_endpoints import *
from Tools import *
import json

movie_db = MongoClient("mongodb://student:alfred@10.33.86.229:27017")
