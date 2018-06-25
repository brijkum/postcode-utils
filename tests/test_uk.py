import pytest

from postcode_utils import uk

# Test Cases for is_valid_postcode function
@pytest.mark.parametrize("postcode", [
    ('EC1A 1BB'),
    ('W1A 0AX'),
    ('M1 1AE'),
    ('B33 8TH'),
    ('CR2 6XH'),
    ('DN55 1PT'),
    ('GIR 0AA'),
    ('ec1A 1bB'),
])
def test_valid_formats(postcode):
    '''Testing for different valid formats of type:
    Type      : Example
    AA9A 9AA  : EC1A 1BB
    A9A 9AA   : W1A 0AX
    A9 9AA    : M1 1AE
    A99 9AA   : B33 8TH
    AA9 9AA   : CR2 6XH
    AA99 9AA  : DN55 1PT
    GIR 9AA   : GIR 0AA
    '''
    assert uk.is_valid_postcode(postcode) == True


@pytest.mark.parametrize("postcode", [
    ('EC1A1BB'),
    ('W1A  0AX'),
    (' M1 1AE'),
    ('B33 8TH '),
    (' CR2 6XH '),
    (' DN551PT'),
    ('GIR          0AA'),
])
def test_invalid_space_formats(postcode):
    '''Test for variations of whitespaces in postcode'''
    assert uk.is_valid_postcode(postcode) == False

def test_empty_postcode():
    '''Tests that correct exception is raised in case of an empty postcode'''
    with pytest.raises(uk.EmptyPostcodeError):
        uk.is_valid_postcode('')


@pytest.mark.parametrize("postcode", [
    ('EC1A 1BB2'),
    ('W1A 0AXA'),
    ('M1BC 1AE'),
    ('B33XYZ 8TH'),
    ('C 6XH'),
    ('DN55 PT'),
    ('GIR 0AA AB'),
])
def test_invalid_formats(postcode):
    '''Test for variations of invalid postcodes'''
    assert uk.is_valid_postcode(postcode) == False


# Test Cases for format_postcode function
@pytest.mark.parametrize("postcode_area, postcode_district, postcode_sector, postcode_unit, postcode", [
    ('EC', '1A', '1', 'BB', 'EC1A 1BB'),
    ('W', '1A', '0', 'AX', 'W1A 0AX'),
    ('M', '1', '1', 'AE', 'M1 1AE'),
    ('B', '33', '8', 'TH', 'B33 8TH'),
    ('C', 'R2', '6', 'XH', 'CR2 6XH'),
    ('DN', '55', '1', 'PT', 'DN55 1PT'),
    ('G', 'IR', '0', 'AA', 'GIR 0AA'),
])
def test_formatting_passes(postcode_area, postcode_district, postcode_sector, postcode_unit, postcode):
    '''Test formatting for variations of valid values'''
    assert uk.format_postcode(
        postcode_area, postcode_district, postcode_sector, postcode_unit) == postcode


@pytest.mark.parametrize("postcode_area, postcode_district, postcode_sector, postcode_unit", [
    ('EC', '1A', 1, 'BB'),
    (None, '1A', '0', 'AX'),
])
def test_formatting_incorrect_types(postcode_area, postcode_district, postcode_sector, postcode_unit):
    '''Test formatting for invalid value types'''
    with pytest.raises(uk.IncorrectValueTypeError):
        uk.format_postcode(
            postcode_area, postcode_district, postcode_sector, postcode_unit)


@pytest.mark.parametrize("postcode_area, postcode_district, postcode_sector, postcode_unit", [
    ('EC', '1A', '1', 'BB2'),
    ('W', '1A', '', 'AX'),
])
def test_formatting_invalid_values(postcode_area, postcode_district, postcode_sector, postcode_unit):
    '''Test formatting for invalid postcode values'''
    with pytest.raises(uk.InvalidValuesProvidedError):
        uk.format_postcode(
            postcode_area, postcode_district, postcode_sector, postcode_unit)
