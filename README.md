# owlToTextToDB
Extracts information from owl file and stores in a file or database.

This implementation uses sqlite3 database and json files

## Features:
* Print all available predicates form owl file
* Parse triples (subject, object and predicate) 
* Save data to file and / or database
* List subjects and objects from triples

## Usage
* Edit [config.json](https://github.com/gsfig/owlToTextToDB/blob/master/config.json) to change inputs and outputs.
* Comment and uncomment function calls in "main" [owlParser.py](https://github.com/gsfig/owlToTextToDB/blob/master/owlParser.py)