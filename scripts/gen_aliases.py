
same_camera_model = {
    
    'Canon EOS 400D': 'Canon Digital Rebel XTi' ,
    'Canon Kiss Digital X': 'Canon Digital Rebel XTi',
    
    'Canon EOS Rebel SL1': 'Canon EOS 100D',
    'Canon Kiss X7': 'Canon EOS 100D',
    
    'Canon EOS Rebel SL2': 'Canon EOS 200D',
    'Canon Kiss X9': 'Canon EOS 200D',
    
    'Canon EOS 250D': 'Canon EOS 200D II',
    'Canon EOS Rebel SL3': 'Canon EOS 200D II',
    'Canon Kiss X10': 'Canon EOS 200D II',
    
    'Canon EOS Rebel T3i': 'Canon EOS 600D',
    'Canon Kiss X5': 'Canon EOS 600D',
    
}

different_camera_model = {
    
    'Canon EOS 5DS R': 'Canon EOS 5DS',
    'Canon EOS 6D Mark II': 'Canon EOS RP',
    
    'Canon EOS R5 C': 'Canon EOS R5',
    'Canon EOS R50': 'Canon EOS R10',
    
    'Canon EOS R8': 'Canon EOS R6m2',
    
    'Nikon D800' : 'Nikon D800E',
    'Nikon Z 6_2' : 'Nikon Z f',
    
    'Sony ILCE-7RM5': 'Sony ILCE-7RM4',
    
    'Fujifilm GFX100S': 'Fujifilm GFX 100'
}    

updated_camera_model = {
    'Sony ILCE-7RM4A': 'Sony ILCE-7RM4',
    'Sony ILCE-7RM3A': 'Sony ILCE-7RM3',
}    

camera_mapping = [
    (same_camera_model, "same model, alternative name"),
    (different_camera_model, "different model, same sensor"),
    (updated_camera_model, "updated model, same sensor")
]

camera_model_map = {}

for mm in camera_mapping:
    dict = mm[0]
    comment = mm[1]

    for k,v in dict.items():
        src_make = k.split()[0]
        src_model = " ".join(k.split()[1:])
        dst_make = v.split()[0]
        dst_model = " ".join(v.split()[1:])
        
        if not src_make in camera_model_map.keys():
            camera_model_map[src_make] = {}
        
        camera_model_map[src_make][src_model] = {
            "make": dst_make,
            "model": dst_model,
            "comments": comment
        }


import json

json_data = {
    "header": {
        "schema_version": "1.0.0",
        "document_creator": "rawtoaces",
        "document_creation_date": "2026-03-27T06:11:34Z",
        "license": "Apache-2.0"
    },
    "data": {
        "camera":
        {
            "make": {
                "Nikon Corporation": "Nikon"
            },
            "model": camera_model_map
        }
    }
}

with open('./data/aliases.json', 'w') as file:
    json.dump(json_data, file, indent=4)
