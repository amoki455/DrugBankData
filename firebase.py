import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def main():
    cred = credentials.Certificate("google-services-key.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    drugs_collection = db.collection('drugs')
    drugs_info_collection = db.collection('drugs_info')
    drug_references_collection = db.collection('drug_references')
    references_info_collection = db.collection('references_info')

    print('Adding drugs data')
    with open('data.json', 'rt') as f:
        drugs = json.load(f)
        for drug in drugs:
            drugs_collection.add({'drugId': drug['id'], 'name': drug['name'], 'summary': drug['summary']})
            drugs_info_collection.add(drug)

    print('Adding drugs references')
    with open('drug_references.json', 'rt') as f:
        drugs_references = json.load(f)
        for drug_references in drugs_references:
            drug_references_collection.add(drug_references)

    print('Adding references info')
    with open('references_info.json', 'rt') as f:
        references_info = json.load(f)
        for reference_info in references_info:
            references_info_collection.add(reference_info)


if __name__ == '__main__':
    main()
