from django import template

# THIS IS HOW I AM ABLE TO PAGINATE AND KEEP THE FILTER
# All the form input fields for filters (like category, item name, quantity) are automatically appended to the url
# once the form is submitted, even if they are blank.
# This function joins them all together all the fields together 

register = template.Library()

@register.simple_tag
def my_url(value, field_name, urlencode=None):
    url = '?{}={}'.format(field_name, value)

    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = '{}&{}'.format(url, encoded_querystring)

    return url
