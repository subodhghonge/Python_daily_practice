# Dictionary - comma separated key-value pairs within curly({}) bracket.
            - Ordered, key-immutable(int, str, tuple), values-mutable, duplicates are not allowed
            - len() used to count elements in dictionary

# Dictionary syntax
            - dict_name = {
                'key1' : 'value1',
                'key2' : 'value2'
            }

# Accessing key-value pairs in dictionary
            1. can access the dictionary value by referring to it's key name inside square bracket similar to indexing
            eg:- dict_name['key_name'] 

            2. get()
            eg:- x = dict_name.get('key_name')

            3. keys() - to get all keys from dictionary
            eg:- x = dict_name.keys()

            4. values() - to get all values from dictionary
            eg:- x = dict_name.values()

            5. items() - to get key_value pairs from dicitonary
            eg:- x = dict_name.items()

# Change Dictionary values
            1. by referring key name we can change items value
            eg :- dict_name['year'] = new_value

            2. update() - update item in dictionary(Key: value)
            eg:- dict_name.update({'key':'value'})

# Add elements in dictionary
            1. by using new index key and assigning value to it
            eg :- dict_name['new_key'] = 'new_value'

            2. update() - update item in dictionary(Key: value)
            eg:- dict_name.update({'key':'value'})

# Remove elements in dictionary
            1. pop() - remove item with specified key name
            eg :- dict_name.pop("key_name")

            2. pop.item() - removes last inserted item
            eg :- dict_name.popitem()

            3. del - remove item with specified key name / delete the entire dictionary
            eg :- del dict_name['key_name'] / del dict_name

            4. clear() - empty the dicitonary
            eg:- dict_name.clear()

# Copy Dictionary
           - dict_name1.copy(dict_name)