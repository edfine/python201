# Used in 01 Intro + Python Syntax Review.ipynb

def dummy():
    return 45
          
public_data = "public stuff!"
_private_data = "private stuff!"

print('__name__ =', __name__)

if __name__ == '__main__':
    # test dummy
    if dummy() == 45:
        print('success')
