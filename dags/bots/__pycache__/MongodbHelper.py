"""
import pymongo
#*********************************CONEXION*****************************************
def get_connection():
    db_name = None
    try:
        myclient = pymongo.MongoClient("mongodb://localhost:27016/")
        db_name = myclient["MentalHealth"]
    except Exception as exception:
        print(exception)
    return db_name

#*********************************CRUD*****************************************
#__________________________________INSERT________________________________________

def insert_document(col_name, query, projection=None):
    try:
        db_name = get_connection()
        col_name = db_name[col_name]
        insert_data = col_name.insert_one(query)
    except Exception as exception:
        print(exception)
    return insert_data

if __name__ == "__main__":
    document = {
        "Indicator": "Toma medicamento las ultimas tres semanas",
        "Group": "By Age",
        "State": "Ecuador",
        "Subgroup": "20 - 27 years",
        "Time Period": 10,
        "Time Period Start Date": "02/07/2023",
        "Time Period End Date": "09/07/2023"
    }
    insert_document("MentalHealthCollection", document)

def get_document(col_name, query, projection=None):
    read_data = None
    try:
        db_name = get_connection()
        col_name = db_name[col_name]
        read_data = col_name.find_one(query, projection)
    except Exception as exception:
        print(exception)
    return read_data

def update_document(col_name, query, update_data):
    result = None
    try:
        db_name = get_connection()
        col_name = db_name[col_name]
        result = col_name.update_many(query, update_data)
        print(f"Modified {result.modified_count} documents")
    except Exception as exception:
        print(exception)
    return result

if __name__ == "__main__":
    query = {"Group": "By Age"}
    update_data = {"$set": {"NewField": "NewValue"}}
    update_document("MentalHealthCollection", query, update_data)
"""