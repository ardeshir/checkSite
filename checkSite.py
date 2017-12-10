import os
import urllib.request  as urllib2
from datetime import datetime
from urllib.request import urlopen
#from urllib2 import urlopen

SITE = os.environ['site']  # URL of the site to check, stored in the site environment variable
EXPECTED = os.environ['expected']  # String expected to be on the page, stored in the expected environment variable


def validate(res):
    '''Return False to trigger the canary

    Currently this simply checks whether the EXPECTED string is present.
    However, you could modify this to perform any number of arbitrary
    checks on the contents of SITE.
    '''
    #print(res)
    return b'EXPECTED' in res




def lambda_handler(event, context):
    event['time'] = datetime.now()
    print('Checking {} at {}...'.format(SITE, event['time']))
    try:
        if  validate(urlopen(SITE).read()):
            raise Exception('Validation failed')
    except:
        print('Check failed!')
        #print(urlopen(SITE).read())
        raise
    else:
        print('Check passed!')
        return event['time']
    finally:
        print('Check complete at {}'.format(str(datetime.now())))

lambda_handler({}, {})
