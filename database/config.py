from configparser import ConfigParser

def config(filename="database/database.ini", section="postgresql"):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        for param in parser.items(section):
            db[param[0]] = param[1]
    else:
        raise Exception("Section {0} not found in the {1}".format(section, filename))
    return db

