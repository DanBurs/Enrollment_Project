import os

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or b'I\x85l\xad%\xce\x14\x88\x0e\xad\x05v`\xb7\x03<'
    
    MONGODB_SETTINGS = { 'db' : 'BLT_Enrollment' }