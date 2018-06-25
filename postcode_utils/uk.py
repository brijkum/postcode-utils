'''Validation and formatting of postcodes for UK

Visit https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting for the rules
'''

import re

PATTERN = r'''^([Gg][Ii][Rr] 0[Aa]{2}$)|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$'''


class Error(Exception):
    '''
    Base class for other exceptions
    '''
    pass


class EmptyPostcodeError(Error):
    '''Raised when the input postcode is empty'''
    pass

class IncorrectValueTypeError(Error):
    '''Raised when the postcode parts entered are not of type string'''
    pass


class InvalidValuesProvidedError(Error):
    '''Raised when the postcode parts entered are not valid'''
    pass


def is_valid_postcode(postcode):
    '''Validate postcode for UK

    @param postcode: the postcode to be validated as string
    @return: True or False is returned based on whether it is valid or invalid
    @raise EmptyPostcodeError: raises an exception when postcode provided is empty
    '''
    if not postcode:
        raise EmptyPostcodeError('Empty string provided as postcode')
    match_obj = re.match(PATTERN, postcode)
    if not match_obj:
        return False
    return True

def format_postcode(postcode_area, postcode_district,
                    postcode_sector, postcode_unit):
    '''Generate and format a postcode from it's parts

    @param postcode_area: UK postcode area
    @param postcode_district: UK postcode district
    @param postcode_sector: UK postcode sector
    @param postcode_unit: UK postcode unit
    @return: Formatted postcode if parts input are valid else None
    @raise IncorrectValueTypeError: raises an exception if postcode part(s) is/are not of type string
    '''
    try:
        postcode = (postcode_area + postcode_district + ' ' +
                    postcode_sector + postcode_unit).upper()
    except TypeError as _ :
        raise IncorrectValueTypeError('Postcode parts provided should be of type string')

    if is_valid_postcode(postcode):
        return postcode
    raise InvalidValuesProvidedError('Please provide valid values for postcode area/district/sector/unit')
