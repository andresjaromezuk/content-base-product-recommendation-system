# %%
import platform
print(platform.machine())
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import applications
# %%
from opensearchpy import Field, Boolean, Float, Integer, Document, Keyword, Text, DenseVector, Nested, Date, Object

class KNNVector(Field):
    name = "knn_vector"
    def __init__(self, dimension, method, **kwargs):
        super(KNNVector, self).__init__(dimension=dimension, method=method, **kwargs)

method = {
    "name": "hnsw",
    "space_type": "cosinesimil",
    #"engine": "nmslib"
}

index_name_1 = 'items'

class Item(Document):
    item_id = Keyword()
    variant_id = Keyword()
    image_url = Keyword()
    title = Text()
    description = Text()
    created_at = Date()
    text_vector = KNNVector(
       839,
        method
    )
    image_vector = KNNVector(
       2048,
        method
    )
    class Index:
        name = index_name_1
        settings = {
                'index': {
                'knn': True
            }
        }
    def save(self, ** kwargs):
        self.meta.id = self.item_id
        return super(Item, self).save(** kwargs)

