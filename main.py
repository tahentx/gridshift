from fastapi import FastAPI
from pydantic import BaseModel
import logging
import pprint

logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='arrow_nlp_model.log',
                    level=logging.DEBUG)
logging.debug('Placeholder - debug')
logging.info('Placeholder - info')
logging.warning('Placeholder - warning')

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None

@app.get("/")
def read_root():
    return {"Metadata" : {
            "Project" : "NLP - Topic Modeling - Apache Arrow Repository", 
            "Method" : "Non-Negative Matrix Factorization (NMF)",
            "Author" : "Todd Hendricks",
            "Contact" : "hendricks.ta@gmail.com" },
            "Results" : {
            "Topic 0" : "high, mild, time, outliers, measurements, severe",
            "Topic 1" : "51, sec, start, passed, pute, dataset",
            "Topic 2" : "testplasmaserialization, plasma, home, ms, serialization_tests, cc",
            "Topic 3" : "bytes_per_second, cpu, benchmark, time, x10, validatelargeascii",
            "Topic 4" : "schema, true, type, nullable, field, type_type",
            "Topic 5" : "endian, little, failed, failures, big, format",
            "Source" : "https://github.com/apache/arrow"} 
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}