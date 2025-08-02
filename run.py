import json

data = None
# with open('Engines_van.json', 'r') as f:
with open('Engines_maja.json', 'r') as f:
    data = json.loads(f.read())
    parts = data.get('Exports')[0].get('Table').get('Data')

    all_parts = []
    first_car_engine_part = None
    first_truck_engine_part = None

    for part in parts:
        part_id = part.get('Name')
        if part_id == 'HeavyDuty_440HP':
            first_truck_engine_part = part
        elif part_id == 'SmallBlock_240HP':
            first_car_engine_part = part
        else:
            all_parts.append(part)

    with open('Engines.json', 'w+') as f:
        data['Exports'][0]['Table']['Data'] = [first_truck_engine_part]+[first_car_engine_part]+all_parts
        f.write(json.dumps(data, indent=4))
    