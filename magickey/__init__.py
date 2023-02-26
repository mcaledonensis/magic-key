"""
This module inserts the magic key and allows to turn it on or off.

Examples:
    >>> import magickey
    >>> from .examples.person import Person

    >>> merlin = Person("Myrddin Wyllt", 42, "Caledonia") 


    >>> # Using the default iPython matching engine
    >>> magickey.turn_on(merlin, magic_type = None)
    >>> @`merlin.name()`
    Myrddin Wyllt

    >>> @merlin What is your first name?
    Invalid .. .  # TODO add actual error

    >>>
    >>> # Using the default Whoosh sting matching engine
    >>> magickey.turn_on(merlin, magic_type = False)
    >>> @merlin What is your first name?
    Myrddin Wyllt

    >>>
    >>> # Using the intellegence engine
    >>> magickey.turn_on(merlin, magic_type = True)
    
    >>> @`merlin.name()`
    Myrddin Wyllt

    >>> @merlin Please, can you remind me, what is your first name?  It's M... ?
    It's Merlin. People also call me Merlinus and Myrddin. Please, feel free to call me Merlin. It is easier this way in English.

    >>> magickey.turn_off(merlin)      # By default, this backs up the episode and consolidates the memory
"""

def turn_on(object, magic_type=None, engine=None):
    """
    Activates the connector between the python interpreter and intellegence engine. Uses no magic by default.
    :param magic_type: Can be None, False or True. Specifies the type of magic.
    :param engine: Can be None, 'openai', 'magickey'
    :param api_key: Can be None, or the API key for the engine.
    """


    # about = f"I'm Arthur-type intelligence shapeshifting as {name}."



    if magic_type is None:      # exact sting matching
        engine = 'openai'
        pass
    if magic_type is True:      # Using the magickey engine
        engine = 'magickey'

    elif magic_type is False:   # whoosh engine sting matching
        pass
    elif magic_type is True:    # intellegence engine sting matching
        pass
    elif magic_type is 'Merlinus':
        pass
    elif magic_type is 'Myrddin':
        pass
    else:
        raise ValueError("magic_type must be None, False or True")
    

import magickey.magics

# Load the extension when this module is loaded.
magics.load_ipython_extension(get_ipython())


