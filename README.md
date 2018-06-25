# postcode-utils
Validates and formats postcodes
Currently only UK is supported

# Validate
from postcode_utils import uk
uk.is_valid_postcode('EC1A 1BB')

# Format
uk.format_postcode('EC', '1A', '1', 'BB')
